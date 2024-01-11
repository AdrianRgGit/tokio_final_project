from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from django.utils.decorators import method_decorator


# Create your views here.
class SignUpView(View):
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)

        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    template_name = 'registration/profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
