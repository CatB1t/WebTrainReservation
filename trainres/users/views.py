from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('trainres-home')
    else:
        form = UserRegisterationForm()
    return render(request, 'users/register.html', {'form': form})