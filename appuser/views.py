from django.shortcuts import render
from django.views.generic import CreateView
from . import forms
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.
# signup view
class UserSignUpView(CreateView):
    template_name = 'signup.html'
    form_class = forms.UserSignUpForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # messages.success(self.request, 'Account created successfully! Please log in.')
        return super().form_valid(form)
