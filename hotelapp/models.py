from django.db import models

# Create your models here.

class Blog(models.Model):
    STATUS=[
        ('open','open'),
        ('close','close')
    ]
    title=models.CharField(max_length=100,null=True,blank=True)
    des=models.TextField()
    status=models.CharField(max_length=20,choices=STATUS)
    created_at=models.DateTimeField(auto_now_add=True)
    mobile=models.IntegerField()
    def __str__(self):
        return f'{self.title},{self.mobile}'

# creating model used for model relation
class Student(models.Model):
    GENDER=[
        ('M','Male'),
        ('F','Female'),
        ('O','Other')
    ]
    name=models.CharField(max_length=20,null=True,blank=True)
    age=models.PositiveIntegerField(null=True,blank=True)
    mobile=models.PositiveIntegerField(null=True,blank=True)
    gender=models.CharField(choices=GENDER)
    read_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.age}'
    
# Model relation - one to one , one to many , many to many
#one to one
class StudentEducation(models.Model):
    student=models.OneToOneField(Student,on_delete=models.CASCADE)
    class_name=models.CharField(max_length=100)
    passing_year=models.IntegerField(max_length=100)
    college_name=models.CharField(max_length=100)
    max_marks=models.PositiveIntegerField(default=100)
    obt_marks=models.PositiveIntegerField(default=100)
    per=models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.class_name , self.college_name}'

# one to many field aka foreign key

class StudentMobile(models.Model):
    Student=models.ForeignKey(Student,on_delete=models.CASCADE)

    mobile=models.PositiveBigIntegerField()
    city=models.CharField(max_length=30)

    def __str__(self):
        return f'{self.Student.name},{self.mobile}'
    
# many to many

class Author(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    def __str__(self):
        return self.name
    
class Books(models.Model):
    author=models.ManyToManyField(Author)
    book_name=models.CharField(max_length=20)
    content=models.TextField()

    def __str__(self):
        return f'{str(self.author.name)}, {self.book_name}'

    
# Model inheritance

class BasicInfo(models.Model):
    GENDER=[
        ('male','male'),
        ('female','female'),
        ('other','other')
    ] 
    name=models.CharField(max_length=20,null=True,blank=True)
    age=models.PositiveIntegerField(null=True,blank=True)
    gender=models.CharField(choices=GENDER)
    mobile=models.PositiveIntegerField(null=False,blank=True)
    
    class Meta:
        abstract=True

class SellerInfo(BasicInfo):                                  # used basic info as inheritance
    address=models.CharField(max_length=50,null=True,blank=True)
    gst_number=models.IntegerField()

class CustomerInfo(BasicInfo):
    city=models.CharField(max_length=20)
    aadhar=models.IntegerField()  

    # for creating object we can create a variable first
    # vinay=models.Manager     AND use vinay at the place of objects
    
class Todo(models.Model):
    task=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
