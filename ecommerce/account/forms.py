from django import forms
from django.contrib.auth.hashers import make_password

from .models import *
class _customers(forms.ModelForm):
    first_name = forms.CharField(widget=(forms.TextInput(attrs={'class':'form-control form-control-lg'})),required=False)
    last_name = forms.CharField(widget=(forms.TextInput(attrs={'class':'form-control form-control-lg'})),required=False)
    email = forms.EmailField(widget=(forms.EmailInput(attrs={'class':'form-control form-control-lg'})))
    username = forms.CharField(widget=(forms.TextInput(attrs={'class':'form-control form-control-lg'})),required=False)
    image = forms.FileField(widget=(forms.FileInput(attrs={'class':'js-file-attach form-attachment-btn-label','id':'avatarUploader',' data-hs-file-attach-options':'{"textTarget": "#avatarImg","mode": "image","targetAttr": "src","resetTarget": ".js-file-attach-reset-img","resetImg": "../assets/img/160x160/img1.jpg","allowTypes": [".png", ".jpeg", ".jpg"]}'})),required=False)
    password = forms.PasswordInput()
    phone_number = forms.CharField(widget=(forms.TextInput(attrs={'class':'js-input-mask form-control','data-hs-mask-options':'{"mask": "0000000000"}'})))
    class Meta:
        model = customers
        fields = ('first_name','last_name','email','username','image','password','phone_number',)

    def clean_password(self,*args,**kwargs):
        password = make_password(self.cleaned_data.get('password'))
        if password == None or len(password) < 8:
            raise forms.ValidationError('حداقل طول پسورد 8 کارکتر می باشد')
        else:
            return password
    def clean_username(self,*args,**kwargs):
        username = self.cleaned_data.get('email')
        if username == None:
            raise forms.ValidationError('ایمیل نمی تواند خالی باشد')
        else:
            return username
class _state(forms.ModelForm):
    title = forms.CharField(error_messages={'required':'لطفا یک عنوان را انتخاب کنید','max_length':'حداکثر طول استان 50 کارکتر می باشد'},widget=(forms.TextInput(attrs={'class':'form-control'})))
    class Meta:
        model = state
        fields = ('title',)
class _city(forms.ModelForm):
    state = forms.ModelChoiceField(queryset=state.objects.all(),error_messages={'required':'لطفا یک استان را انتخاب کنید'},widget=(forms.Select(attrs={'class':'form-control'})))
    title = forms.CharField(error_messages={'required':'لطفا یک شهر را انتخاب کنید','max_length':'حداکثر طول شهر 50 کارکتر می باشد'},widget=(forms.TextInput(attrs={'class':'form-control'})))
    class Meta:
        model = city
        fields = ('state','title')
class _address(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=customers.objects.all())
    title = forms.CharField(error_messages={'required':'لطفا یک عنوان بنویسید','max_length':'حداکثر طول عنوان 50 کارکتر می باشد'},widget=(forms.TextInput(attrs={'class':'form-control'})))
    city = forms.ModelChoiceField(queryset=city.objects.all(),error_messages={'required':'لطفا یک شهر را انتخاب کنید'},widget=(forms.Select(attrs={'class':'form-control'})))
    description = forms.CharField(error_messages={'required':'لطفا توضیحات آدرس خود را بنویسید','max_length':'حداکثر طول توضیحات آدرس 500 کارکتر می باشد'},widget=(forms.Textarea(attrs={'class':'form-control'})))
    zipcode = forms.CharField(error_messages={'required':'لطفا کد پستی خود را وارد کنید','max_length':'حداکثر طول کد پستی 10 کارکتر می باشد'},widget=(forms.NumberInput(attrs={'class':'form-control'})))
    class Meta:
        model = address
        fields = ('user','title','city','description','zipcode')
