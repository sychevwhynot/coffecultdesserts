from django import forms
from phonenumber_field.formfields import PhoneNumberField

from cackes.models import Order


class OrderForm(forms.ModelForm):
    phone = PhoneNumberField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+7 (XXX) XXX-XX-XX',
            'type': 'tel',
        }),
        label='Номер телефона',
        required=True,
        region='RU',
    )
    consent_personal = forms.BooleanField(
        required=True,
        label='Я согласен на обработку персональных данных',
        error_messages={
            'required': 'Необходимо согласие на обработку персональных данных',
        },
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        }),
    )
    consent_policy = forms.BooleanField(
        required=True,
        label='Я ознакомлен и согласен с политикой конфиденциальности',
        error_messages={
            'required': 'Необходимо согласие с политикой конфиденциальности',
        },
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        }),
    )

    class Meta:
        model = Order
        fields = ['name', 'email', 'phone', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@example.com',
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Расскажите, какой торт вы хотите',
                'rows': 4,
            }),
        }

    def save(self, commit=True):
        order = super().save(commit=False)
        if commit:
            order.save()
        return order
