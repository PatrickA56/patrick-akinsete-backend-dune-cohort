# ToriloShop 🛍️

A simple Django project demonstrating the **MTV (Model-Template-View)** architecture with two apps: `products` and `users`.

---

## 📂 Project Structure

Today
hlp write  a readme.md for this : Set up a Django project called toriloshop:
• Create 2 apps: 'products' and 'users' — register both in INSTALLED_APPS.
• In products, create 3 views: home(), product_list(), about().
• Wire each to URLs: / → home, /products/ → product_list, /about/ → about.
• Each view returns an HttpResponse with meaningful, descriptive content.
• Run the server and confirm all 3 pages work correctly.
• Bonus: Add a custom 404 handler view
Here’s a clean and professional README.md you can use for your Django project setup. It explains the structure, steps, and usage clearly:

markdown
# ToriloShop 🛍️

A simple Django project demonstrating the **MTV (Model-Template-View)** architecture with two apps: `products` and `users`.

---

## 📂 Project Structure

toriloshop/
├── manage.py
├── toriloshop/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── products/
│   ├── views.py
│   ├── urls.py
│   └── ...
└── users/
├── views.py
├── urls.py
└── ...

Code

---

## ⚙️ Setup Instructions

1. **Create Django Project**
   ```bash
   django-admin startproject toriloshop
   cd toriloshop
Create Apps

bash
python manage.py startapp products
python manage.py startapp users
Register Apps in settings.py

python
INSTALLED_APPS = [
    ...,
    'products',
    'users',
]
Define Views in products/views.py

python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to ToriloShop Home!")

def product_list(request):
    return HttpResponse("Browse our list of amazing products.")

def about(request):
    return HttpResponse("About ToriloShop: Your trusted online store.")
Wire URLs in toriloshop/urls.py

python
from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('about/', views.about, name='about'),
]
Run Server

bash
python manage.py runserver
Visit:

/ → Home page

/products/ → Product list

/about/ → About page

🎁 Bonus: Custom 404 Handler
In toriloshop/urls.py:

python
from django.http import HttpResponseNotFound

def custom_404(request, exception):
    return HttpResponseNotFound("Oops! Page not found. Try again.")

handler404 = 'toriloshop.urls.custom_404'
✅ Verification
Ensure all three pages (/, /products/, /about/) return meaningful content.

Test an invalid URL to confirm the custom 404 handler works.

🚀 Next Steps
Add templates for better UI.

Connect models to a database.

Expand users app with authentication features.

Code

Would you like me to also include **sample screenshots of the pages** (home, products, about, and 404) so your README looks more visual and engaging?
write everything in  way i can just copy it
Here’s a ready‑to‑use README.md you can copy directly into your project folder:

markdown
# ToriloShop 🛍️

A simple Django project demonstrating the **MTV (Model-Template-View)** architecture with two apps: `products` and `users`.

---

## 📂 Project Structure

toriloshop/
├── manage.py
├── toriloshop/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── products/
│   ├── views.py
│   ├── urls.py
│   └── ...
└── users/
├── views.py
├── urls.py
└── ...



---

## ⚙️ Setup Instructions

1. **Create Django Project**
   ```bash
   django-admin startproject toriloshop
   cd toriloshop


2: Create Apps

bash
python manage.py startapp products
python manage.py startapp users



3: Register Apps in settings.py

python
INSTALLED_APPS = [
    ...,
    'products',
    'users',
]


Define Views in products/views.py


from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to ToriloShop Home!")

def product_list(request):
    return HttpResponse("Browse our list of amazing products.")

def about(request):
    return HttpResponse("About ToriloShop: Your trusted online store.")


Wire URLs in toriloshop/urls.py
from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('about/', views.about, name='about'),
]

# Bonus: Custom 404 handler
from django.http import HttpResponseNotFound

def custom_404(request, exception):
    return HttpResponseNotFound("Oops! Page not found. Try again.")

handler404 = 'toriloshop.urls.custom_404'


Run Server

python manage.py runserver


Visit:

/ → Home page

/products/ → Product list

/about/ → About page



<!-- MODULE 8 README -->

# ToriloShop Project

## 📖 Project Description
ToriloShop is a Django-based e-commerce learning project. In this module, the application was extended to include two core models:
- **Category**: Represents product categories (e.g., Electronics, Furniture, Provision).
- **Product**: Represents items sold in the shop, linked to a category.

This project demonstrates how to define models, run migrations, perform ORM operations, and manage data through both the Django shell and the admin panel.

---

## Features Implemented
### Models
- **Category**
  - `name` (CharField, max_length=200)
  - `description` (TextField, blank=True)

- **Product**
  - `name` (CharField, max_length=200)
  - `price` (DecimalField, max_digits=10, decimal_places=2)
  - `stock` (IntegerField)
  - `category` (ForeignKey → Category)
  - `created_at` (DateTimeField, auto_now_add=True)

### ORM Operations
- Added 3 categories: Electronics, Furniture, Provision.
- Added 6 products (2 per category).
- Queried:
  - All products
  - Products by category
  - Products with price > 5000
- Updated one product’s price.
- Deleted one product.
- Registered both models in Django admin.

---

## ⚙️ Setup Instructions
1. Clone the repository.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate 

   Install Django:

bash
pip install django
Run migrations:

bash
python manage.py makemigrations
python manage.py migrate
Create a superuser:

bash
python manage.py createsuperuser
Start the server:

bash
python manage.py runserver
Access the admin panel at http://127.0.0.1:8000/admin.

🖼️ Screenshots
All screenshots are stored in the screenshots/ folder.

📂 Repository Structure
Code
toriloshop/
├── products/
│   ├── migrations/
│   ├── models.py
│   ├── admin.py
│   └── ...
├── screenshots/
│   ├── 03_shell_all_products.png
│   ├── 04_shell_products_by_category.png
│   ├── 05_shell_products_price_gt_5000.png
│   ├── 06_shell_update_product.png
│   ├── 07_shell_delete_product.png
│   └── 08_admin_panel.png
├── manage.py
└── README.md