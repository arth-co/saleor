from __future__ import unicode_literals

from django import forms
from django.forms.models import inlineformset_factory
from django.utils.translation import pgettext_lazy

from ...userprofile.models import Vendor



'''
class ProductClassForm(forms.Form):
    product_cls = forms.ChoiceField(
        label=pgettext_lazy('Product class form label', 'Product class'),
        widget=forms.RadioSelect,
        choices=[(cls.__name__, presentation) for cls, presentation in
                 PRODUCT_CLASSES.items()])

    def __init__(self, *args, **kwargs):
        super(ProductClassForm, self).__init__(*args, **kwargs)
        product_class = next(iter((PRODUCT_CLASSES)))
        self.fields['product_cls'].initial = product_class.__name__


'''


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name','users','warehouses']

    def __init__(self, *args, **kwargs):
        super(VendorForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = pgettext_lazy(
            'Product form labels', 'Enter the Vendor Name')
        self.fields['warehouses'].widget.attrs['data-placeholder'] = pgettext_lazy(
            'Product form labels', 'Select warehouse addresses')
        self.fields['users'].widget.attrs['data-placeholder'] = pgettext_lazy(
            'Product form labels', 'Select users')
