from django import forms
from localflavor.us.forms import USZipCodeField
from .models import Order


class OrderCreateForm(forms.ModelForm):
    postal_code = USZipCodeField()

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']
        
    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
