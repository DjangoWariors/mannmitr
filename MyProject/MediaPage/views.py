from django.shortcuts import render,redirect
from . models import MediaCoverage,YouTubeLink
from blogsite.models import Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def media(request):
    ##### for categeory and sub Categeory #####
    queryset = Category.objects.all()
    cate= {}
    for id in queryset:
        cat = Category.objects.get(id=id.id)
        subcat=cat.subcategory_set.all()
        cate[id.category] = subcat
    ##### categeory and sub Categeory #####
    
    post_exp = queryset = MediaCoverage.objects.all()
    paginator = Paginator(post_exp,6) 
    page_number = request.GET.get('page')
    post_exp = paginator.get_page(page_number)
    return render(request,'mediaCoverage.html',{'queryset':post_exp,'cate':cate})

