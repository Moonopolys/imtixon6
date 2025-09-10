from django import forms

from .models import Ads


class CommentForm(forms.Form):
    text = forms.CharField(max_length=500, label="Izohi", widget=forms.TextInput(
        attrs={
            "style": "width: 63%; border-radius: 5px; padding: 10px; margin-bottom: 10px",
            "placeholder": "Izoh matni..."
        }
    ))


class AdsForm(forms.ModelForm):
    class Meta:
        model = Ads
        # fields = '__all__'
        exclude = ["views"]
        lable = {
            "title": "NOMI",
            "description": "MATNI"
        }
        widgets = {
            "title": forms.TextInput(attrs={
                "style": "width: 76%",
                "placeholder": "Nomi"
            })
        }