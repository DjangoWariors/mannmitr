from django.urls import path

from . import views
 
urlpatterns = [ 
    
    path('' ,views.index, name="index"),
    path('search' ,views.search, name="search"),
    path('tab/<str:category>/' ,views.tab, name="tab"),
    path('expert/<int:pk>/' ,views.expert, name="expert"),
    path('expert-list' ,views.expert_list, name="expert_list"),
    path('posts/<int:pk>/',views.posts_detail, name= "posts_detail"),
    path('categeory/<int:Subcategory_id>/',views.subcate,name="subcate")
   
]
