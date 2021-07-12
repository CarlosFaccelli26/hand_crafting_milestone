from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductReview, RATE_CHOICES


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
    
    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)
    
    def __init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        frielndly_name = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = frielndly_name
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ('content',
                  'rate',)

    content = forms.CharField(
                              widget=forms.Textarea(
                                attrs={'class': 'form-control form-control-sm'}),
                              required=True)
    rate = forms.ChoiceField(
                             choices=RATE_CHOICES,
                             widget=forms.Select(
                                attrs={'class': 'form-control form-control-sm'}),
                             required=True)
