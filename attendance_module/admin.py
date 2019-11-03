from django.contrib import admin
from attendance_module.models import Person, PersonAttendanceInfo, PersonSerialTracker, RegistationType, Schedule

# Register your models here.
admin.site.register(Person)
admin.site.register(PersonAttendanceInfo)
admin.site.register(PersonSerialTracker)
admin.site.register(RegistationType)
admin.site.register(Schedule)
