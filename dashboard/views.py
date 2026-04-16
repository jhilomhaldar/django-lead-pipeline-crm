from django.shortcuts import render
from leads.models import Lead


def home(request):
    total_leads = Lead.objects.count()

    context = {
        'total_leads': total_leads,
    }

    return render(request, 'dashboard/home.html', context)