from django import forms
from .models import HomeContact, Services, Contact
from ckeditor.widgets import CKEditorWidget

class AddServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['title', 'description', 'categories', 'tags', 'uploaded_file']
        widgets = {
            'description': CKEditorWidget(),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].required = False 

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['last_name'].required = False 
        
class HomeContactForm(forms.ModelForm):
    class Meta:
        model = HomeContact
        fields = '__all__'

   