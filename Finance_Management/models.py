from django.db import models
from django.db.models import *
from Events.models import *
# Create your models here.
class TotalFund(models.Model):
    TotalAmount = FloatField(default=0)
    
    def __str__(self):
        return f"Total Amount: {self.TotalAmount}"
    
class Fund(models.Model):
    fund_provider= CharField(max_length=200)
    regno = CharField(max_length=200,blank=True,null=True,help_text="requrired if the provider is student")
    cls = CharField(max_length=200,blank=True,null=True,help_text="requrired if the provider is student")    
    type = CharField(max_length=200)
    amount = FloatField()
    billing_no = CharField(max_length=200,default="",unique=True)
    
    def save(self, *args, **kwargs):
        is_new = self._state.adding
        if not is_new:
            # Get original value from DB
            old = Fund.objects.get(pk=self.pk)
            difference = self.amount - old.amount
            TotalFund.objects.all().update(TotalAmount=F('TotalAmount') + difference)
        else:
            TotalFund.objects.all().update(TotalAmount=F('TotalAmount') + self.amount)

        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Provider: {self.fund_provider}: amount: {self.amount}: Bill: {self.billing_no}"
    
class Expence(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField()
    billing_no = models.CharField(max_length=200,unique=True)

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        if not is_new:
            old = Expence.objects.get(pk=self.pk)
            difference = self.amount - old.amount
            TotalFund.objects.all().update(TotalAmount=F('TotalAmount') - difference)
        else:
            TotalFund.objects.all().update(TotalAmount=F('TotalAmount') - self.amount)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Event: {self.event} | Amount: {self.amount} | Bill No: {self.billing_no}"
    