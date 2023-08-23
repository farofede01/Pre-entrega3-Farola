from django import forms

class medicoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    dni = forms.IntegerField()
    email = forms.EmailField()

class hospitalForm (forms.Form):
    nombre = forms.CharField(max_length=50)
    num_telefono = forms.IntegerField
    direccion = forms.CharField(max_length=50)
    email = forms.EmailField()

class obrasocialForm (forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()


