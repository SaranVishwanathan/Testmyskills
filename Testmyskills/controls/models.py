from django.db import models
from django import forms

# Create your models here.
class Levelone_assessment(models.Model):
    qn1=models.IntegerField()
    """
    qn2=models.CharField(max_length=20)
    qn3=models.CharField(max_length=20)
    qn4=models.CharField(max_length=20)
    qn5=models.CharField(max_length=50)
    qn6=models.CharField(max_length=20)
    qn7=models.CharField(max_length=20)
    qn8=models.CharField(max_length=20)
    qn9=models.CharField(max_length=20)
    qn10=models.CharField(max_length=20)
    """

class LvloneForm(forms.ModelForm):
    class Meta:
        model = Levelone_assessment
        fields = '__all__'