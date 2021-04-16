from django.urls import path
from app1.views import RegisterView, MyObtainTokenPairView, SigninView, UpdateProfileView, TicketAPIView, ListTicketView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('token_request/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    #path('token_request/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('signin/', SigninView.as_view(), name='sign_in'),
    path('updateprofile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('ticket/', TicketAPIView.as_view(), name='ticket_save'),
    path('listticket/', ListTicketView.as_view(), name='list_ticket'),
]