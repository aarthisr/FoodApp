from django import forms
from .models import Item

class Item_Form(forms.ModelForm):
    class Meta:
        model = Item
        fields= ['item_name', 'item_desc', 'item_price', 'item_image']