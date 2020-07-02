from django.db import models

# Create your models here.
class Clients(models.Model):
    Name = models.CharField(max_length=200, help_text='Enter Clients Name')
    Class_insured = models.CharField(max_length=255)
    Car_plate = models.CharField(max_length=20, default="KBB 406B")
    Insuerer = models.CharField(max_length=100)
    Policy_no = models.CharField(max_length=255)
    Date_insured = models.DateTimeField()
    Date_expiry = models.DateTimeField()
    Rate = models.CharField(max_length=15)
    Tl = models.CharField(max_length=20)
    Pf = models.CharField(max_length=20)
    Sd = models.CharField(max_length=20)
    Sum_insured = models.CharField(max_length=20)
    Annual_premium = models.IntegerField()
    Commision = models.IntegerField()

    class Meta:
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.Name
    
class Claims(models.Model):
    Name = models.CharField(max_length=200)
    Class_insurance = models.CharField(max_length=20)
    Policy_no = models.CharField(max_length=50)
    Claim_no = models.CharField(max_length=20)
    Date_Accident = models.DateTimeField()
    Place = models.CharField(max_length=90)
    Explanation = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = "Claims"

    def __str__(self):
        return self.Name
        

