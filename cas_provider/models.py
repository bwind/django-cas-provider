from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.importlib import import_module


ServiceTicket = None
LoginTicket = None


alt_models = ('CAS_SERVICE_TICKET_MODEL', 'CAS_LOGIN_TICKET_MODEL')
if all([hasattr(settings, name) for name in alt_models]):
    def get_model(name):
        name = getattr(settings, name)
        dot = name.rindex('.')
        module = import_module(name[:dot])
        return getattr(module, name[dot + 1:])
    ServiceTicket, LoginTicket = [get_model(m) for m in alt_models]


if not ServiceTicket:
    class ServiceTicket(models.Model):
        user = models.ForeignKey(User)
        service = models.URLField()
        ticket = models.CharField(max_length=256)
        created = models.DateTimeField(auto_now=True)

        def __unicode__(self):
            return "%s (%s) - %s" % (self.user.username, self.service,
                self.created)


if not LoginTicket:
    class LoginTicket(models.Model):
        ticket = models.CharField(max_length=32)
        created = models.DateTimeField(auto_now=True)

        def __unicode__(self):
            return "%s - %s" % (self.ticket, self.created)
