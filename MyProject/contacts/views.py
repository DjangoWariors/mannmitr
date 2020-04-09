from django.shortcuts import render,redirect
from blogsite.models import Category
from contacts.models import contact,internship
from .forms import contactsForm,internshipForm
# Create your views here.

def contacts(request):
        ##### for categeory and sub Categeory #####
    queryset = Category.objects.all()
    cate= {}
    for id in queryset:
        cat = Category.objects.get(id=id.id)
        subcat=cat.subcategory_set.all()
        cate[id.category] = subcat
    ##### categeory and sub Categeory #####
    form = contactsForm()
    if request.method == "POST":  
        form = contactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
        else:  
            form = contactsForm()
        return render(request, 'contactus.html',{'form':form})
    return render(request,'contactus.html',{'cate':cate,'form':form})



def internships(request):
        ##### for categeory and sub Categeory #####
    queryset = Category.objects.all()
    cate= {}
    for id in queryset:
        cat = Category.objects.get(id=id.id)
        subcat=cat.subcategory_set.all()
        cate[id.category] = subcat
    ##### categeory and sub Categeory #####
    form = internshipForm()
    if request.method == "POST":  
        form = internshipForm(request.POST,request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('index')  
        else:  
            form = internshipForm()  
        return render(request, 'intern.html',{'form':form})
    return render(request,'intern.html',{'cate':cate,'form':form})
    

