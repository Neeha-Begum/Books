from django.shortcuts import render,redirect
from app1.models import *

# Create your views here.
def homeview(request):
    obj=Book.objects.all()
    return render(request,'home.html',{'books':obj})

def bookview(request):
    if request.method=="POST":
        title=request.POST.get('title')
        genre=request.POST.get('genre')
        price=request.POST.get('price')
        authorid=int(request.POST.get('author'))
        a=Author.objects.get(id=authorid)
        obj=Book(title=title,genre=genre,price=price,author=a)
        obj.save()
        return redirect('homepage')
    return render(request,'book.html')

def authorview(request):
    if request.method=="POST":
        name=request.POST.get('name')
        age=int(request.POST.get('age'))
        rating=int(request.POST.get('rating'))
        obj=Author(name=name,age=age,rating=rating)
        obj.save()
        return redirect('homepage')
    return render(request,'author.html')

def deleteview(request,rid):
    if request.user.is_superuser:
        obj=Book.objects.get(id=rid)
        obj.delete()
        return redirect('homepage')
    return render(request,'home.html')

