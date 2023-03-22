from django import forms


# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


# class CartAddProductForm(forms.Form):
#     quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int,label='Quantity')
#     override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(initial=1)
    override = forms.BooleanField(required=False,  initial=False,  widget=forms.HiddenInput)
