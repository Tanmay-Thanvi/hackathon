from django.db import models

# Create your models here.
class PromptData(models.Model):
    prompt = models.TextField()
    answer = models.TextField()
    isSharable = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)  
    last_modified_date = models.DateTimeField(auto_now=True, null=True, blank=True)  