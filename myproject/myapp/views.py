from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
  # return HttpResponse('<h1>Hi,Bro</h1')
  
  context={
    'name':'ANSH VERMA',
    'age':18,
    'Current_edu':'KIET GROUP OF INSTITUTION'
  }
  return render(request,'index.html',context)
  
  # name='ANSH'
  # return render(request,'index.html',{'name':name})