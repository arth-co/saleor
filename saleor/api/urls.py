__author__ = 'hkalra'


from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
#from rest_framework.authtoken import views as auth_token_views

from saleor.api import views


router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'product_variants', views.ProductVariantViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^token-auth/', views.obtain_auth_token_xml)

    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^api-token-auth/', auth_token_views.obtain_auth_token),
]
