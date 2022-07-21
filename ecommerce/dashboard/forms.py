from django import forms
from django.utils.text import slugify
from tinymce.widgets import TinyMCE
from gallery.models import images
from dashboard.models import *
from main.models import *


class _page_generate_(forms.ModelForm):
    title = forms.CharField(error_messages = {"max_length": "طول عنوان نباید از 250 کارکتر بیشتر شود","required" : "عنوان نمی تواند خالی باشد"},widget=(forms.TextInput(attrs={'class':'form-control' , "style":"width: 50%"})))
    url = forms.SlugField(allow_unicode=True,error_messages = {"max_length": "طول عنوان نباید از 250 کارکتر بیشتر شود","required" : "عنوان نمی تواند خالی باشد"},widget=(forms.TextInput(attrs={'class':'form-control' , "style":"width: 50%"})))
    description_seo = forms.CharField(error_messages={"max_length": "طول توضیحات نباید از 450 کارکتر بیشتر شود",
                                                   "required": "توضیحات نمی تواند خالی باشد"},
                                   widget=(forms.Textarea(attrs={'class': 'form-control', "style": "width: 50%"})))
    keywords_seo = forms.CharField(error_messages = {"max_length": "طول عنوان نباید از 150 کارکتر بیشتر شود","required" : "عنوان نمی تواند خالی باشد"},widget=(forms.TextInput(attrs={'class':'form-control' , "style":"width: 50%"})))
    tags_seo = forms.CharField(error_messages = {"max_length": "طول عنوان نباید از 150 کارکتر بیشتر شود","required" : "عنوان نمی تواند خالی باشد"},widget=(forms.TextInput(attrs={'class':'form-control' , "style":"width: 50%"})))
    image = forms.ModelChoiceField(queryset=images.objects.all(),
                                   widget=(forms.Select(attrs={'class': 'form-control none'})))
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30 , 'id' : 'tinymce'}))
    class Meta:
        model = page_generator
        fields = ('title','url' ,'description_seo' ,'tags_seo','keywords_seo' , 'image' , 'text')
class _main_footer(forms.ModelForm):
    title = forms.CharField(error_messages = {"max_length": "طول عنوان نباید از 250 کارکتر بیشتر شود","required" : "عنوان نمی تواند خالی باشد"},widget=(forms.TextInput(attrs={'class':'form-control' , "style":"width: 50%"})))
    class Meta:
        model = main_footer
        fields = ('title',)
class _sub_footer(forms.ModelForm):
    main = forms.ModelChoiceField(error_messages = {"required" : "حداقل یک گزینه را انتخاب نمایید"},queryset=main_footer.objects.all(),widget=(forms.Select(attrs={'class': 'form-control'})))
    title = forms.CharField(error_messages = {"max_length": "طول عنوان نباید از 250 کارکتر بیشتر شود","required" : "عنوان نمی تواند خالی باشد"},widget=(forms.TextInput(attrs={'class':'form-control' , "style":"width: 50%"})))
    link = forms.CharField(error_messages = {"max_length": "طول لینک نباید از 450 کارکتر بیشتر شود","required" : "عنوان نمی تواند خالی باشد"},widget=(forms.TextInput(attrs={'class':'form-control' , "style":"width: 50%"})))
    class Meta:
        model = sub_footer
        fields = ('main','title','link')
class _navbar_process(forms.ModelForm):
    title = forms.CharField(error_messages={"max_length": "طول عنوان نباید از 30 کارکتر بیشتر شود","required": "عنوان نمی تواند خالی باشد"},widget=(forms.TextInput(attrs={'class': 'form-control', "style": "width: 50%"})))
    image = forms.ModelChoiceField(error_messages = {"required" : "حداقل یک عکس را انتخاب نمایید"},queryset=images.objects.all(),widget=(forms.Select(attrs={'class': 'form-control none'})))
    descriptions = forms.CharField(error_messages={"max_length": "طول توضیحات نباید از 30 کارکتر بیشتر شود","required": "عنوان نمی تواند خالی باشد"},widget=(forms.TextInput(attrs={'class': 'form-control', "style": "width: 50%"})))
    class Meta:
        model = navbar_process
        fields = ('title','image','descriptions')
