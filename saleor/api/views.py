from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
import django_filters
from rest_framework import parsers, filters
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.authtoken.views import ObtainAuthToken


from saleor.product.models.base import Product, ProductVariant
from .serializers import ProductSerializer, ProductVariantSerializer

class ObtainAuthTokenXML(ObtainAuthToken):
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,XMLParser)
    renderer_classes = (XMLRenderer,)

obtain_auth_token_xml = ObtainAuthTokenXML.as_view()



class ProductFilter(django_filters.FilterSet):
    # Defining Filter on Product Price
    min_price = django_filters.NumberFilter(name="price", lookup_type='gte')
    max_price = django_filters.NumberFilter(name="price", lookup_type='lte')
    # Defining Filter on Product Category
    category = django_filters.CharFilter(name="categories__name")
    #

    class Meta:
        model = Product
        # Filters on name, category and price
        fields = ['name','categories','price','weight']



class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Product.objects.all()
    authentication_classes = (BasicAuthentication, TokenAuthentication, SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = (XMLRenderer, JSONRenderer,)
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name','categories__name')
    ordering_fields = ('name')
    filter_class = ProductFilter
    serializer_class = ProductSerializer

class ProductVariantFilter (django_filters.FilterSet):
    # Defining Filter on Product Price
    min_price = django_filters.NumberFilter(name="price_override", lookup_type='gte')
    max_price = django_filters.NumberFilter(name="price_override", lookup_type='lte')
    # Defining Filter on Product Category
    product = django_filters.CharFilter(name="product__name")
    #

    class Meta:
        model = ProductVariant
        # Filters on name, category and price
        fields = ['name','product','price_override','weight_override']





class ProductVariantViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = ProductVariant.objects.all()
    authentication_classes = (BasicAuthentication, TokenAuthentication, SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = (XMLRenderer, JSONRenderer,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ProductVariantFilter
    serializer_class = ProductVariantSerializer



