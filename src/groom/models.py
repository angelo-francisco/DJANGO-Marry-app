from django.db import models
from uuid import uuid4
from secrets import token_urlsafe
from django.shortcuts import get_object_or_404


essencial = {
    'null': True,
    'blank': True
}

status_choices = (
    ('AC', 'Aguardando confirmação'),
    ('C', 'Confirmado'),
    ('R', 'Recusado')
)


class Guest(models.Model):
    guest = models.CharField(max_length=100, **essencial)
    whatsapp = models.CharField(max_length=50, **essencial)
    token = models.CharField(max_length=200, **essencial)
    max_escorts = models.PositiveIntegerField(default=0, **essencial) 
    status = models.CharField(max_length=2, choices=status_choices, default='AC')
    uid = models.UUIDField(default=uuid4, unique=True, **essencial, editable=False)


    def save(self, *args, **kwargs):
        if not self.token:
            self.token = token_urlsafe(16)
        
        super(Guest, self).save(*args, **kwargs)

    def __str__(self):
        return self.guest
    

    @property
    def link(self):
        return f'groom/guests/see/?token={self.token}'
    

class Gift(models.Model):
    name = models.CharField(max_length=50, **essencial)
    photo = models.ImageField(upload_to="gifts/photos/", **essencial)
    price = models.FloatField(**essencial)
    importance = models.IntegerField(**essencial)
    reservated = models.BooleanField(default=False, **essencial)
    reservated_by = models.ForeignKey(Guest, on_delete=models.CASCADE, **essencial)
    uid = models.UUIDField(default=uuid4, unique=True, **essencial, editable=False)


    def __str__(self):
        return self.name


class Escorts(models.Model):
    escort = models.CharField(max_length=100, **essencial)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)