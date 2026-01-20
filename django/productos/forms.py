from django import forms
from . import models


class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = ["nombre", "stock", "puntaje", "categoria"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "stock": forms.NumberInput(attrs={"class": "form-control"}),
            "puntaje": forms.NumberInput(attrs={"class": "form-control"}),
            "categoria": forms.Select(attrs={"class": "form-select"}),
        }
