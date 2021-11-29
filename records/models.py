from django.contrib.auth import get_user_model
from django.db import models

CustomUser = get_user_model()
class Record(models.Model):
    # id = models.AutoField(primary_key=True)
    sender = models.CharField(max_length=100)
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    office = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.filename
    
