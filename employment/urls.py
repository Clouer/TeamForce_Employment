from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from employment import views

urlpatterns = [
    path('', views.UsersView.as_view(), name='main'),
    path('login/', views.SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('profile/', login_required(views.ProfileView.as_view(), login_url='/login/'), name='profile'),
    path('add_skill/', views.AddSkilView.as_view(), name='add_skill'),

]
