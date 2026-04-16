from django.shortcuts import render
from leads.models import Lead


def home(request):
    total_leads = Lead.objects.count()
    new_leads = Lead.objects.filter(status='New').count()
    contacted_leads = Lead.objects.filter(status='Contacted').count()
    qualified_leads = Lead.objects.filter(status='Qualified').count()
    lost_leads = Lead.objects.filter(status='Lost').count()

    context = {
        'total_leads': total_leads,
        'new_leads': new_leads,
        'contacted_leads': contacted_leads,
        'qualified_leads': qualified_leads,
        'lost_leads': lost_leads,
    }

    return render(request, 'dashboard/home.html', context)