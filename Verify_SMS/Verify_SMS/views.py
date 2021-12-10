from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from Codes.forms import CodeForm
# from django.forms import ModelForm
from Users.models import CustomUser


@login_required
def home_view(request):
    return render(request, 'main.html', {})

def auth_view(request):
    form= AuthenticationForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['pk'] =  user.pk
            return redirect('verify_view')
    return render(request, 'auth.html', {'form':form})

def verify_view(request):
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')
    if pk:
        user = CustomUser.objects.get(pk=pk)
        code = user.code
        code_user = f"{user.username}: {user.code}"

        # send sms if not makes sure that the sms code is sent once
        if not request.POST:
            print(code_user)
            # pass
            if form.is_valid():
                nun = form.cleaned_data.get('number')

                if str(code)== nun:
                    code.save()
                    login(request,user)
                    return redirect('home')

                else:
                    return redirect('login_view')
    return render(request, 'verify.html', {'form':form})                    

# not suer of linings

                  

