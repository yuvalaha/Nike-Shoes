from django.test import TestCase, SimpleTestCase, Client
from django.urls import resolve, reverse

from clothing.models import TypeModel, ClothingModel
from .views import details, list, insert, delete, edit 
from http import HTTPStatus
from django.contrib.auth.models import User

# Test Urls

# Test urls integrity
class TestUrls(SimpleTestCase):
    
    # Test urls integrity:
    def test_urls(self):
        url = reverse("items")
        view_function = resolve(url).func
        self.assertEqual(view_function, list)
        
        url = reverse("details", args=[1])
        view_function = resolve(url).func
        self.assertEqual(view_function, details)
        
        url = reverse("insert")
        view_function = resolve(url).func
        self.assertEqual(view_function, insert)
        
        url = reverse("edit", args=[1])
        view_function = resolve(url).func
        self.assertEqual(view_function, edit)
        
        url = reverse("delete", args=[1])
        view_function = resolve(url).func
        self.assertEqual(view_function, delete)
        
        
class TestViews(TestCase):
    
    # Do before each test: 
    def setUp(self):
        self.client = Client()
        shirts = TypeModel.objects.create(name="Shirts")
        ClothingModel.objects.create(model="t_shirt", price=30, type=shirts)
        ClothingModel.objects.create(model="long_shirt", price=46, type=shirts)
        username = "testing@gmail.com"
        password = "testing1234"
        User.objects.create_superuser(username=username, password=password)
        self.client.login(username=username, password=password)
        
        
        
    
    # Test list view:
    def test_list(self):
        url = reverse("items")
        response = self.client.get(url) # Url
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "items.html")
        self.assertContains(response, "t_shirt")
        self.assertContains(response, "long_shirt")
    
    
    # Test details view:
    def test_details(self):
        url = reverse("details", args=[1])
        response = self.client.get(url)  
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response,"details.html")
        self.assertContains(response, "t_shirt")
    
    
    # Test insert- get view:
    def test_insert_get(self):
        url = reverse("insert")
        response = self.client.get(url)  
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response,"insert.html")
        self.assertContains(response, "<form")
        self.assertContains(response, "</form>")
        
    # Test insert- post view:
    def test_insert_post(self):
        url = reverse("insert") 
        form_data = {"model":"sweatshirt", "price":125, "type": 1}
        response = self.client.post(url, data=form_data, follow=True) # follow = True --> tell the client to follow all redirection until final result.   
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response,"items.html")
        existInDB = ClothingModel.objects.filter(model="sweatshirt").exists()
        self.assertTrue(existInDB)
        self.assertContains(response, "sweatshirt")
        
     # Test edit- get view:
    def test_edit_get(self):
        url = reverse("edit", args=[1])
        response = self.client.get(url)  
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response,"edit.html")
        self.assertContains(response, "<form")
        self.assertContains(response, "</form>")
        
    
   # Test edit- post view:
    def test_edit_post(self):
        url = reverse("edit", args=[1]) 
        form_data = {"model":"running shirt", "price":75, "type": 1}
        response = self.client.post(url, data=form_data, follow=True) # follow = True --> tell the client to follow all redirection until final result.   
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response,"items.html")
        existInDB = ClothingModel.objects.filter(model="running shirt").exists()
        self.assertTrue(existInDB)
        self.assertContains(response, "running shirt") 
        
        
    # Test delete view:
    def test_delete(self):
        url = reverse("delete", args=[1]) 
        response = self.client.post(url, follow=True) # follow = True --> tell the client to follow all redirection until final result.   
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response,"items.html")
        existInDB = ClothingModel.objects.filter(id=1).exists()
        self.assertFalse(existInDB)   