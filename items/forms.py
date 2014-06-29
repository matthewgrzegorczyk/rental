# -*- coding: utf-8 -*-

from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
from django.forms.extras.widgets import SelectDateWidget

class ReserveItem(forms.Form):
    reserve_from = forms.DateTimeField(label="Reserve since", widget=AdminSplitDateTime)
    reserve_to = forms.DateTimeField(label="Reserve to", widget=AdminSplitDateTime)
    comment = forms.CharField(label="Komentarz", widget=forms.Textarea)
