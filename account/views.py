from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Profile
from django.views.generic import DetailView,CreateView,UpdateView
from .forms import CustomSignupForm 
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import FormView



class Profilepageview(DetailView):
    model=Profile
    template_name='profile_view.html'
    context_object_name='profile'


    def get_object(self, queryset=None):
        profile = super().get_object(queryset)
        profile.update_badge()  # Update the badge field
        profile.save()  # Save the profile instance with the updated badge
        return profile


class ProfileUpdatePage(LoginRequiredMixin,UpdateView):
    model=Profile
    fields=['profile_picture','bio',]
    template_name='profile_update.html'


    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})


class SignUpview(CreateView):
    form_class=CustomSignupForm
    success_url=reverse_lazy('login')
    template_name='registration/signup.html'
    
    def form_invalid(self, form):
        username = form.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():

            messages.error(self.request, 'Username already exists.')
        else:
            messages.error(self.request, ' Choose another username/Failed to create an account.')
        return self.render_to_response(self.get_context_data(form=form))



    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('login')
    



