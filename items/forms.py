# -*- coding: utf-8 -*-

from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
from django.forms.extras.widgets import SelectDateWidget, SelectDateWidget


class ReserveItem(forms.Form):
    reserve_from_date = forms.DateTimeField(label="Reserve since")
    reserve_from_time = forms.SplitDateTimeField(label="Rezerw", widget=AdminSplitDateTime())
    reserve_to_date = forms.DateTimeField(label="Reserve to", widget=AdminSplitDateTime)
    reserve_to_time = forms.DateTimeField(label="Reserve to", widget=AdminSplitDateTime)
    comment = forms.CharField(label="Komentarz", widget=forms.Textarea)


class registerForm(forms.Form):
    image = forms.ImageField()
