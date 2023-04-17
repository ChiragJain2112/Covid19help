from django.db import models

# Create your models here.
class State(models.Model):
    statename=models.CharField(max_length=100,null=False,blank=False)
    def __str__(self):
        return self.statename


class City(models.Model):
    cityname=models.CharField(max_length=100,null=False,blank=False)
    state=models.ForeignKey(State,on_delete=models.CASCADE,related_name='cities')
    def __str__(self):
        return self.cityname


class Hospital(models.Model):
    hospitalname=models.CharField(max_length=100,null=False,blank=False)
    city=models.ForeignKey(City,on_delete=models.CASCADE,related_name='hospitals')
    phone=models.CharField(max_length=100,null=False,blank=False)
    address=models.CharField(max_length=100,null=False,blank=False)
    def __str__(self):
        return self.hospitalname


class Facility(models.Model):
    #hospital=models.OneToOneField(Hospital,on_delete=models.CASCADE,primary_key=True)
    title=models.CharField(max_length=100,null=False,blank=False,default='')
    def __str__(self):
        return self.title



class Availability(models.Model):
    hospital=models.ForeignKey(Hospital,on_delete=models.CASCADE,related_name='availabilities')
    facility=models.ForeignKey(Facility,on_delete=models.CASCADE,related_name='availabilities')
    total=models.IntegerField(default=0)
    availabile=models.IntegerField(default=0)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.hospital.hospitalname}-{self.facility.title}'

