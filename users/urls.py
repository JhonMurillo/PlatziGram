from django.urls import path
from users import views 

urlpatterns = [
    path('', views.login_view, name='login'),
    path('/logout', views.logout_view, name='logout')
]