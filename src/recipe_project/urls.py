from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from recipes import views as recipe_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', recipe_views.home_view, name='home'),
    path('recipes/', include('recipes.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logged_out.html'), name='logout'),
    path('register/', recipe_views.register_view, name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
