# -*- coding: utf-8 -*-

from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
from django.forms.extras.widgets import SelectDateWidget, SelectDateWidget


class registerForm(forms.Form):
    avatar = forms.ImageField(label="Avatar")
