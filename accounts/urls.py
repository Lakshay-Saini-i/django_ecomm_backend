from django.urls import path
from .views import login_page, register_page, activate_email


urlpatterns= [
    path('login/', view=login_page, name='login'),
    path('register/', view=register_page, name='register'),
    path('activate/<email_token>/', view=activate_email, name= 'activate_email')
]


