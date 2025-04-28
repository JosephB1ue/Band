from django.db import models

class Register_table(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    # email = models.EmailField()
    # confirm_password = models.CharField(max_length=30)
    # mobile = models.ImageField()
    # address = models.TextField()
    # date_of_birth = models.DateField()

class Band(models.Model):
    band_name = models.CharField(max_length=100)
    band_image = models.FileField(upload_to='band_images/')
    band_price = models.IntegerField()
    band_description = models.TextField()

class Carttable(models.Model):
    customer = models.ForeignKey(Register_table, on_delete=models.CASCADE) # ForeignKey is used to create a many-to-one relationship. on_delete=models.CASCADE used to delete the related object when the referenced object is deleted from the cart 
    product = models.ForeignKey(Band, on_delete=models.CASCADE) # CASCADE used to delete the related object when the referenced object is deleted from the cart.
    quantity = models.PositiveIntegerField(default=1) # PositiveIntegerField is used to store positive integers only.


# Create your models here.
