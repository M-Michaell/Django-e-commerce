from django.shortcuts import render ,reverse,redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import DetailView
from accounts.forms import CustomUserCreationForm

# Create your views here.


def profile(request) :
    return redirect(f"/accounts/profile/{request.user.id}")

def logout(request):
    return redirect("/accounts/login")


class CustomUserCreate(CreateView):
    model = User
    template_name="accounts/registration.html"
    form_class = CustomUserCreationForm
    success_url =reverse_lazy("login")




class UserProfileView(DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'user'



class UserProfileUpdateView(UpdateView):
    print("hello")
    model = User
    template_name = 'accounts/update.html'
    form_class = CustomUserCreationForm
    # url=reverse("account.profile2")
    success_url = reverse_lazy('login')
    # context_object_name = 'user'

class DeleteUser(DeleteView):
  model = User
  template_name = 'accounts/delete.html'
  success_url = reverse_lazy('accounts.create')
  