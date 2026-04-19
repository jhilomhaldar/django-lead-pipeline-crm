from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from leads.models import Lead
from deals.models import Deal
from django.db.models import Sum


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
        'total_pipeline_value': total_pipeline_value,
        'open_value': open_value,
        'won_value': won_value,

        'recent_leads': recent_leads,
        'recent_deals': recent_deals,
    }

    return render(request, 'dashboard/home.html', context)