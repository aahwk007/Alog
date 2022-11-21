from .models import Todo
from django.forms import ModelForm

class T_form(ModelForm):
    class Meta:
        model = Todo
        #fields = ['title','description','tag','status','due_date']
        fields ='__all__'
