from django import forms
from .models import Vendor, Contract, PerformanceRating, Procurement

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'contact_name', 'email', 'phone', 'address']

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['vendor', 'contract_title', 'start_date', 'end_date', 'contract_value']

class RatingForm(forms.ModelForm):
    class Meta:
        model = PerformanceRating
        fields = ['vendor', 'rating', 'comments']

class ProcurementForm(forms.ModelForm):
    class Meta:
        model = Procurement
        fields = ['vendor', 'item_description', 'quantity', 'unit_price', 'total_price', 'date_of_procurement']
