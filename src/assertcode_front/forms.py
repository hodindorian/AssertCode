from django import forms

class QRCodeForm(forms.Form):
    url = forms.URLField(
        label="Lien",
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'https://example.com'
        })
    )

    fill_color = forms.CharField(
        label="Couleur du QR",
        initial="#000000",
        widget=forms.TextInput(attrs={
            'type': 'color',
            'class': 'form-control form-control-color'
        })
    )

    back_color = forms.CharField(
        label="Couleur du fond",
        initial="#ffffff",
        widget=forms.TextInput(attrs={
            'type': 'color',
            'class': 'form-control form-control-color'
        })
    )