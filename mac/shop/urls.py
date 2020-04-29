from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'ShopHome'),
    path('about/',views.about, name = 'AboutUs'),
    path('contact/',views.contact, name = 'ContactUs'),
    # to get tracking status
    path('tracker/',views.tracker, name = 'TrackingStatus'),
    # search functionality
    path('search/',views.search, name = 'Search'),
    # products view
    # to send id of the product along with the request
    path('products/<int:myid>',views.productView, name = 'ProductView'),
    # checkout page
    path('checkout/',views.checkout, name = 'Checkout'),
    # handle request from paytm
    path('handlerequest/',views.checkout, name = 'HandleRequest'),
]
