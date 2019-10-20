from django import forms
from .models import Book, User

# -------------------------------------------------------------
class RawSearchForm(forms.Form):
    #categorys = Book.objects.exclude(category__isnull=True).all().distinct()
    categorys = Book.objects.values("category").distinct()    

    #category = forms.ChoiceField(required=False,
            #choices=[["", "-- select an option --"]] + [(o, str(o)) for o in categorys])
    category = forms.ChoiceField(required=False,
            choices=[["", "-- select an option --"]] + [(o, str(o)) for o in categorys])
    available = forms.ChoiceField(required=False,
            choices=[["", "-- select an option --"]] + [(True, 'True'),(False, 'False')])
    keyword = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={"placeholder" : "Keywords"}))

    """def clean_keyword(self):
            category = self.cleaned_data.get("category")
            available = self.cleaned_data.get("available")
            keyword = self.cleaned_data.get("keyword")
    
            if "aaa" in keyword:
                    raise forms.ValidationError('One of fields is required')
            
            return self.cleaned_data"""

