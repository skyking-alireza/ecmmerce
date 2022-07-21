from django import forms
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from tinymce.widgets import TinyMCE
from product.models import *
from gallery.models import images
from jalali_date.fields import JalaliDateTimeField , SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime


class main_category(forms.ModelForm):
    name = forms.CharField(error_messages = {"max_length": "طول عنوان نباید از 150 کارکتر بیشتر شود","required" : "عنوان نمی تواند خالی باشد"},
                           widget=(forms.TextInput(attrs={'class':'form-control' , "style":"width: 50%"})))
    descriptions = forms.CharField(error_messages = {"max_length": "طول توضیحات نباید از 450 کارکتر بیشتر شود","required" : "توضیحات نمی تواند خالی باشد"},
                                   widget=(forms.Textarea(attrs={'class': 'form-control', "style": "width: 50%"})))
    keywords = forms.CharField(error_messages={"max_length": "طول کلمات کلیدی نباید از 150 کارکتر بیشتر شود",
                                           "required": "کلمات کلیدی نمی تواند خالی باشد"},
                           widget=(forms.TextInput(attrs={'class': 'form-control', "style": "width: 50%"})))
    tags = forms.CharField(error_messages={"max_length": "طول تگ ها نباید از 150 کارکتر بیشتر شود",
                                               "required": "تگ ها نمی تواند خالی باشد"},
                               widget=(forms.TextInput(attrs={'class': 'form-control', "style": "width: 50%"})))
    class Meta:
        model = maincategory
        fields = ('name', 'descriptions' , 'keywords' , 'tags')
class sub_category(forms.ModelForm):
    category = forms.ModelChoiceField(error_messages={"required": "لطفا یک دسته بندی را انتخاب کنید"},queryset=maincategory.objects.all(),widget=(forms.Select(attrs={'class': 'form-control'})))
    name = forms.CharField(error_messages = {"max_length": "طول عنوان نباید از 150 کارکتر بیشتر شود","required" : "عنوان نمی تواند خالی باشد"},
                           widget=(forms.TextInput(attrs={'class':'form-control' })))
    showindexpage = forms.BooleanField(widget=(forms.CheckboxInput(attrs={'id': 'switchmain', "class": "form-check-input"})) , required=False)
    image = forms.ModelChoiceField(queryset=images.objects.all() , widget=(forms.Select(attrs={'class' : 'form-control none'})))
    descriptions = forms.CharField(error_messages = {"max_length": "طول توضیحات نباید از 450 کارکتر بیشتر شود","required" : "توضیحات نمی تواند خالی باشد"},
                                   widget=(forms.Textarea(attrs={'class': 'form-control'})))
    keywords = forms.CharField(error_messages={"max_length": "طول کلمات کلیدی نباید از 150 کارکتر بیشتر شود",
                                           "required": "کلمات کلیدی نمی تواند خالی باشد"},
                           widget=(forms.TextInput(attrs={'class': 'form-control'})))
    tags = forms.CharField(error_messages={"max_length": "طول تگ ها نباید از 150 کارکتر بیشتر شود",
                                               "required": "تگ ها نمی تواند خالی باشد"},
                               widget=(forms.TextInput(attrs={'class': 'form-control'})))
    class Meta:
        model = subcategory
        fields = ('category' , 'name', 'showindexpage' , 'image' ,'descriptions' , 'keywords' , 'tags' )
class tree_menu(forms.ModelForm):
    name = forms.CharField(error_messages = {"max_length": "طول عنوان نباید از 150 کارکتر بیشتر شود","required" : "عنوان نمی تواند خالی باشد"},
                           widget=(forms.TextInput(attrs={'class':'form-control' })))
    tree = forms.BooleanField(widget=(forms.CheckboxInput(attrs={'id': 'switchmain', "class": "form-check-input"})) , required=False)
    link = forms.CharField(error_messages = {"max_length": "طول لینک نباید از 150 کارکتر بیشتر شود" },
                           widget=(forms.TextInput(attrs={'class':'form-control' })) , required=False)
    class Meta:
        model = treemenu
        fields = ('name','tree','link')
class Variable_(forms.ModelForm):
    name = forms.CharField(error_messages = {"max_length": "طول متغیر نباید از 150 کارکتر بیشتر شود","required" : "متغیر نمی تواند خالی باشد"},
                           widget=(forms.TextInput(attrs={'class':'form-control' })))
    class Meta:
        model = Variable
        fields = ('name',)
