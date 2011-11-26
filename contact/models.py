from django.utils.translation import ugettext as _
from django.db import models

STATUS_CHOICES = (
    ('P', _('Particulier')),
    ('A', _('Association')),
    ('E', _('Entreprise')),
)

class Contact(models.Model):
    
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    email = models.EmailField()
    message = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.message