# Import forms and models 
from django import forms 
from .models import Product, Category 

class ProductForm(forms.ModelForm):
    class Meta:
        # Tell Django which model this form is based on
        model = Product
        # List only the fields you want the user to fill in
        # 'pk', 'id', and 'created_at' are excluded — Django handles those
        fields = ['name', 'price', 'stock', 'category']
        # widgets let you customise how each field renders in HTML
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Product name'}),
            'price': forms.NumberInput(attrs={'min': '0'}),
             'stock': forms.NumberInput(attrs={'class': 'form-control'}),
                     'category': forms.Select(attrs={'class': 'form-select'}),
    }

    def clean_price(self):
             price = self.cleaned_data.get('price')
             if price <= 0:
                 raise forms.ValidationError('Price must be greater than 0.')
             return price

# Add clean_stock method OUTSIDE Meta but INSIDE ProductForm:
    def clean_stock(self):
             stock = self.cleaned_data.get('stock')
             if stock < 0:
                 raise forms.ValidationError('Stock cannot be negative.')
             return stock


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            }
