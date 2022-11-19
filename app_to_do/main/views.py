from django.views import generic

class ErrorView(generic.TemplateView):
	template_name = "main/404.html"

class BlankView(generic.TemplateView):
	template_name = "main/blank.html"

class ButtonsView(generic.TemplateView):
	template_name = "main/buttons.html"

class CardsView(generic.TemplateView):
	template_name = "main/cards.html"

class ChartsView(generic.TemplateView):
	template_name = "main/charts.html"

class ForgotPasswordView(generic.TemplateView):
	template_name = "main/forgot-password.html"

class IndexView(generic.TemplateView):
	template_name = "main/index.html"

class LoginView(generic.TemplateView):
	template_name = "main/login.html"

class RegisterView(generic.TemplateView):
	template_name = "main/register.html"

class TablesView(generic.TemplateView):
	template_name = "main/tables.html"

class UtilitiesAnimationView(generic.TemplateView):
	template_name = "main/utilities-animation.html"

class UtilitiesBorderView(generic.TemplateView):
	template_name = "main/utilities-border.html"

class UtilitiesColorView(generic.TemplateView):
	template_name = "main/utilities-color.html"

class UtilitiesOtherView(generic.TemplateView):
	template_name = "main/utilities-other.html"

