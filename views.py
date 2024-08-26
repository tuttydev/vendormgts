# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vendor, Contract, PerformanceRating, Procurement
from .forms import VendorForm, ContractForm, RatingForm, ProcurementForm
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

class VendorDeleteView(DeleteView):
    model = Vendor
    success_url = reverse_lazy('vendor_list')
    template_name = 'vendors/vendor_confirm_delete.html'


class VendorUpdateView(UpdateView):
    model = Vendor
    fields = ['name', 'email', 'phone', 'address']  # Include the fields you want to update
    template_name = 'vendors/vendor_update.html'  # Fixed the typo here ('emplate_name' to 'template_name')
    success_url = reverse_lazy('vendor_list')

def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendors/vendor_list.html', {'vendors': vendors})

def vendor_detail(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)  # Better error handling with get_object_or_404
    contracts = Contract.objects.filter(vendor=vendor)
    ratings = PerformanceRating.objects.filter(vendor=vendor)
    procurements = Procurement.objects.filter(vendor=vendor)
    return render(request, 'vendors/vendor_detail.html', {
        'vendor': vendor,
        'contracts': contracts,
        'ratings': ratings,
        'procurements': procurements
    })

def add_vendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor_list')
    else:
        form = VendorForm()
    return render(request, 'vendors/add_vendor.html', {'form': form})

# Similarly, create views for Contracts, PerformanceRatings, and Procurements
