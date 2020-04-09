from django.shortcuts import render,redirect,get_object_or_404,redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib import messages
from . models import Subcategory,Posts,Category,Expert
from subscribe.models import Subscribe
from sidebar.models import SidebarImage,SidebarTitle
from MediaPage.models import YouTubeLink

# Create your views here.

def index(request):
    ##### for categeory and sub Categeory #####
    cate= {}
    queryset = Category.objects.all()
    for id in queryset: 
        cat = Category.objects.get(id=id.id)
        subcat=cat.subcategory_set.all()
        cate[id.category] = subcat
    ##### categeory and sub Categeory #####
    slider = Posts.objects.order_by('-creation_date').filter(status__contains='P').filter(slider__contains='U')
    sliderl = Posts.objects.order_by('-creation_date').filter(status__contains='P').filter(slider__contains='L')
    up_slider = Posts.objects.order_by('-creation_date').filter(status__contains='P')
    sidebarimg = SidebarImage.objects.order_by('-creation_date')[:1]
    sidebrtitle = SidebarTitle.objects.order_by('-creation_date')[:1]
    YouTubeLin = YouTubeLink.objects.order_by('-creation_date')[:1]
    
    if request.method == "POST": 
        email = request.POST['email']
        Subscribe.objects.create(email = email)
    return render(request,'index.html',
        {'cate': cate, 'up_slider':up_slider, 'sidebarimg':sidebarimg,'sidebrtitle':sidebrtitle,'yt':YouTubeLin,'slider':slider,'sliderl':sliderl})

def posts_detail(request,pk):

    ##### for categeory and sub Categeory #####
    queryset = Category.objects.all()
    cate= {}
    for id in queryset:
        cat = Category.objects.get(id=id.id)
        subcat=cat.subcategory_set.all()
        cate[id.category] = subcat
    ##### categeory and sub Categeory #####
    post_data = get_object_or_404(Posts,pk=pk)
    slider =  Posts.objects.all()[:5]
    #########
    expert = post_data.expert_id
    expert = Expert.objects.get(id=expert)
    
    return render(request,'post1.html',{'cate': cate,'post_data':post_data,'slider':slider,'expert':expert})

def subcate(request,Subcategory_id):

    ##### for categeory and sub Categeory #####
    queryset = Category.objects.all()
    cate= {}
    for id in queryset:
        cat = Category.objects.get(id=id.id)
        subcat=cat.subcategory_set.all()
        cate[id.category] = subcat
    ##### categeory and sub Categeory #####
    
    #subcate=Posts.objects.filter(Subcategory=Subcategory_id)

    slider = Posts.objects.order_by('-creation_date').filter(status__contains='P').filter(slider__contains='U')
    sliderl = Posts.objects.order_by('-creation_date').filter(status__contains='P').filter(slider__contains='L')
    up_slider = Posts.objects.order_by('-creation_date').filter(status__contains='P')
    sidebarimg = SidebarImage.objects.order_by('-creation_date')[:1]
    sidebrtitle = SidebarTitle.objects.order_by('-creation_date')[:1]
    YouTubeLin = YouTubeLink.objects.order_by('-creation_date')[:1]
    
    if request.method == "POST": 
        email = request.POST['email']
        Subscribe.objects.create(email = email)
    return render(request,'subtab.html',
    {'cate': cate, 'up_slider':up_slider, 'sidebarimg':sidebarimg,'sidebrtitle':sidebrtitle,'yt':YouTubeLin,'slider':slider,'sliderl':sliderl})

def search(request):
    ##### for categeory and sub Categeory #####
    cate= {}
    queryset = Category.objects.all()
    for id in queryset: 
        cat = Category.objects.get(id=id.id)
        subcat=cat.subcategory_set.all()
        cate[id.category] = subcat
    ##### categeory and sub Categeory #####
    
    if request.method == "POST":
        ###### processing post data #######
        search = str(request.POST['search'])
    
    expert_list=Posts.objects.filter(expert__name__contains=search)
    if expert_list.count()==0:
        return render(request,'404.html')
   
    return render(request,'expert-list.html',{'cate':cate,  'expert_list':expert_list })



def expert(request,pk):
    ##### for categeory and sub Categeory #####
    cate= {}
    queryset = Category.objects.all()
    for id in queryset: 
        cat = Category.objects.get(id=id.id)
        subcat=cat.subcategory_set.all()
        cate[id.category] = subcat
    #############################
    expert = get_object_or_404(Expert,pk=pk)
    expert_all = Expert.objects.all()
    post_exp = Posts.objects.filter(expert__id = pk)
    paginator = Paginator(post_exp, 6) 

    page_number = request.GET.get('page')
    post_exp = paginator.get_page(page_number)
    slider = Posts.objects.all()[:5]
    YouTubeLin = YouTubeLink.objects.all()[:1]
    
    return render(request,'expert.html',{'cate':cate,'expert':expert, 'post_exp':post_exp,'slider':slider,'expert_all':expert_all,'YouTubeLink':YouTubeLin})

def expert_list(request):
    ##### for categeory and sub Categeory #####
    cate= {}
    queryset = Category.objects.all()
    for id in queryset: 
        cat = Category.objects.get(id=id.id)
        subcat=cat.subcategory_set.all()
        cate[id.category] = subcat
    ##############################
    expert_list=Expert.objects.all()
    return render(request,'expert-list.html',{'cate':cate, 'expert_list':expert_list})

def tab(request,category):
    ##### for categeory and sub Categeory #####
    cate= {}
    queryset = Category.objects.all()
    for id in queryset: 
        cat = Category.objects.get(id=id.id)
        subcat=cat.subcategory_set.all()
        cate[id.category] = subcat
    ##### categeory and sub Categeory #####
    categorys = Category.objects.get(category=category)
    
    up_slider = Posts.objects.order_by('-last_update').filter(status__contains='P')
    if request.method == "POST": 
        email = request.POST['email']
        Subscribe.objects.create(email = email)
    return render(request,'tab.html', {'cate': cate, 'up_slider':up_slider})



