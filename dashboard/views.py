from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from leads.models import Lead
from deals.models import Deal
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from decimal import Decimal
from datetime import date
from calendar import month_abbr
import json



def home(request):
    total_leads = Lead.objects.count()
    new_leads = Lead.objects.filter(status='New').count()
    contacted_leads = Lead.objects.filter(status='Contacted').count()
    qualified_leads = Lead.objects.filter(status='Qualified').count()
    lost_leads = Lead.objects.filter(status='Lost').count()

    total_deals = Deal.objects.count()
    open_deals = Deal.objects.exclude(stage__in=['won', 'lost']).count()
    won_deals = Deal.objects.filter(stage='won').count()
    lost_deals_count = Deal.objects.filter(stage='lost').count()

    total_pipeline_value = Deal.objects.aggregate(total=Sum('value'))['total'] or 0
    open_value = Deal.objects.exclude(stage__in=['won', 'lost']).aggregate(total=Sum('value'))['total'] or 0
    won_value = Deal.objects.filter(stage='won').aggregate(total=Sum('value'))['total'] or 0

    recent_leads = Lead.objects.order_by('-id')[:5]
    recent_deals = Deal.objects.select_related('lead').order_by('-id')[:5]

    # Deal stage chart data
    new_stage_count = Deal.objects.filter(stage='new').count()
    qualified_stage_count = Deal.objects.filter(stage='qualified').count()
    proposal_stage_count = Deal.objects.filter(stage='proposal').count()
    won_stage_count = Deal.objects.filter(stage='won').count()
    lost_stage_count = Deal.objects.filter(stage='lost').count()

    new_stage_value = Deal.objects.filter(stage='new').aggregate(total=Sum('value'))['total'] or Decimal('0')
    qualified_stage_value = Deal.objects.filter(stage='qualified').aggregate(total=Sum('value'))['total'] or Decimal('0')
    proposal_stage_value = Deal.objects.filter(stage='proposal').aggregate(total=Sum('value'))['total'] or Decimal('0')
    won_stage_value = Deal.objects.filter(stage='won').aggregate(total=Sum('value'))['total'] or Decimal('0')
    lost_stage_value = Deal.objects.filter(stage='lost').aggregate(total=Sum('value'))['total'] or Decimal('0')

    # Monthly lead trends
    # Last 6 months labels
    today = date.today()
    months = []

    for i in range(5, -1, -1):
        year = today.year
        month = today.month - i

        while month <= 0:
            month += 12
            year -= 1

        months.append((year, month))

    month_labels = [f"{month_abbr[m]} {y}" for y, m in months]

    # Lead monthly data
    lead_monthly_qs = (
        Lead.objects
        .annotate(month=TruncMonth('created_at'))
        .values('month')
        .annotate(total=Count('id'))
        .order_by('month')
    )

    lead_data_map = {}
    for item in lead_monthly_qs:
        if item['month']:
            key = (item['month'].year, item['month'].month)
            lead_data_map[key] = item['total']

    lead_month_counts = [lead_data_map.get((y, m), 0) for y, m in months]

    # Deal monthly data
    deal_monthly_qs = (
        Deal.objects
        .annotate(month=TruncMonth('created_at'))
        .values('month')
        .annotate(total=Count('id'))
        .order_by('month')
    )

    deal_data_map = {}
    for item in deal_monthly_qs:
        if item['month']:
            key = (item['month'].year, item['month'].month)
            deal_data_map[key] = item['total']

    deal_month_counts = [deal_data_map.get((y, m), 0) for y, m in months]

    lead_month_labels = month_labels
    deal_month_labels = month_labels
    
    lead_status_counts = [
        Lead.objects.filter(status='New').count(),
        Lead.objects.filter(status='Contacted').count(),
        Lead.objects.filter(status='Qualified').count(),
        Lead.objects.filter(status='Lost').count(),
    ]

    top_leads_qs = (
        Lead.objects
        .annotate(deal_count=Count('deals'))
        .filter(deal_count__gt=0)
        .order_by('-deal_count', 'id')[:5]
    )

    top_lead_labels = [str(lead) for lead in top_leads_qs]
    top_lead_deal_counts = [lead.deal_count for lead in top_leads_qs]

    context = {
        'total_leads': total_leads,
        'new_leads': new_leads,
        'contacted_leads': contacted_leads,
        'qualified_leads': qualified_leads,
        'lost_leads': lost_leads,

        'total_deals': total_deals,
        'open_deals': open_deals,
        'won_deals': won_deals,
        'lost_deals_count': lost_deals_count,
        'lead_status_counts': lead_status_counts,
        'top_lead_labels': json.dumps(top_lead_labels),
        'top_lead_deal_counts': json.dumps(top_lead_deal_counts),
        'won_lost_counts': [won_deals, lost_deals_count],
        'total_pipeline_value': total_pipeline_value,
        'open_value': open_value,
        'won_value': won_value,

        'recent_leads': recent_leads,
        'recent_deals': recent_deals,

        'deal_stage_counts': [
            new_stage_count,
            qualified_stage_count,
            proposal_stage_count,
            won_stage_count,
            lost_stage_count,
        ],
        'deal_stage_values': [
            float(new_stage_value),
            float(qualified_stage_value),
            float(proposal_stage_value),
            float(won_stage_value),
            float(lost_stage_value),
        ],

        'lead_month_labels': json.dumps(lead_month_labels),
        'lead_month_counts': json.dumps(lead_month_counts),
        'deal_month_labels': json.dumps(deal_month_labels),
        'deal_month_counts': json.dumps(deal_month_counts),
    }

    return render(request, 'dashboard/home.html', context)