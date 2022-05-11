from django import forms
from django.utils.translation import gettext_lazy as _


# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
                                # choices=PRODUCT_QUANTITY_CHOICES,
                                widget=forms.NumberInput(attrs={ 'class':'qty-text'}),
                                initial=1
                                )
                                # coerce=int,
                                # label=_('Quantity'))
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput
                                  )
    
    width = forms.IntegerField(
                                required=False,
                                # choices=PRODUCT_QUANTITY_CHOICES,
                                widget=forms.NumberInput(attrs={ 'class':'qty-text'}),
                                initial=1
                                )
    
    length = forms.IntegerField(
                                required=False,
                                # choices=PRODUCT_QUANTITY_CHOICES,
                                widget=forms.NumberInput(attrs={ 'class':'qty-text'}),
                                initial=1
                                )
    
    height = forms.IntegerField(
                                required=False,
                                # choices=PRODUCT_QUANTITY_CHOICES,
                                widget=forms.NumberInput(attrs={ 'class':'qty-text'}),
                                initial=1
                                )
