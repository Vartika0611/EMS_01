from django.shortcuts import render,HttpResponse,redirect
from .models import empinfo

# Create your views here.
def home(request):
       show=empinfo.objects.all()
       if request.method=="POST":
              name=request.POST['name']
              designation=request.POST['designation']
              email=request.POST['email']
              salary=request.POST['salary']
              # new_file=request.FILES['new_file']
              
              sh=empinfo(name=name,designation=designation,email=email,salary=salary)
              sh.save()
              return redirect('home')
       return render(request,'home.html',{'ab':show})