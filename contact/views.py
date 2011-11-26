#encoding=utf-8
from django import http
from django.views.decorators.cache import cache_page
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.core.mail import send_mail
import forms
import models
# import the logging library
import logging
import settings

# Get an instance of a logger
logger = logging.getLogger("serious.custom")

@cache_page(60 * 60 * 24)
def index(request):
    'affiche le formulaire de contact'
    if request.method == 'POST': # If the form has been submitted...
        res = save(request)
        if res :
            return HttpResponseRedirect(request.POST['backend_url'])
            
    form = forms.ContactForm() # An unbound form

    return render_to_response('contact/index.html', {'form' : form}, context_instance=RequestContext(request))
    
    
def ajax(request):
    res = save(request)
    return HttpResponse(res, mimetype='text/plain')
    

    
def save(request):
    'sauvegarde le message et envoie un mail'
    if request.method == 'POST': # If the form has been submitted...
        form = forms.ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            contact = forms.ContactForm(request.POST)
            
            #sauvegarde en base de données
            contact = contact.save()
            
            #envoi d'un email
            send_mail(  '[SERIOUS-WORKS.ORG] - Prise de contact', 
                        "status : %s\n\n%s" % (contact.get_status_display(), contact.message),       
                        contact.email,
                        settings.CONTACT_EMAIL_TO, 
                        fail_silently=True)
            
            return True
            
    return False

    
@cache_page(60 * 60 * 24)
def thanks(request):
    return render_to_response('contact/thanks.html', {}, context_instance=RequestContext(request))
    
