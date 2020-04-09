from django.shortcuts import render,redirect,get_object_or_404,redirect
from django.core.paginator import Paginator
from . models import HindiSubcategory,HindiPosts,HindiCategory
from blogsite.models import Expert
from About_us.models import AboutUs,AboutFounder
from sidebar.models import SidebarImage,SidebarTitle
from subscribe.models import Subscribe
from MediaPage.models import YouTubeLink
# Create your views here.
def index2(request):
    
    cate= {}
    queryset = HindiCategory.objects.all()
    for id in queryset: 
        cat = HindiCategory.objects.get(id=id.id)
        subcat=cat.hindisubcategory_set.all()
        cate[id.category] = subcat
    
    up_slider = HindiPosts.objects.order_by('-last_update').filter(status__contains='P')
    slider = HindiPosts.objects.order_by('-creation_date').filter(status__contains='P').filter(slider__contains='U')
    lslider = HindiPosts.objects.order_by('-creation_date').filter(status__contains='P').filter(slider__contains='L')
    sidebarimg = SidebarImage.objects.order_by('-creation_date')[:1]
    sidebrtitle = SidebarTitle.objects.order_by('-creation_date')[:1]
    YouTubeLin = YouTubeLink.objects.order_by('-creation_date')[:1]
    
    if request.method == "POST": 
        email = request.POST['email']
        Subscribe.objects.create(email = email)
    return render(request,'index2.html', 
        {'cate': cate, 'up_slider':up_slider, 'sidebarimg':sidebarimg,'sidebrtitle':sidebrtitle,'yt':YouTubeLin,'slider':slider,'lslider':lslider})

def abouthn(request):
    
    cate= {}
    queryset = HindiCategory.objects.all()
    for id in queryset:
        
        cat = HindiCategory.objects.get(id=id.id)
        subcat=cat.hindisubcategory_set.all()
        cate[id.category] = subcat
    about = AboutUs.objects.filter(language__contains='IN')[:1]
    founders=AboutFounder.objects.filter(language__contains='IN')[:2]
    
    return render(request,"aboutushn.html",{'about': about,'founders':founders,'cate':cate })

def categeory(request,category):
    
    cate= {}
    queryset = HindiCategory.objects.all()
    for id in queryset: 
        cat = HindiCategory.objects.get(id=id.id)
        subcat=cat.hindisubcategory_set.all()
        cate[id.category] = subcat
    
    #categorys = HindiCategory.objects.get(category=category)
    
    up_slider = HindiPosts.objects.order_by('-creation_date').filter(status__contains='P')
    if request.method == "POST": 
        email = request.POST['email']
        Subscribe.objects.create(email = email)

    return render(request,'tabhn.html', {'cate': cate, 'up_slider':up_slider})

def subcatehn(request,Subcategory_id):

    queryset = HindiCategory.objects.all()
    cate= {}
    for id in queryset:
        cat = HindiCategory.objects.get(id=id.id)
        subcat=cat.Hindisubcategory_set.all()
        cate[id.category] = subcat
    
    #subcate = get_object_or_404(Posts,Subcategory=Subcategory_id)
    
    subcate=HindiPosts.objects.filter(Subcategory=Subcategory_id)
    print(subcate.count())

    return render(request,'subcathn.html',{'cate':cate, 'subcate':subcate})


def posts_hindi(request,pk):

    queryset = HindiCategory.objects.all()
    cate= {}
    for id in queryset:
        cat = HindiCategory.objects.get(id=id.id)
        subcat=cat.hindisubcategory_set.all()
        cate[id.category] = subcat
    
    post_data = get_object_or_404(HindiPosts,pk=pk)
    print(post_data)
    slider =  HindiPosts.objects.all()[:5]
    #########
    expert = post_data.expert_id
    expert = Expert.objects.get(id=expert)
    
    return render(request,'posthn1.html',{'cate': cate,'post_data':post_data,'slider':slider,'expert':expert})

def experthn(request,pk):
    
    cate= {}
    queryset = HindiCategory.objects.all()
    for id in queryset: 
        cat = HindiCategory.objects.get(id=id.id)
        subcat=cat.hindisubcategory_set.all()
        cate[id.category] = subcat
    
    expert = get_object_or_404(Expert,pk=pk)
    expert_all = Expert.objects.all()
    post_exp = HindiPosts.objects.filter(expert__id = pk)
    paginator = Paginator(post_exp, 6) 

    page_number = request.GET.get('page')
    post_exp = paginator.get_page(page_number)
    slider = HindiPosts.objects.all()[:5]
    YouTubeLin = YouTubeLink.objects.all()[:1]
    
    return render(request,'experthn.html',{'cate':cate,'expert':expert, 'post_exp':post_exp,'slider':slider,'expert_all':expert_all,'YouTubeLink':YouTubeLin})


