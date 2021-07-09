from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    #be chia dasyresi dashte bashim
    # fields=['title','content']
    fieldsets = [
        ('title',              {'fields': ['title']}),
        ('content information',{'fields': ['content', 'author']}),
        ('image', {'fields':['image']}),
    ]

    list_display=['title' ,'content', 'date']
    search_fields=['title' , 'content']
    

admin.site.register(Blog , BlogAdmin)