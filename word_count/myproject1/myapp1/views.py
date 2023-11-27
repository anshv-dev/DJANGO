from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
   # return HttpResponse('<h1>Hi,Bro</h1')
  return render(request,'index.html')
 
  
  
  # name='ANSH'
  # return render(request,'index.html',{'name':name})
def counter(request):
  words=request.GET['text'] #POST ka error dikha rha tha yaha 
  amount_words=len(words.split())
  return render(request,'counter.html',{'amount':amount_words})  