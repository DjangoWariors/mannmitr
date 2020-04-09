from django.shortcuts import render
from . models import AboutFounder,AboutUs
from blogsite.models import Category
# Create your views here.
def about(request):
    ##### for categeory and sub Categeory #####
    cate= {}
    queryset = Category.objects.all()
    for id in queryset:
        
        cat = Category.objects.get(id=id.id)
        subcat=cat.subcategory_set.all()
        cate[id.category] = subcat
    about = AboutUs.objects.all()[:1]
    founders=AboutFounder.objects.all()[:2]
    
    return render(request,"aboutus.html",{'about': about,'founders':founders,'cate':cate })
