


from django.forms import ModelForm as MainModelForm
from .models import MyCar as Model

class ModelForm(MainModelForm):
     class Meta:
         model = Model
         fields = ('__all__')
         labels = {
             'name':  'Writer',
         }
         help_texts = {
           'name': 'Some useful help text.',
         }
         error_messages = {
             'name': {
                 'max_length':  "This writer's name is too long.",
              },
         }
