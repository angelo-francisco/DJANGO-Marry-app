from django import forms
from .models import (Gift, Guest)
from django.conf import settings


class GiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={
                'class': "block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            }),

            "photo": forms.FileInput(attrs={
                'class': "block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            }),

            "price": forms.NumberInput(attrs={
                'class': "block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            }),

            "importance": forms.NumberInput(attrs={
                'class': "block w-full py-3 text-gray-900",
                'type': "range",
                'min': 1,
                'max': 5,
            }),
        }


    def clean_name(self):
        name = self.cleaned_data.get('name')

        if len(name) > 50:
            raise forms.ValidationError("O nome do presente deve ter menos de 50 caracteres.")
        
        return name

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')

        if photo.size > settings.IMAGE_MAX_SIZE:
            raise forms.ValidationError('O tamanho da imagem deve ser menor que 10MB')
        
        if photo.content_type not in settings.IMAGE_ALLOWED_TYPES:
            raise forms.ValidationError('O formato inválido, use apenas PNG ou JPEG.')
    
        return photo

    def clean_importance(self):
        importance = self.cleaned_data.get('importance')
        
        if not (1 <= importance <= 5):
            raise forms.ValidationError('Importância está fora da escala estabelecida.')
        
        if not isinstance(importance, int):
            raise forms.ValidationError("A importância deve ser um dado numérico.")
        
        return importance

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if not isinstance(price, (int, float)):
            raise forms.ValidationError("O preço deve ser um dado numérico.")
        
        return price


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['guest', 'whatsapp', 'max_escorts']
        widgets = {
            'guest': forms.TextInput(attrs={
                'class': "block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            }),

            'whatsapp': forms.TextInput(attrs={
                'class': "block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            }),

            'max_escorts': forms.NumberInput(attrs={
                'min': 0,
                'class': "block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            })

        }

    def clean_guest(self):
        guest = self.cleaned_data.get('guest')

        if len(guest) > 100:
            raise forms.ValidationError('Nome do convidade é muito grande')
        
        return guest
    
    def clean_whatsapp(self):
        whatsapp = self.cleaned_data.get('whatsapp')

        if len(whatsapp) > 50:
            raise forms.ValidationError('Whatsapp muito grande!')
        
        return whatsapp