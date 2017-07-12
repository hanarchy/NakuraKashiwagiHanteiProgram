from django import forms


class DetectorForm(forms.Form):
    context = forms.CharField(
        widget=forms.Textarea(attrs={"class": "center-block"}),
        required=True,
        label='')
