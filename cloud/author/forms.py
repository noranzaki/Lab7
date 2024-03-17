from django import forms
from .models import Author

class AuthorModelForm(forms.ModelForm):
     class Meta:
        model= Author
        
        fields='__all__'


     def clean_name(self):
       name = self.cleaned_data['name']

       if Author.objects.filter(name=name).exists() and self.instance.name != name:
        raise forms.ValidationError("Name already exists")

       if len(name) < 2:
        raise forms.ValidationError("Name must be at least 2 characters")

       return name
        
      

