from django.urls import path

from . import views
 
urlpatterns = [ 
    
    path('hi/' ,views.index2, name="index2"),
    path('hi/abouthn/' ,views.abouthn, name="abouthn"),
    #path('search' ,views.search, name="search"),
    #path('hindi' ,views.hindi, name="hindi"),
    path('hi/<str:category>/' ,views.categeory, name="categeory"),
    path('hi/expert/<int:pk>/' ,views.experthn, name="experthn"),
    #path('expert-list' ,views.expert_list, name="expert_list"),
    path('hi/posts_hindi/<int:pk>/',views.posts_hindi, name= "posts_hindi"),
    path('hi/subcategeory<int:Subcategory_id>/',views.subcatehn,name="subcatehn")

]
