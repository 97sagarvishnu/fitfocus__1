from django.contrib import admin
from.models import Trainers,Admission,Payment,otp


admin.site.register(Trainers)

admin.site.register(otp)



class PaymentAdmin(admin.ModelAdmin):
    list_display=('person_name','card_number','expiry','cvv')
    admin.site.register(Payment)


class AdmissionAdmin(admin.ModelAdmin):
    list_display=('name','phone','email','admission_date')
    admin.site.register(Admission)


