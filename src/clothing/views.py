
from django.http import Http404
from django.shortcuts import redirect, render
from .models import ClothingModel, ClothingForm
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.


# Items view:
def list(request):
    items = ClothingModel.objects.all()
    context = {"active": "items", "items": items}
    return render(request, "items.html", context)


# Details view:
def details(request, id):
    try:
        item = ClothingModel.objects.get(pk=id)
        context = {"item": item}
        return render(request, "details.html", context)
    except ClothingModel.DoesNotExist:
        raise Http404()

# Insert view:
@login_required(login_url="login")
def insert(request):
    if request.method == "GET":
        context = {"active": "insert", "form": ClothingForm()}
        return render(request, "insert.html", context)
    form = ClothingForm(request.POST)
    # Check if the form is valid
    if not form.is_valid():
       context = {"form":form, "active": "insert"}
       return render(request, "insert.html", context)     
    form.save()
   
    return redirect("items")

# Update view:
@login_required(login_url="login")
def edit(request, id):
    try:
        if request.method == "GET":
            cloth = ClothingModel.objects.get(pk=id) # Get the cloth we want to edit 
            context = {"form" : ClothingForm(instance = cloth)}
            return render(request, "edit.html", context)
        dummy_cloth = ClothingModel(pk=id)
        form = ClothingForm(request.POST, instance=dummy_cloth)
        if not form.is_valid():
            context = {"form" : form}
            return render(request, "edit.html", context)
        form.save()
        return(redirect("items"))
    except ClothingModel.DoesNotExist:
        raise Http404()
    
# Delete view:
@permission_required(perm="is_superuser", login_url="login")
def delete(request, id):
    try:
        dummy_cloth = ClothingModel(pk = id)
        dummy_cloth.delete()
        return redirect("items") 
    except ClothingModel.DoesNotExist:
        raise Http404()
        