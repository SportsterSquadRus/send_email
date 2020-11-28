"""django-forms module"""
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Form definition for Contact."""

    class Meta:
        """Meta definition for Contactform."""

        model = Contact
        fields = '__all__'
