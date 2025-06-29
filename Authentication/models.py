from django.db import models
from django.db.models import *
from django.contrib.auth.models import User
# Create your models here.

class Secretry(models.Model):
    user = OneToOneField(User,on_delete=CASCADE)
    type_choices = [
        ("Chief","Chief"),
        ("Chief-Joind","Chief-Joid"),
        ("Joind","Joind")
        
    ]
    type=CharField(max_length=200,choices=type_choices,null=True,blank=True)
    profile = ImageField(upload_to="Secretry")
    mobile = IntegerField()
    batch = CharField(max_length=200)
    
    
    def __str__(self):
        stauts =" "
        if(self.user.is_active):
            status= "Active"
        else: 
            status ="In Active"
        return f"User: {self.user} Status: {status} batch: {self.batch}"
    
class Trusherer(models.Model):
    user = OneToOneField(User,on_delete=CASCADE)
    profile = ImageField(upload_to="Treshere")
    mobile = IntegerField()
    batch = CharField(max_length=200)
    
    def __str__(self):
        stauts =" "
        if(self.user.is_active):
            status= "Active"
        else: 
            status ="In Active"
        return f"User: {self.user} Status: {status} batch: {self.batch}"
    
class Quardinators(models.Model):
    user = OneToOneField(User,on_delete=CASCADE)
    department = CharField(max_length=200)
    qulification = TextField()
    profile = ImageField(upload_to="Quardinators")
    mobile = IntegerField()
    
    def __str__(self):
        stauts =" "
        if(self.user.is_active):
            status= "Active"
        else: 
            status ="In Active"
        return f"User: {self.user} Status: {status} " #batch: {self.batch}
    
class Swifters(models.Model):
    user = OneToOneField(User,on_delete=CASCADE)
    profile = ImageField(upload_to="Treshere")
    mobile = IntegerField()
    batch = CharField(max_length=200)
    
    def __str__(self):
        stauts =" "
        if(self.user.is_active):
            status= "Active"
        else: 
            status ="In Active"
        return f"User: {self.user} Status: {status} batch: {self.batch}"

    
class Students(models.Model):
    user = OneToOneField(User,on_delete=CASCADE)
    regno = CharField(max_length=20)
    dob = DateField()
    cls = CharField(max_length=200)
    department = CharField(max_length=200)
    profile = ImageField(upload_to="Students")
    year_choices =[
        ("I-Year","I-Year"),
        ("II-Year","II-Year"),
        ("III-Year","III-Year"),
    ]
    year_of_study = CharField(max_length=200,choices=year_choices,default=1)
    batch = CharField(max_length=200,help_text="Example : 2021-2024")
    
    def __str__(self):
        stauts =" "
        if(self.user.is_active):
            status= "Active"
        else: 
            status ="In Active"
        return f"User: {self.user} Status: {status} batch: {self.batch}"
    