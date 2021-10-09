from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import movieform
# Create your views here.
def add(request):
    obj=Movie.objects.all()
    return render(request,'index.html',{'result':obj})
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'mov':movie})
def adds(request):
    if request.method=='POST':
        name=request.POST.get('name')
        dis = request.POST.get('dis')
        rate = request.POST.get('rating')
        image = request.FILES['img']
        movie=Movie(name=name,des=dis,rating=rate,image=image)
        movie.save()
    return render(request,'add.html')
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