class menu_(forms.ModelForm):
    tree = forms.ModelChoiceField(error_messages={"required": "لطفا یک منوی شاخه را انتخاب کنید"},queryset=treemenu.objects.all(),widget=(forms.Select(attrs={'class': 'form-control'})))
    name = forms.CharField(error_messages = {"max_length": "طول منو نباید از 150 کارکتر بیشتر شود","required" : "منو نمی تواند خالی باشد"},
                           widget=(forms.TextInput(attrs={'class':'form-control' })))
    link = forms.CharField(error_messages = {"max_length": "طول لینک نباید از 150 کارکتر بیشتر شود" },
                           widget=(forms.TextInput(attrs={'class':'form-control' })) , required=False)
    class Meta:
        model = menu
        fields = ('name','tree' ,'link')
class sub_menu(forms.ModelForm):
    selectmenu = forms.ModelChoiceField(error_messages={"required": "لطفا یک منوی را انتخاب کنید"},queryset=menu.objects.all(),widget=(forms.Select(attrs={'class': 'form-control'})))
    category = forms.ModelChoiceField(queryset=(subcategory.objects.all()),widget=(forms.Select(attrs={'class': 'form-control'})))
    class Meta:
        model = submenu
        fields = ('selectmenu','category')
class brand_(forms.ModelForm):
    name = forms.CharField(error_messages={"max_length": "طول برند نباید از 150 کارکتر بیشتر شود",
                                           "required": "برند نمی تواند خالی باشد"},
                           widget=(forms.TextInput(attrs={'class': 'form-control'})))
    showindexpage = forms.BooleanField(widget=(forms.CheckboxInput(attrs={'id': 'switchmain', "class": "form-check-input"})),
                                       required=False)
    image = forms.ModelChoiceField(queryset=images.objects.all() , widget=(forms.Select(attrs={'class' : 'form-control none'})))
    descriptions = forms.CharField(error_messages={"max_length": "طول توضیحات نباید از 450 کارکتر بیشتر شود",
                                                   "required": "توضیحات نمی تواند خالی باشد"},
                                   widget=(forms.Textarea(attrs={'class': 'form-control'})))
    keywords = forms.CharField(error_messages={"max_length": "طول کلمات کلیدی نباید از 150 کارکتر بیشتر شود",
                                               "required": "کلمات کلیدی نمی تواند خالی باشد"},
                               widget=(forms.TextInput(attrs={'class': 'form-control'})))
    tags = forms.CharField(error_messages={"max_length": "طول تگ ها نباید از 150 کارکتر بیشتر شود",
                                           "required": "تگ ها نمی تواند خالی باشد"},
                           widget=(forms.TextInput(attrs={'class': 'form-control'})))

    class Meta:
        model = brand
        fields = ( 'name', 'showindexpage', 'image', 'descriptions', 'keywords', 'tags')

class color_(forms.ModelForm):
    name = forms.CharField(error_messages={"max_length": "طول نام رنگ نباید از 150 کارکتر بیشتر شود",
                                           "required": "نام رنگ نمی تواند خالی باشد"},
                           widget=(forms.TextInput(attrs={'class': 'form-control'})))
    color = forms.CharField(error_messages={"max_length": "طول  رنگ نباید از 10 کارکتر بیشتر شود",
                                           "required": "نام نمی تواند خالی باشد"},
                           widget=(forms.TextInput(attrs={'class': 'form-control'})))
    class Meta:
        model = color
        fields = ( 'name', 'color')
class warranty_(forms.ModelForm):
    name = forms.CharField(error_messages={"max_length": "طول گارانتی رنگ نباید از 150 کارکتر بیشتر شود",
                                           "required": "نام گارانتی نمی تواند خالی باشد"},
                           widget=(forms.TextInput(attrs={'class': 'form-control'})))
    class Meta:
        model = warranty
        fields = ( 'name',)
class details_(forms.ModelForm):
    name = forms.CharField(error_messages={"max_length": "طول عنوان جزئیات نباید از 150 کارکتر بیشتر شود",
                                           "required": "نام جزئیات نمی تواند خالی باشد"},
                           widget=(forms.TextInput(attrs={'class': 'form-control'})))
    class Meta:
        model = details
        fields = ( 'name',)
