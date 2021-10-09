from django.shortcuts import render,HttpResponse,redirect
from .forms import BlogForm
from .models import Blog
import os




def home(request):
	content = Blog.objects.all()
	return render(request,"home.html",{'content':content})


def blog_add(request):
	if request.method == 'POST':
		form = BlogForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect("home")
	else:
		form = BlogForm()
	return render(request,"blogadd.html",{'form':form})

def blog_edit(request,id):
	content = Blog.objects.get(id=id)
	# form = BlogForm(request.POST,request.FILES,instance=content)
	# if form.is_valid():
	# 	form.save()
	# 	return redirect('/')
	if request.method =="POST":
		if len(request.FILES) !=0:  
			if len(content.bloggerimage)>0:#check the image is having or not
				os.remove(content.bloggerimage.path) #remove previous image for content 
				content.bloggerimage=request.FILES['bloggerimage']
				content.title=request.POST.get('title')
				content.name=request.POST.get('name')
				content.date=request.POST.get('date')
				content.blog=request.POST.get('blog')
				
				content.save()
				return redirect('/')
	return render(request,'blogedit.html',{'content':content})


def blog_update(request,id):
	content = Blog.objects.get(id=id)
	return render(request,'edit.html',{'form':form})



def blog_trash(request,id):
	
	content = Blog.objects.get(id=id)
	if len(content.bloggerimage) > 0:
		os.remove(content.bloggerimage.path)  #delete media from path 
	content.delete()
	return redirect("/")