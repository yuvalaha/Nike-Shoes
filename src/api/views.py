from django.shortcuts import render
from .models import ClothSerializer
from clothing.models import ClothingModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Get all clothes
@api_view(["GET"])
def get_clothes(request): 
    try:
        
        # Get all clothes
        clothes = ClothingModel.objects.all()
        
        # Create a serializer for converting into json 
        serializer = ClothSerializer(clothes, many = True) # many=True --> convert into list
        
        # Return back the serialized json
        return Response(serializer.data)
    
    except Exception as err:
        json = { "error": str(err) }
        return Response(json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# Get one cloth       
@api_view(["GET"])
def get_cloth(request, id): 
    try:
        
        # Get one cloth
        cloth = ClothingModel.objects.get(pk = id)
        
        # Create a serializer for converting into json 
        serializer = ClothSerializer(cloth) 
        
        # Return back the serialized json
        return Response(serializer.data)
    
    except ClothingModel.DoesNotExist:
        json = { "error": f"id {id} not found" }
        return Response(json, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as err:
        json = { "error": str(err) }
        return Response(json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
# Add cloth 
@api_view(["POST"])
def add_cloth(request): 
    
    try:
        # Get the given cloth for adding
        cloth = request.data
        
        # Create a serializer for converting into json 
        serializer = ClothSerializer(data=cloth) 
        
        # Validation
        if not serializer.is_valid():
            json = { "error": serializer.errors }
            return Response(json, status=status.HTTP_400_BAD_REQUEST)
        
        # Save to database
        serializer.save()
        
        # Take the added cloth including the cloth id
        added_cloth = serializer.data
        
        # Return back the serialized json
        return Response(added_cloth, status=status.HTTP_201_CREATED)
        
    except Exception as err:
        json = { "error": str(err) }
        return Response(json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    
# Update cloth 
@api_view(["PUT"])
def update_cloth(request, id): 
    try:
        
        # Check if cloth exist
        exist = ClothingModel.objects.filter(id=id).exists()
        if not exist:
            json = {"error": f"id {id} not found"}
            return Response(json, status=status.HTTP_404_NOT_FOUND)
        
        
        # Get the given cloth for adding
        cloth = request.data
        
        # Create serializer for saving cloth
        serializer = ClothSerializer(data = cloth, instance=ClothingModel(pk=id))
        
        # Validation
        if not serializer.is_valid():
            json = {"error": serializer.errors}
            return Response(json, status=status.HTTP_400_BAD_REQUEST)
        
        # Save to database
        serializer.save()
        
        # Return the updated cloth
        return Response(serializer.data)
    
    except ClothingModel.DoesNotExist:
        json = {"error": f"id {id} not found"}
        return Response(json, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as err:
        json = {"error": str(err)}
        return Response(json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# Delete cloth 
@api_view(["DELETE"])
def delete_cloth(request, id): 
    
    try: 
        
        # Check if cloth exist
        exist = ClothingModel.objects.filter(id=id).exists()
        if not exist:
            json = {"error": f"id {id} not found"}
            return Response(json, status=status.HTTP_404_NOT_FOUND)
        
        
        # Create dummy cloth for delete
        dummy_cloth = ClothingModel(pk=id)
        
        # Delete the cloth from the database
        dummy_cloth.delete()
        
        # Response back nothing
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    except ClothingModel.DoesNotExist:
        json = {"error": f"id {id} not found"}
        return Response(json, status=status.HTTP_404_NOT_FOUND)
    except Exception as err:
        json = {"error": str(err)}
        return Response(json, status=status.HTTP_500_INTERNAL_SERVER_ERROR)