class value_details_(forms.ModelForm):
    namedetails = forms.ModelChoiceField(error_messages={"required": " مقدار نمی تواند خالی باشد"} , queryset=details.objects.all() , widget=(forms.Select(attrs={'class': 'form-control select2'})) )
    value = forms.CharField(error_messages={"max_length": "طول مقدار جزئیات نباید از 150 کارکتر بیشتر شود",
                                           "required": " مقدار نمی تواند خالی باشد"},
                           widget=(forms.TextInput(attrs={'class': 'form-control'})))
    class Meta:
        model = valuedetails
        fields = ( 'namedetails', 'value')
open_sale = 1
close_sale = 2
check_inventory = 3
stop_production = 4
coming_soon = 5
status_choied = (
    (open_sale, 'در حال فروش'),
    (close_sale, 'توقف فروش'),
    (check_inventory, 'اتمام موجودی'),
    (stop_production, 'توقف تولید'),
    (coming_soon, 'به زودی موجود می شود'),
)
class product_(forms.ModelForm):
    name = forms.CharField(error_messages={"max_length": "طول عنوان کالا جزئیات نباید از 150 کارکتر بیشتر شود",
                                           "required": "نام کالا نمی تواند خالی باشد"},
                           widget=(forms.TextInput(attrs={'class': 'form-control'})))
    engname = forms.CharField(error_messages={"max_length": "طول عنوان کالا جزئیات نباید از 150 کارکتر بیشتر شود"},
                           widget=(forms.TextInput(attrs={'class': 'form-control'})),required=False)
    category = forms.ModelMultipleChoiceField(queryset=subcategory.objects.all(),widget=forms.SelectMultiple(),error_messages={"required": "دسته بندی نمی تواند خالی باشد"})
    weight = forms.CharField(widget=(forms.NumberInput(attrs={'class': 'form-control'})),required=False)
    dimensions = forms.CharField(widget=(forms.TextInput(attrs={'class': 'form-control'})),required=False)
    warranty = forms.ModelChoiceField(queryset=warranty.objects.all(),widget=forms.Select(),error_messages={"required": "دسته بندی نمی تواند خالی باشد"})
    image = forms.ModelChoiceField(queryset=images.objects.all(),widget=(forms.Select(attrs={'class': 'form-control none'})))
    imageother = forms.ModelMultipleChoiceField(queryset=images.objects.all(),widget=(forms.SelectMultiple(attrs={'class': 'form-control none'})))
    allowcomment = forms.BooleanField(widget=(forms.CheckboxInput(attrs={'id': 'allowcomment', "data-switch": "info"})),required=False)
    visibility = forms.BooleanField(widget=(forms.CheckboxInput(attrs={'id': 'visibility', "data-switch": "info"})),required=False)
    details = forms.ModelMultipleChoiceField(queryset=valuedetails.objects.all(),widget=forms.SelectMultiple(attrs={'class': 'none' , 'id' : 'id_details'}),error_messages={"required": "دسته بندی نمی تواند خالی باشد"})
    meta_descriptions = forms.CharField(error_messages={"max_length": "طول توضیحات سئو کالا جزئیات نباید از 500 کارکتر بیشتر شود",
                                           "required": "توضیحات سئو نمی تواند خالی باشد"},
                           widget=(forms.Textarea(attrs={'class': 'form-control'})))
    meta_keywords = forms.CharField(error_messages={"max_length": "طول کلمات کلیدی کالا جزئیات نباید از 150 کارکتر بیشتر شود",
                                           "required": "کلمات کلیدی نمی تواند خالی باشد"},
                           widget=(forms.TextInput(attrs={'class': 'form-control'})))
    descriptions = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30 , 'id' : 'tinymce'}))
    status = forms.ChoiceField(choices=status_choied)
    brand = forms.ModelChoiceField(queryset=brand.objects.all(),widget=forms.Select(),error_messages={"required": "دسته بندی نمی تواند خالی باشد"})
    countview = forms.CharField(widget=(forms.NumberInput(attrs={'class': 'form-control none'})),required=False,initial=0)
    class Meta:
        model = product
        fields = ('name' , 'engname' , 'category' , 'weight' , 'warranty' , 'dimensions','countview' , 'image' , 'imageother'  , 'allowcomment' ,'visibility' , 'details' , 'meta_descriptions' , 'meta_keywords' , 'descriptions' , 'status' , 'brand')
