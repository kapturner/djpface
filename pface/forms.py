from django import forms

class GcodeFileForm(forms.Form):
    gcodefile = forms.FileField(
        label='Select a gcode file',
        help_text='Upload GCode file'
    )
