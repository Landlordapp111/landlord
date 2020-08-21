from django.contrib import admin
from Rooms.models import room
# Register your models here.

class abcAdmin(admin.ModelAdmin):
<<<<<<< HEAD
<<<<<<< HEAD
    list_display = ('Address','NumberOfRooms','price','im2','im3','im4','lender_contact')
=======
<<<<<<< HEAD
    list_display = ('Address','NumberOfRooms','price','im2','im3','im4','lender_contact')
=======
    list_display = ('Address','NumberOfRooms','price','date','im2','im3','im4','lender_contact')
>>>>>>> final
>>>>>>> final
=======
    list_display = ('Address','NumberOfRooms','price','im2','im3','im4','lender_contact')
>>>>>>> 8ec0bb0a8aadbc8d50544daee769579f9b28d94b

admin.site.register(room,abcAdmin)
