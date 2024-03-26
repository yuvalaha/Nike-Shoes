from django.urls import path
from . import views

urlpatterns = [
    # GET http://localhost:8000/api/clothes
    path("clothes", views.get_clothes), 
    
    # GET http://localhost:8000/api/clothes/id
    path("clothes/<int:id>", views.get_cloth), 
    
    # GET http://localhost:8000/api/clothes/add
    path("clothes/add", views.add_cloth), 
    
    # GET http://localhost:8000/api/clothes/edit/id
    path("clothes/edit/<int:id>", views.update_cloth), 
    
    # GET http://localhost:8000/api/clothes/delete/id
    path("clothes/delete/<int:id>", views.delete_cloth), 
]
