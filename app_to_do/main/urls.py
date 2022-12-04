from django.urls import path
from . import views

from django.contrib.auth.decorators import login_required

from django.contrib.auth import views as auth_views


app_name = "main"

urlpatterns = [

    path('Error404/', views.ErrorView.as_view(), name="error"),
    path('blank/', views.BlankView.as_view(), name="blank"),
    path('buttons/', views.ButtonsView.as_view(), name="button"),
    path('cards/', views.CardsView.as_view(), name="cards"),
    path('charts/', views.ChartsView.as_view(), name="charts"),
    
    path('', login_required(views.IndexView.as_view()), name="index"),
    path('accounts/login/', views.LoginView, name="login"),
    path('register/', views.RegisterView, name="register"),
    path('tables/', views.TablesView.as_view(), name="tables"),
    path('utilitiesAnimation/', views.UtilitiesAnimationView.as_view(), name="utilitiesAnimation"),
    path('utilitiesBorder/', views.UtilitiesBorderView.as_view(), name="utilitiesBorder"),
    path('utilitiesColor/', views.UtilitiesColorView.as_view(), name="utilitiesColor"),
    path('utilitiesOther/', views.UtilitiesOtherView.as_view(), name="utilitiesOther"),
    
    path('creacionTareas/', login_required(views.CreationTareasView.as_view()), name="creacionTareas"),

	path('logout/', views.LogoutUserView, name="logout"),
]

