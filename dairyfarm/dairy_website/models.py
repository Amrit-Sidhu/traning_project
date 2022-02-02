from django.db import models


class farmer_record(models.Model):
    farmer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    farm_name = models.CharField(max_length=50)
    farm_type = models.CharField(max_length=50)
    total_animal = models.CharField(max_length=20)


class animal_record(models.Model):
    farmer_id = models.IntegerField()
    tag_no = models.CharField(max_length=15)
    animal_dob = models.DateField()
    body_weight = models.IntegerField()
    breed_type = models.CharField(max_length=20)
    current_lactation  = models.IntegerField()
    last_calving_date = models.DateField()
    is_cattle_inseminated = models.CharField(max_length=10)
    inseminated_type = models.CharField(max_length=30 )
    bull_details = models.CharField(max_length=50,default=None)
    inseminated_date = models.DateField()
    animal_image = models.ImageField(blank=True, null=True)
    animal_type_age = models.CharField(max_length=20,default="calf")


class vaccination(models.Model):
    tag_no = models.CharField(max_length=34 ,default="no selected")
    vaccination_type = models.CharField(default="----",max_length=50)
    vaccination_date = models.DateField(default="----")
    due_date = models.DateField(default="2020-02-02")
    farmer_id = models.IntegerField()


class deworming(models.Model):
    tag_no = models.CharField(max_length=34 ,default="no selected")
    deworming_date = models.DateField(default="2020-02-02")
    medicine_name = models.CharField(default="----",max_length=200)
    due_date = models.DateField(default="2020-02-02")
    farmer_id = models.IntegerField()


class milk_record(models.Model):
    tag_no = models.CharField(max_length=20)
    milk_quantity = models.IntegerField()
    milk_date = models.DateField()
    milk_time = models.CharField(max_length=20)
    farmer_id = models.IntegerField()


class questions(models.Model):
    que_id = models.IntegerField(primary_key=True)
    farmer_id_que = models.IntegerField()
    que_subject = models.CharField(max_length=200)
    que_body = models.CharField(max_length=500)
    que_date = models.DateField()
    farmer_name_que = models.CharField(max_length=50,default="Amritpal Singh")
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)


class answer(models.Model):
    ans_id = models.IntegerField(primary_key=True)
    que_id = models.IntegerField( )
    farmer_id_ans = models.IntegerField()
    ans_body = models.CharField(max_length=500)
    ans_date = models.DateField()
    farmer_name_ans = models.CharField(max_length=50,default="Amritpal Singh")