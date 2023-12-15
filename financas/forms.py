from django import forms


class ImportarCsvForm(forms.Form):
    arquivo = forms.FileField(
        widget=(
            forms.FileInput(
                attrs={
                    "class": "form-control",
                    "accept": "text/csv",
                    "id": "file",
                    },
            )
        ),
        label="Faça o upload do arquivo CSV."
    )