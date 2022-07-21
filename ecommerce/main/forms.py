from  django import forms
from .models import *
#for import lib
class logo_site_(forms.ModelForm):
    image = forms.ImageField(error_messages={'required' : 'یک عکس انتخاب کنید'},widget=(forms.FileInput(attrs={'class': 'form-control'})),required=False)
    title = forms.CharField(error_messages={'required' : 'عنوان اجباری هست' , 'max_length' : 'حداکثر طول 150 کارکتر می باشد'},widget=(forms.TextInput(attrs={'class': 'form-control'})))
    class Meta:
        model = logo_site
        fields = ('image','title')
class icon_site_(forms.ModelForm):
    image = forms.ImageField(error_messages={'required' : 'یک عکس انتخاب کنید'},widget=(forms.FileInput(attrs={'class': 'form-control'})))
    class Meta:
        model = icon_site
        fields = ('image',)