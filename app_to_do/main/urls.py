from django.urls import path
from . import views


app_name = "main"

urlpatterns = [

    path('Error404/', views.ErrorView.as_view(), name="error"),
    path('blank/', views.BlankView.as_view(), name="blank"),
    path('buttons/', views.ButtonsView.as_view(), name="button"),
    path('cards/', views.CardsView.as_view(), name="cards"),
    path('charts/', views.ChartsView.as_view(), name="charts"),
    path('forgotPassword/', views.ForgotPasswordView.as_view(), name="forgotPassword"),
    path('', views.IndexView.as_view(), name="index"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('tables/', views.TablesView.as_view(), name="tables"),
    path('utilitiesAnimation/', views.UtilitiesAnimationView.as_view(), name="utilitiesAnimation"),
    path('utilitiesBorder/', views.UtilitiesBorderView.as_view(), name="utilitiesBorder"),
    path('utilitiesColor/', views.UtilitiesColorView.as_view(), name="utilitiesColor"),
    path('utilitiesOther/', views.UtilitiesOtherView.as_view(), name="utilitiesOther"),
    
	path('logout/', views.logoutUser, name="logout"),
]

    