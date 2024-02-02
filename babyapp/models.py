from django.db import models
from datetime import date, timedelta
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta




class ChildManager(models.Manager):
    """Creates both a Child and a ChildHealthReview object at the same time.

    When a parent registers a child,
    at the same time, a medical examination schedule is created for the child.

    
    """

    def create_child(self, first_name, last_name, date_of_birth, sex, parent_id):
        child = Child.objects.create(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            sex=sex,
            parent_id=parent_id
        )
        health_rev_dates = (
            child.date_of_birth + timedelta(days=1),
            child.date_of_birth + timedelta(days=40),
            child.date_of_birth + timedelta(days=67),
            child.date_of_birth + timedelta(days=70),
            child.date_of_birth + timedelta(days=89),
            child.date_of_birth + timedelta(days=180),
            child.date_of_birth + timedelta(days=304),
            child.date_of_birth + timedelta(days=363)
        )

     
vaccine_programs = {
    'Program1': ['OPV', 'IPV/OPV', 'HepB', 'DPTw', 'Hib'],
    'Program2': ['DPTw', 'IPV/OPV', 'Hib'],
    'Program3': ['DPTw', 'IPV/OPV', 'Hib'],
    'Program4': ['OPV', 'HepB'],
    'Program5': ['OPV', 'MMR'],
    'Program6': ['TCV'],
    'Program7': ['HepA1']
}

class Child(models.Model):
    SEX = (
        ("Male", "Male"),
        ("Female", "Female")
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_of_birth = models.DateField(help_text='yyyy-mm-dd')
    sex = models.CharField(max_length=7, choices=SEX)
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    Location=models.CharField(max_length=50,null=True,blank=True)
    objects = ChildManager()

    @property
    def age(self):
        # returns the age in years, you need to install pip install python-dateutil
        return relativedelta(date.today(), self.date_of_birth).years

    @property
    def year(self):
        return self.date_of_birth.strftime('%Y')

    @property
    def age_in_month(self):
        return self.date_of_birth.strftime('%m')

    @property
    def age_in_day(self):
        return (date.today() - self.date_of_birth).days  # returns age in days
    
    def get_vaccination_dates(self):
        return [
            
            self.date_of_birth + timedelta(days=40),
            self.date_of_birth + timedelta(days=67),
            self.date_of_birth + timedelta(days=70),
            self.date_of_birth + timedelta(days=89),
            self.date_of_birth + timedelta(days=180),
            self.date_of_birth + timedelta(days=304),
            self.date_of_birth + timedelta(days=363)
        ]
        
    def __str__(self):
        return  self.first_name
        # return f'{self.last_name} {self.first_name} | {self.date_of_birth} | id:{self.id} | pid:{self.parent_id}'
    




class VaxName(models.Model):
    """The model stores inoculation names."""
    vax_name = models.CharField(max_length=64)

    def __str__(self):
        return self.vax_name

class VaxProgram(models.Model):
    vax_program_name=models.CharField(max_length=64)
    year=models.IntegerField()
    Child=models.ForeignKey(Child,on_delete=models.CASCADE)
    vaxes = models.ManyToManyField(VaxName) 

class Vax_Cycle(models.Model):
    vax_cycle_name=models.CharField(max_length=64)
    program=models.ForeignKey(VaxProgram,on_delete=models.CASCADE)

class Vax(models.Model):
    name=models.ForeignKey(VaxName,on_delete=models.CASCADE)
    vax_cycle=models.ForeignKey(Vax_Cycle,on_delete=models.CASCADE)
    exp_vax_date = models.DateField(
        verbose_name='Vaccination date required',
        help_text='YYYY-MM-DD',
        null=True
    )
    vax_date = models.DateField(
        verbose_name='Vaccination date',
        help_text='YYYY-MM-DD',
        null=True,
        blank=True
    )
    symptom_after_vax = models.TextField(
        verbose_name='Observations',
        null=True,
        blank=True
    )

class vaccine_names(models.Model):
    vaccine=models.CharField(max_length=10)

    def __str__(self):
        return self.vaccine

# class VaccinationPrograms(models.Model):
#     selected_vaccines = models.ManyToManyField(vaccine_names, related_name='vaccination_programs')

#     def __str__(self):
#         return f"Vaccination Program {self.id}"


class VaccinePrograms(models.Model):
    vaccines = models.ManyToManyField(vaccine_names)

class Hospitals(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    location=models.CharField(max_length=50,blank=True,null=True)
    slots_available = models.IntegerField(null=True,blank=True)
    programs_available = models.ManyToManyField(VaccinePrograms,default=None)
    
    def __str__(self):
        return self.name


# class VaccineBooking(models.Model):
#     STATUS_CHOICES = [
#         ("Taken", "Taken"),
#         ("Pending", "Pending"),
#     ]

#     parent_name = models.ForeignKey(Child, on_delete=models.CASCADE)
#     parent_email = models.EmailField()
#     hospital = models.ForeignKey(Hospitals, on_delete=models.CASCADE)
#     vaccine_program = models.ForeignKey(VaccinePrograms, on_delete=models.CASCADE)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Pending")
#     booking_date = models.DateTimeField(auto_now_add=True)

#     def save(self, *args, **kwargs):
#         # If booking_date is not null, mark the program as "Taken"
#         if self.booking_date:
#             self.status = "Taken"
#         else:
#             # If booking_date is null, mark other programs as "Pending"
#             VaccineBooking.objects.filter(
#                 parent_name=self.parent_name,
#                 hospital=self.hospital,
#             ).exclude(vaccine_program=self.vaccine_program).update(status="Pending")

#         super().save(*args, **kwargs)
    


class VaccineBooking(models.Model):
    parent_name = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_email = models.EmailField()
    hospital = models.ForeignKey(Hospitals, on_delete=models.CASCADE)
    vaccine_program = models.ForeignKey(VaccinePrograms, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.parent_name
    

# class VaccineStatus(models.Model):
#     program = models.OneToOneField(VaccinePrograms, on_delete=models.CASCADE)
#     is_taken = models.BooleanField(default=False)
#     parent_name = models.ForeignKey(User, on_delete=models.CASCADE)
    

class VaccineStatus(models.Model):
    child_name = models.ForeignKey(Child, on_delete=models.CASCADE)
    program = models.ForeignKey(VaccinePrograms, on_delete=models.CASCADE)
    is_taken = models.BooleanField(default=False)
    