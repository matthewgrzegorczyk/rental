# -*- coding: utf-8 -*-

from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
from django.forms.extras.widgets import SelectDateWidget, SelectDateWidget


class ReserveItem(forms.Form):
    reserve_from = forms.DateTimeField()
    reserve_to = forms.DateTimeField()
    # comment = forms.CharField(label="Komentarz", widget=forms.Textarea)


class registerForm(forms.Form):
    image = forms.ImageField()
