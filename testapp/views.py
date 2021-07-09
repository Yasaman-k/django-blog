from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
from .forms import AddPostForm
from django.views import generic

class BlogView(generic.ListView):
    template_name='testapp/Home.html'
    context_object_name='blogpost'

    def get_queryset(self):
        return Blog.objects.all()

class BlogDetail(generic.DeleteView):
    model= Blog
    template_name='testapp/BlogDetail.html'

def Addpost(request):
    if request.method == "POST":
        form = AddPostForm(request.POST , request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            image = form.cleaned_data['image']
            author = request.user

            blog = Blog.objects.create(title= title, content=content , author=author , image=image)
            blog.save()
            return HttpResponse('blog post created')
    else:
        #vase zamani k method get bashe v user taze varede on url shode bashe
        # print(request.user)
        form=AddPostForm()
        blog = Blog.objects.all()
           
    context={'form':form}
    return render(request,'testapp/additem.html',context)
     

    # def BlogView(request):
    # form = AddPostForm()
    # # print(request)
    # if request.method == "POST":
    #     # print(request.POST['title'])
    #     form = AddPostForm(request.POST)
    #     if form.is_valid():
    #         title = form.cleaned_data['title']
    #         content = form.cleaned_data['content']

    #         blog = Blog.objects.create(title= title, content=content)
    #         blog.save()
    #         return HttpResponse('blog post created')
    # else:
    #     form=AddPostForm()
    #     blog = Blog.objects.all()
    #         # print(title , content)
    #     # data=request.POST
    #     # data['title']
    #     # data['content']
    #     # blog=Blog.objects.create(title=data['title'],content=data['content'])
    #     # blog.save()
    # print(blog)
    # context={'blogpost':blog , 'form' : form}
    # return render(request,'Home.html',context)

# def BlogDetail(request,num):
    
#     name="codinguy"
#     context={'number':num, 'name':name }
#     return render(request,'BlogDetail.html',context)
#     # return HttpResponse(f"hey you are looking at {num}") #f-string

# def BlogDetail(request,postid):
#     post = Blog.objects.get(id=postid)
#     # motaqeyere post ijad mikonim az dakhele model blog object hasho entekhab mikonim
#     # get mikonim query zadim
#     context={'post':post}
#     return render(request,'BlogDetail.html',context)
#     # return HttpResponse(f"hey you are looking at {num}") #f-string