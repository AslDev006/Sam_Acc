import uuid
from django.db import models

Boglanildi = "Bog'lanildi"
Boglanilmadi = "Bog'lanilmadi"
class Contact_Model(models.Model):
    Call = (
        (Boglanildi, Boglanildi),
        (Boglanilmadi, Boglanilmadi),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=13)
    called = models.CharField(max_length=100, choices=Call, default=Boglanilmadi)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name