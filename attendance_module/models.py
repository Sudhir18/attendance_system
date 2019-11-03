from django.db import models

# Create your models here.

class Schedule( models.Model):
    name = models.CharField( max_length = 100 , unique = True)
    description = models.CharField( max_length = 1000)

    class Meta:
        db_table = 'schedules'

    def __str__(self):
        return self.name


class RegistationType( models.Model):
    name = models.CharField( max_length = 100 , unique = True)
    description = models.CharField( max_length = 1000)

    class Meta:
        db_table = 'registration_types'

    def __str__(self):
        return self.name


class Person( models.Model):
    name = models.CharField( max_length = 150 , unique = True)
    GENDER_TYPES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    gender = models.CharField( max_length = 1, choices = GENDER_TYPES)
    dob = models.DateField()
    living_place = models.CharField( max_length=250, null=True, blank=True)
    occupation = models.CharField(max_length=250, null=True, blank=True)
    referred_by = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        db_table = 'persons'

    def __str__(self):
        return self.name + " ( " + self.living_place + " ) "

class PersonSerialTracker( models.Model ):

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    registration_type = models.ForeignKey(RegistationType, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    serial_number = models.IntegerField()
    changed_on = models.DateField()

    class Meta:
        db_table = 'person_serial_tracker'

    def __str__(self):
        return self.person.name + " [ " + self.statusregistration_type.name + " : " + self.serial_number + " ] "

class PersonAttendanceInfo(models.Model):

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    person_serial_tracker = models.ForeignKey(PersonSerialTracker, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    ATTENDANCE_STATUS = [
        ('P', 'Present'),
        ('A', 'Absent')
    ]
    status = models.CharField(max_length=1, choices=ATTENDANCE_STATUS)

    class Meta:
        db_table = 'person_attendance_info'

    def __str__(self):
        return self.person.name + " - " + self.status
