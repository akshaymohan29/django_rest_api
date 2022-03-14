from django.db import models

class StudentsSchool(models.Model):
    school=models.CharField(max_length=50)
    school_address=models.CharField(max_length=50)
    def __str__(self):
        return self.school

class Grade(models.Model):
    name=models.CharField(max_length=10)
    mark=models.IntegerField()
    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=100)
    roll_no=models.IntegerField()
    std=models.IntegerField()
    detail=models.TextField(max_length=200)
    school=models.ForeignKey(StudentsSchool, on_delete=models.CASCADE)
    grade=models.ForeignKey(Grade,on_delete=models.CASCADE)

    def __str__(self):
        return self.name