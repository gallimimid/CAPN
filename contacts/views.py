from django.views.generic.base import TemplateView
from django.http import JsonResponse
from django.db.models import Q
from contacts.models import Product

class IndexView(TemplateView):
    template_name = 'contacts/index.html'

####################
### Part # Query ###
####################
def part_numberQuery(request):
    part_num = request.GET.get('q')
    product_result = {'result':list(Product.objects.filter(
        Q(catalog_number__icontains=part_num) |
        Q(style_number__icontains=part_num)).values(
            'catalog_number',
            'style_number',
            'contact__name',
            'contact__phone',
            'contact__email',
            'contact__link'))[:42]}
    return JsonResponse(product_result, safe=True)