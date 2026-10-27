from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    category_name=models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.category_name

class ProductDb(models.Model):
    category=models.ForeignKey(CategoryDb,on_delete = models.CASCADE)
    product_name = models.CharField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    #here maxlength=10 defines we can give 10 digit amount and decimal place 2 defines after point we can add two digits
    stock = models.IntegerField()

    def __str__(self):
        return self.product_name

