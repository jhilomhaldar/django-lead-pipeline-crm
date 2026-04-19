from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Deal
from .forms import DealForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@login_required
def deal_list(request):
    deals = Deal.objects.select_related('lead').order_by('-created_at')

    # Filters
    search = request.GET.get('search', '')
    stage = request.GET.get('stage', '')
    lead_id = request.GET.get('lead', '')
    min_value = request.GET.get('min_value', '')
    max_value = request.GET.get('max_value', '')

    if search:
        deals = deals.filter(title__icontains=search)

    if stage:
        deals = deals.filter(stage=stage)

    if lead_id:
        deals = deals.filter(lead_id=lead_id)

    if min_value:
        deals = deals.filter(value__gte=min_value)

    if max_value:
        deals = deals.filter(value__lte=max_value)

    # Pagination
    paginator = Paginator(deals, 5)   # 5 deals per page
    page_number = request.GET.get('page')
    deals = paginator.get_page(page_number)

    # For dropdowns
    from leads.models import Lead
    leads = Lead.objects.all()

    context = {
        'deals': deals,
        'page_obj': deals,
        'leads': leads,
        'search': search,
        'selected_stage': stage,
        'selected_lead': lead_id,
        'min_value': min_value,
        'max_value': max_value,
    }

    return render(request, 'deals/deal_list.html', context)


@login_required
def deal_create(request):
    lead_id = request.GET.get('lead')

    if request.method == 'POST':
        form = DealForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Deal created successfully.')
            return redirect('deal_list')
    else:
        initial_data = {}
        if lead_id:
            initial_data['lead'] = lead_id
        form = DealForm(initial=initial_data)

    return render(request, 'deals/deal_form.html', {
        'form': form,
        'page_title': 'Add Deal'
    })

@login_required
def deal_edit(request, pk):
    deal = get_object_or_404(Deal, pk=pk)

    if request.method == 'POST':
        form = DealForm(request.POST, instance=deal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Deal updated successfully.')
            return redirect('deal_list')
    else:
        form = DealForm(instance=deal)

    return render(request, 'deals/deal_form.html', {
        'form': form,
        'page_title': 'Edit Deal'
    })


@login_required
def deal_delete(request, pk):
    deal = get_object_or_404(Deal, pk=pk)

    if request.method == 'POST':
        deal.delete()
        messages.success(request, 'Deal deleted successfully.')
        return redirect('deal_list')

    return render(request, 'deals/deal_confirm_delete.html', {'deal': deal})


@login_required
def deal_pipeline(request):
    deals_new = Deal.objects.filter(stage='new').select_related('lead').order_by('-created_at')
    deals_qualified = Deal.objects.filter(stage='qualified').select_related('lead').order_by('-created_at')
    deals_proposal = Deal.objects.filter(stage='proposal').select_related('lead').order_by('-created_at')
    deals_won = Deal.objects.filter(stage='won').select_related('lead').order_by('-created_at')
    deals_lost = Deal.objects.filter(stage='lost').select_related('lead').order_by('-created_at')

    new_total = sum(deal.value for deal in deals_new)
    qualified_total = sum(deal.value for deal in deals_qualified)
    proposal_total = sum(deal.value for deal in deals_proposal)
    won_total = sum(deal.value for deal in deals_won)
    lost_total = sum(deal.value for deal in deals_lost)

    context = {
        'deals_new': deals_new,
        'deals_qualified': deals_qualified,
        'deals_proposal': deals_proposal,
        'deals_won': deals_won,
        'deals_lost': deals_lost,

        'new_count': deals_new.count(),
        'qualified_count': deals_qualified.count(),
        'proposal_count': deals_proposal.count(),
        'won_count': deals_won.count(),
        'lost_count': deals_lost.count(),

        'new_total': new_total,
        'qualified_total': qualified_total,
        'proposal_total': proposal_total,
        'won_total': won_total,
        'lost_total': lost_total,

        'total_count': deals_new.count() + deals_qualified.count() + deals_proposal.count() + deals_won.count() + deals_lost.count(),
        'open_total': new_total + qualified_total + proposal_total,
        'grand_total': new_total + qualified_total + proposal_total + won_total + lost_total,
    }

    return render(request, 'deals/deal_pipeline.html', context)

@login_required
def deal_detail(request, pk):
    deal = get_object_or_404(Deal.objects.select_related('lead'), pk=pk)

    return render(request, 'deals/deal_detail.html', {
        'deal': deal
    })

@login_required
@require_POST
def update_deal_stage(request):
    deal_id = request.POST.get('deal_id')
    new_stage = request.POST.get('new_stage')

    valid_stages = ['new', 'qualified', 'proposal', 'won', 'lost']

    if not deal_id or new_stage not in valid_stages:
        return JsonResponse({
            'success': False,
            'message': 'Invalid request'
        }, status=400)

    try:
        deal = Deal.objects.get(pk=deal_id)
        deal.stage = new_stage
        deal.save()

        return JsonResponse({
            'success': True,
            'message': 'Deal stage updated successfully'
        })
    except Deal.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Deal not found'
        }, status=404)