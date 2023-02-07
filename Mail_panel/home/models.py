from django.db import models

STATUS=(
    ('approved', 'apporoved'),
    ('unapproved', 'unapproved')
    )

class Emp(models.Model):
    to=models.CharField(max_length=50)
    name=models.CharField(max_length=30)
    subject=models.CharField(max_length=50)
    description=models.TextField()
    from_emp=models.CharField(max_length=50, unique=True)
    def __str__(self) -> str:
        return self.name

class Admin(models.Model):
    emp_details=models.ForeignKey(Emp,on_delete=models.CASCADE)
    response=models.CharField(max_length=30, choices=STATUS)
    def __str__(self) -> str:
        return self.emp_details.name +' '+ self.response

        
