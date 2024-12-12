from django import forms


class CreateProductForm(forms.Form):
    product_name = forms.CharField(max_length=128)
    product_description = forms.CharField(widget=forms.Textarea, label='Input description')
    price = forms.DecimalField(label='Input price', min_value=1, max_value=100000)
