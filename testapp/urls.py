# from django.contrib import admin
from testapp.models import Blog
from django.urls import path
from .views import Addpost, BlogView, BlogDetail



# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    # path('', BlogView), #BARAYE YE TABE EE
    path('',BlogView.as_view()),
    # path('<int:num>',BlogDetail),#faqat age adad bashe neshon mide
    # path('blog/<postid>',BlogDetail.as_view(),name='detail') 
    path('blog/<pk>',BlogDetail.as_view(),name='detail') ,
    # postid=primarykey
    path('additem',Addpost, name='additem')

   
]
