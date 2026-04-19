from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Lead
from .forms import LeadForm
from django.db.models import Q
from django.core.paginator import Paginator
from deals.models import Deal

@login_required
def lead_list(request):
    q = request.GET.get('q', '')
    status = request.GET.get('status', '')

    leads = Lead.objects.all().order_by('-created_at')

    if q:
        leads = leads.filter(
            Q(first_name__icontains=q) |
            Q(last_name__icontains=q) |
            Q(email__icontains=q) |
            Q(company__icontains=q) |
            Q(phone__icontains=q)
        )

    if status:
        leads = leads.filter(status=status)

    paginator = Paginator(leads, 5)  # 5 leads per page
    page_number = request.GET.get('page')
    leads = paginator.get_page(page_number)

    return render(request, 'leads/lead_list.html', {'leads': leads})

@login_required
def lead_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    related_deals = Deal.objects.filter(lead=lead).order_by('-created_at')

    return render(request, 'leads/lead_detail.html', {
        'lead': lead,
        'related_deals': related_deals,
    })

@login_required
def lead_create(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lead_list')
    else:
        form = LeadForm()

    return render(request, 'leads/lead_form.html', {
                                                        'form': form,
                                                        'page_title': 'Add Lead',
                                                        'page_subtitle': 'Create a new lead in Room CRM.',
                                                        'button_text': 'Save Lead',
                                                    })


@login_required
def lead_edit(request, pk):
    lead = get_object_or_404(Lead, pk=pk)

    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('lead_list')
    else:
        form = LeadForm(instance=lead)

    return render(request, 'leads/lead_form.html', {
                                                        'form': form,
                                                        'page_title': 'Edit Lead',
                                                        'page_subtitle': 'Update lead information in Room CRM.',
                                                        'button_text': 'Update Lead',
                                                    })    
                                                

@login_required
def lead_delete(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    lead.delete()
    return redirect('lead_list')