class _swiper(forms.ModelForm):
    title = forms.CharField(error_messages={"max_length": "طول عنوان نباید از 50 کارکتر بیشتر شود","required": "عنوان نمی تواند خالی باشد"},widget=(forms.TextInput(attrs={'class': 'form-control', "style": "width: 50%"})))
    image = forms.ModelChoiceField(error_messages = {"required" : "حداقل یک عکس را انتخاب نمایید"},queryset=images.objects.all(),widget=(forms.Select(attrs={'class': 'form-control none'})))
    descriptions = forms.CharField(error_messages={"max_length": "طول عنوان نباید از 100 کارکتر بیشتر شود","required": "عنوان نمی تواند خالی باشد"},widget=(forms.TextInput(attrs={'class': 'form-control', "style": "width: 50%"})))
    link = forms.CharField(error_messages={"max_length": "طول لینک نباید از 100 کارکتر بیشتر شود","required": "عنوان نمی تواند خالی باشد"},widget=(forms.TextInput(attrs={'class': 'form-control', "style": "width: 50%"})))
    class Meta:
        model = swiper
        fields = ('title','image','descriptions' , 'link')
class _blog_(forms.ModelForm):
    title = forms.CharField(error_messages = {"max_length": "طول عنوان نباید از 250 کارکتر بیشتر شود","required" : "عنوان نمی تواند خالی باشد"},widget=(forms.TextInput(attrs={'class':'form-control' , "style":"width: 50%"})))
    category = forms.ModelChoiceField(queryset=category_blog.objects.all(),error_messages={'required' : 'یک دسته بندی انتخاب کنید'},widget=(forms.Select(attrs={'class':'form-control'})))
    url = forms.SlugField(allow_unicode=True,error_messages = {"max_length": "طول عنوان نباید از 250 کارکتر بیشتر شود","required" : "عنوان نمی تواند خالی باشد"},widget=(forms.TextInput(attrs={'class':'form-control' , "style":"width: 50%"})))
    description_seo = forms.CharField(error_messages={"max_length": "طول توضیحات نباید از 450 کارکتر بیشتر شود",
                                                   "required": "توضیحات نمی تواند خالی باشد"},
                                   widget=(forms.Textarea(attrs={'class': 'form-control', "style": "width: 50%"})))
    keywords_seo = forms.CharField(error_messages = {"max_length": "طول عنوان نباید از 150 کارکتر بیشتر شود","required" : "عنوان نمی تواند خالی باشد"},widget=(forms.TextInput(attrs={'class':'form-control' , "style":"width: 50%"})))
    tags_seo = forms.CharField(error_messages = {"max_length": "طول عنوان نباید از 150 کارکتر بیشتر شود","required" : "عنوان نمی تواند خالی باشد"},widget=(forms.TextInput(attrs={'class':'form-control' , "style":"width: 50%"})))
    image = forms.ModelChoiceField(queryset=images.objects.all(),
                                   widget=(forms.Select(attrs={'class': 'form-control none'})))
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30 , 'id' : 'tinymce'}))
    class Meta:
        model = blogs
        fields = ('title','category','url' ,'description_seo' ,'tags_seo','keywords_seo' , 'image' , 'text')


class _blog_Category(forms.ModelForm):
    title = forms.CharField(error_messages={"max_length": "طول عنوان نباید از 250 کارکتر بیشتر شود",
                                            "required": "عنوان نمی تواند خالی باشد"},
                            widget=(forms.TextInput(attrs={'class': 'form-control', "style": "width: 50%"})))
    class Meta:
        model = category_blog
        fields = ('title',)