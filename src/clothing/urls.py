from django.urls import path
from . import views

urlpatterns = [
# http://localhost:8000/clothing/
path('', views.list,  name="items"),

# http://localhost:8000/clothing/details/(id)
path('details/<int:id>', views.details,  name="details"),

# http://localhost:8000/clothing/new
path('new', views.insert,  name="insert"),

# http://localhost:8000/clothing/edit/..
path('edit/<int:id>', views.edit,  name="edit"),

# http://localhost:8000/clothing/delete/..
path('delete/<int:id>', views.delete,  name="delete"),
]

