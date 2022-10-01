from django.forms import ModelForm
from autos.models import Make


# Create the form class.
"""
subclasses ModelForm to derive the form from a model.

In this case the model class is Make and the fileds is all of 'em

"""
class MakeForm(ModelForm):
    class Meta:
        model = Make
        fields = '__all__'
