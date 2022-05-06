from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, UpdateView
from .models import Blog
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import Q

def Index(request):
    query = request.POST.get('query')

    if query:
        blogs = Blog.objects.filter(
            Q(title__contains=query) | Q(content__contains=query)
        ).order_by('-created_datetime')

    else:
        blogs = Blog.objects.order_by('-created_datetime')

    return render(request, 'blog_app/index.html', {'blogs': blogs})

class CreateBlog(CreateView):
    model = Blog
    template_name = "blog_app/create.html"
    fields = ('title', 'img', 'content')
    success_url = reverse_lazy('blog_app:index')

def Detail(request, num):
   obj = Blog.objects.get(pk=num)
   return render(request, 'blog_app/detail.html', {'obj' :obj })

def Delete(request, num):
   obj = Blog.objects.get(pk=num)
   if (request.method == 'POST'):
       obj.delete()
       return redirect(to='blog_app:index')
   
   return render(request, 'blog_app/detail.html', {'obj' :obj })


class UpdateBlog(UpdateView):
   template_name = 'blog_app/update.html'
   model = Blog
   fields = ('title', 'img', 'content')
   context_object_name = 'obj'
   success_url = reverse_lazy('blog_app:index')
