from django.db import models
# from django.forms.models import model_to_




class Person(models.Model):
    
    reg = models.CharField(max_length=30,null=True,unique=True)
    name = models.CharField(max_length=30,null=True)
    subject = models.CharField(max_length=30,null=True)
    mark = models.PositiveBigIntegerField(null=True)
    date = models.DateField(auto_now_add=False,blank=True,null=True)
    def __str__(self):
        return self.id
        

    # def get_object(self):
    #     return self.request.Person
    # def Person_id(self):
    #    return self.id
    # marks =models.IntegerField()
    # reg_no=models.CharField(max_length=50)
    # reg_no=models.ForeignKey()
    # Reg_NO = models.CharField(max_length=50)
    # marks = models.DecimalField(primary_key=True)

# class Employees(models.Model):
#     EmployeeId = models.AutoField(primary_key=True)
#     EmployeeName = models.CharField(max_length=500)
#     DepartmentName = models.CharField(max_length=500)
    