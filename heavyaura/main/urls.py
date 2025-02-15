from django.urls import path, include
from . import views


app_name = 'main'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('',views.popular_list, name='popular_list'),
    path('register/',views.register, name='register'),
    path('authtorisation/', views.authtorisation, name='authtorisation'),
 
    
]
