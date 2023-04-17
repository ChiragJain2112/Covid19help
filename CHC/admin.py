from django.contrib import admin
from CHC.models import State,City,Hospital,Facility,Availability

# Register your models here.

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=Hospital)
def afterHospitalSave(signal,instance,**kwargs):
    facilities=Facility.objects.all()
    for facility in facilities:
        availability=Availability(hospital=instance,facility=facility)
        availability.save()


@receiver(post_save,sender=Facility)
def afterFacilitySave(signal,instance,**kwargs):
    hospitals=Hospital.objects.all()
    for hospital in hospitals:
        availability=Availability(hospital=hospital,facility=instance)
        availability.save()

class FacilityAdmin(admin.ModelAdmin):
    model=Facility
    list_display = ['title']



class HospitalAdmin(admin.ModelAdmin):
    model=Hospital
    list_display = ['hospitalname','city','phone','address']



class CityAdmin(admin.ModelAdmin):
    model=City
    list_display = ['cityname','state']


class AvailabilityAdmin(admin.ModelAdmin):
    model=Availability
    list_display = ['hospital','facility','total','availabile','updated_at']
    list_editable = ['total','availabile']

admin.site.register(State)
admin.site.register(City,CityAdmin)
admin.site.register(Hospital,HospitalAdmin)
admin.site.register(Facility,FacilityAdmin)
admin.site.register(Availability,AvailabilityAdmin)