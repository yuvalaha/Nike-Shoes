from django.db.models import Model, CharField, DecimalField, ForeignKey, RESTRICT
from django.forms import ModelForm, NumberInput, Select, TextInput
from django.core.validators import MinLengthValidator, MaxLengthValidator, MaxValueValidator, MinValueValidator
 
# Create your models here.


class TypeModel(Model):

    # First column id

    # Second Column
    name = CharField(max_length=25)

    # __str__ magic method: 
    def __str__(self):
        return self.name

    # Metadata:
    class Meta:
        db_table = "type"

    
# --------------------------------------------------------------------


class ClothingModel(Model):

    # First column id

    # Second Column Manufacture
    model = CharField(max_length=30, validators=[MinLengthValidator(2), MaxLengthValidator(30)])

    # Third Column Price
    price = DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0, "Price cant be negative"), MaxValueValidator(500)])

    # Fourth Column Type
    type = ForeignKey(TypeModel, on_delete=RESTRICT)


    # Metadata:
    class Meta:
        db_table = "clothes"
        
        
# --------------------------------------------------------------------       

# Clothing form model - describing gow to build a cloth form
class ClothingForm(ModelForm):

    class Meta:
        model = ClothingModel
        exclude = ["id"] # or field = ["manufacture", "price", "type"]

        widgets = {
        "model": TextInput(attrs = {"class": "form-control", "minlength": 2, "maxlength": 30}),  # attrs = HTML Attributes 
        "price": NumberInput(attrs = {"class": "form-control", "min": 0, "max": 500}),  
        "type": Select(attrs = {"class": "form-control"})
        }