class Variable_price_(forms.ModelForm):
    product = forms.ModelChoiceField(error_messages={"required": " محصول نمی تواند خالی باشد"} , queryset=product.objects.all() , widget=(forms.Select(attrs={'class': 'form-control select2'})) )
    color = forms.ModelChoiceField(queryset=color.objects.all() , widget=(forms.Select(attrs={'class': 'form-control select2'})),required=False )
    details = forms.ModelChoiceField(queryset=Variable.objects.all() , widget=(forms.Select(attrs={'class': 'form-control select2'})),required=False )
    price = forms.IntegerField(error_messages={"required": " قیمت نمی تواند خالی باشد"} ,  widget=(forms.NumberInput(attrs={'class': 'form-control'})))
    min = forms.IntegerField(widget=(forms.NumberInput(attrs={'class': 'form-control min min0', 'id' : '0' , 'min' : '1'})))
    max = forms.IntegerField(error_messages={"required": " حداکثر خرید نمی تواند خالی باشد"} ,widget=(forms.NumberInput(attrs={'class': 'form-control max max0', 'id' : '0'})))
    count = forms.IntegerField(error_messages={"required": "  تعداد موجودی نمی تواند خالی باشد"} ,widget=(forms.NumberInput(attrs={'class': 'form-control count count0', 'id' : '0' })))
    colleague = forms.BooleanField(widget=(forms.CheckboxInput(attrs={'id': 'switch0', "data-switch": "info" })),required=False)
    price_colleague = forms.IntegerField(error_messages={"required": " قیمت همکار نمی تواند خالی باشد"},
                               widget=(forms.NumberInput(attrs={'class': 'form-control colleague0' , 'disabled' : 'disabled'})),required=False)
    min_colleague = forms.IntegerField(error_messages={"required": " حداقل خرید همکار نمی تواند خالی باشد"},widget=(forms.NumberInput(attrs={'class': 'form-control min0_colleague colleague0', 'id' : '0', 'disabled' : 'disabled'})),required=False)
    max_colleague = forms.IntegerField(error_messages={"required": " حداکثر خرید همکار نمی تواند خالی باشد" },
                             widget=(forms.NumberInput(attrs={'class': 'form-control max0_colleague colleague0', 'id' : '0', 'disabled' : 'disabled'})),required=False)
    count_colleague = forms.IntegerField(error_messages={"required": " تعداد موجودی همکار نمی تواند خالی باشد"},
                             widget=(forms.NumberInput(attrs={'class': 'form-control count0_colleague colleague0', 'id' : '0', 'disabled' : 'disabled'})),required=False)

    discount = forms.BooleanField(widget=(forms.CheckboxInput(attrs={'id': 'discount0', "data-switch": "info"})),required=False)
    price_discount = forms.IntegerField(widget=(forms.NumberInput(attrs={'class': 'form-control discount0' , 'disabled' : 'disabled'})),required=False)
    class Meta:
        model = Variable_price
        fields = ('product', 'color','details' , 'price' , 'min' , 'max' , 'count' , 'colleague' , 'price_colleague' , 'min_colleague' , 'max_colleague' , 'count_colleague' , 'discount', 'price_discount' , 'timestart' , 'timeend')

    def __init__(self, *args, **kwargs):
        super(Variable_price_, self).__init__(*args, **kwargs)
        self.fields['timestart'] = SplitJalaliDateTimeField(label=('تاریخ شروع تخفیف'),
            widget=AdminSplitJalaliDateTime, # optional, to use default datepicker
            required=False
        )
        self.fields['timeend'] = SplitJalaliDateTimeField(label=('تاریخ پایان تخفیف'),
            widget=AdminSplitJalaliDateTime,
            required=False
        )
class product_comment_(forms.ModelForm):
    account = forms.ModelChoiceField(queryset=customers.objects.all())
    product = forms.ModelChoiceField(queryset=product.objects.all())
    title = forms.CharField(error_messages={"max_length": "طول عنوان نباید از 150 کارکتر بیشتر شود",
                                           "required": "عنوان نمی تواند خالی باشد"},
                           widget=(forms.TextInput(attrs={'class': 'form-control'})))
    starts = forms.IntegerField(widget=(forms.NumberInput(attrs={'class': 'form-control', 'min' : '1'})))
    text = forms.CharField(error_messages={"max_length": "طول نظر نباید از 150 کارکتر بیشتر شود",
                                            "required": "نظر نمی تواند خالی باشد"},
                            widget=(forms.Textarea(attrs={'class': 'form-control'})))
    sendtime = forms.CharField()
    class Meta:
        model = comment_product
        fields = ('account' ,'product' ,'title' , 'starts' , 'text','sendtime')

