from django import forms

from .models import Movimentacao


class MovimentacaoForm(forms.ModelForm):

    class Meta:
        model = Movimentacao

        fields = [
            'equipamento',
            'codigo',
            'origem',
            'destino',
            'uso',
            'foto',
            'observacao',
        ]
        #Widgets são do bootstrap
        widgets = {
            'equipamento': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'codigo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Código do equipamento'
                }
            ),

            'origem': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Local de origem'
                }
            ),

            'destino': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Local de destino'
                }
            ),

            'uso': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex.: uso administrativo'
                }
            ),

            'foto': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'observacao': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Observações adicionais'
                }
            ),
        }


    def clean_codigo(self):
        codigo = self.cleaned_data['codigo'].strip()

        if not codigo:
            raise forms.ValidationError(
                'Informe o código do equipamento.'
            )

        return codigo


    def clean_origem(self):
        origem = self.cleaned_data['origem'].strip()

        if not origem:
            raise forms.ValidationError(
                'Informe a origem do equipamento.'
            )

        return origem


    def clean_destino(self):
        destino = self.cleaned_data['destino'].strip()

        if not destino:
            raise forms.ValidationError(
                'Informe o destino do equipamento.'
            )

        return destino