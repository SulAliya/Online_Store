from django.forms import ModelForm, BooleanField, forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ('view_counter', 'owner')

    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('product_name')
        for forbidden_word in self.forbidden_words:
            if forbidden_word in cleaned_data.lower():
                raise forms.ValidationError('Имеются запрещённые слова')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        for forbidden_word in self.forbidden_words:
            if forbidden_word in cleaned_data.lower():
                raise forms.ValidationError('Имеются запрещённые слова')
        return cleaned_data


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'current_version')


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

