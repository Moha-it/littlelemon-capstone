from django.urls import path
from api.views import  MenuViewListCreateAPIView, MenuRetrieveUpdateView,BookingViewSet ,BookingRetrieveUpdateView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu/', MenuViewListCreateAPIView.as_view(), name='menuitem-list-create'),
    path('menu/<int:pk>/', MenuRetrieveUpdateView.as_view(), name='menuitem-retrieve-update'),
    path('booking/', BookingViewSet.as_view() ,name='booking-list-create'),   
    path('booking/<int:pk>/', BookingRetrieveUpdateView.as_view(), name='booking-retrieve-update'),
    path('api-token-auth/', obtain_auth_token),
    
]