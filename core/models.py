from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    context = models.TextField(max_length=300)

    def __repr__(self):
        return "Sender: " + self.name + "Context: " + self.context[10:]