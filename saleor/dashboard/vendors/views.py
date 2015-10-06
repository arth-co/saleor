from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.utils.http import is_safe_url
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.http import require_http_methods

from ...userprofile.models import Vendor

from ..utils import paginate
from ..views import staff_member_required
from . import forms

@staff_member_required
def vendor_list(request):
    vendors = (Vendor.objects
                .prefetch_related('users','warehouses')
                .select_related('default_warehouse','admin_user'))

    form = forms.VendorForm(request.POST or None)

    if form.is_valid():
        return redirect('dashboard:vendor-add')
    vendors, paginator = paginate(vendors, 30, request.GET.get('page'))
    ctx = {'form': form, 'vendors': vendors, 'paginator': paginator}
    return TemplateResponse(request, 'dashboard/vendors/list.html', ctx)

