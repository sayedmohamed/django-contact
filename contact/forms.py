from django.utils.translation import ugettext as _
import floppyforms as forms
from form_utils.forms import BetterForm, BetterModelForm
from models import Contact
class ContactForm(forms.ModelForm):
    status    = forms.ChoiceField(
        
        choices=(('P', _('Particulier')), ('A', _('Association')), ('E', _('Entreprise'))),
        widget=forms.RadioSelect(choices=((False, 'Particulier'), (True, 'Entreprise')),),
        )

    email   = forms.EmailField()
    message = forms.CharField(widget = forms.Textarea(attrs={'size':'40'}),)
        # 
    class Meta:
        model = Contact
        #     fieldsets = [({'fields': ['entreprise', 'email', 'message'],})]
        #     # row_attrs = {'type': {'style': 'display: none'}}
        #     
        #     widgets = {
        #                 'entreprise' : forms.RadioSelect(choices=((False, 'Particulier'), (True, 'Entreprise')),),
        #                 'message' : forms.Textarea(attrs={'size':'40'}),
        #     }