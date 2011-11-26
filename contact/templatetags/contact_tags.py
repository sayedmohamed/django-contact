#encoding=utf-8
from django import template
from contact.forms import ContactForm

from django.core.urlresolvers import reverse
register = template.Library()


@register.inclusion_tag('contact/formulaire.html')
def contact_form(backend_url=None):
    """
    En parametre l'url de retour en cas de succes, penser au '/' initial !
    Par defaut, c'est la page /contact/thanks qui est chargée.
    """
    
    if backend_url is None :
        backend_url = reverse("contact_thanks")
    form = ContactForm()
    return {'form': form, 'backend_url' : backend_url}
    
    
    
@register.inclusion_tag('dialogbox.html')
def contact_dialog_form(caller="#contact-button"):
    """
    caller est l'élément jquery qui va appeler la dialog-box
    c'est à dire le bouton "contactez nous"
    """
    
    form = ContactForm()
    return {'form': form, 'caller' : caller}
