from django.db import models

class Company(models.Model):
    company_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type_of_company = models.CharField(max_length=100 , choices=(('IT' , 'IT') , ('Non IT' , 'Not IT') , ('Mobile Phones' , 'Mobile Phones')))
    established_date = models.DateField(auto_now= True)
    active = models.BooleanField(default= True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    employee_designation = models.CharField(max_length=100)
    employee_salary = models.IntegerField()
    company = models.ForeignKey(Company, on_delete = models.CASCADE)

    def __str__(self):
        return self.employee_name
