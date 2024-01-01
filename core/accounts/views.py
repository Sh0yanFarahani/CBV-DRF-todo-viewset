from .forms import RegistrationForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.shortcuts import redirect


class RegisterPage(FormView):
    template_name = "registration/register.html"
    form_class = RegistrationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("task:task-list")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("task:task-list")
        return super(RegisterPage, self).get(*args, **kwargs)
    