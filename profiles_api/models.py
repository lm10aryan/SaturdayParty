from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from datetime import date




class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, phone_number, password):
        """Create a new user profile"""
        if not phone_number:
            raise ValueError('Users must have a Phone Number')

        user = self.model(phone_number=phone_number)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone_number, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(phone_number, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    phone_number = models.IntegerField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'phone_number'


    def __str__(self):
        """Return string representation of user"""
        return str(self.phone_number)




class farmer(models.Model):
    """Basic info of the farmer"""
    farmer_id = models.IntegerField(primary_key=True)
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    street=models.CharField(max_length=200)
    village=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pin_code=models.IntegerField(default=000000)

    def __str__(self):
        """Return name of the user"""
        return '%s, %s'%(self.farmer_id, self.phone_no)



class chemicals_info(models.Model):
    """List of all chemicals """

    chemical_id=models.AutoField(primary_key=True)
    chemical_name=models.CharField(max_length=50)

    def __str__(self):
        """Return name of the chemical"""
        return self.chemical_name


class diseases_info(models.Model):
    """List of all diseases"""
    disease_id=models.AutoField(primary_key=True)
    disease_name=models.CharField(max_length=50)

    def __str__(self):
        """Return name of the disease"""
        return self.disease_name



class fields_info(models.Model):
    """Basic info of the field of the farmer"""
    field_id=models.AutoField(primary_key=True)
    farmer=models.ForeignKey(farmer,on_delete=models.CASCADE)
    street=models.CharField(max_length=200)
    village=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pin_code=models.IntegerField(default=000000)
    total_acres=models.IntegerField(default=0)

    class Meta:
        unique_together = (("field_id", "farmer"),)

    def __str__(self):
        """ Return street of the field """
        return str(self.field_id)

class CropNames(models.Model):
    """ Database model for storing different crops """
    crop_id=models.AutoField(primary_key=True)
    crop_name=models.CharField(max_length=50)

    def __str__(self):
        """Return name of the crop"""
        return self.crop_name


class products_info(models.Model):
    """Basic info of the crop for a particular farmer """
    product_id=models.AutoField(primary_key=True)
    field=models.ForeignKey(fields_info,on_delete=models.CASCADE)
    product_name=models.ForeignKey(CropNames,on_delete=models.DO_NOTHING,default=None)
    seed_type=models.CharField(max_length=50)
    date_of_start=models.DateField()
    acres=models.IntegerField()

    class Meta:
        unique_together = (("product_id","field"))

    def __str__(self):
        """Return product Name of the crop"""
        return self.product_name


class QuestionSheet(models.Model):
    """Question Sheet for the crop"""
    id=models.AutoField(primary_key=True)
    past_question=models.CharField(max_length=255)
    future_question=models.CharField(max_length=255)
    type=models.CharField(max_length=50)
    constraint=models.CharField(max_length=50,default='',blank=True)
    options_text=models.CharField(max_length=300,default='',blank=True)
    options_value=models.CharField(max_length=50,default='',blank=True)
    question_tag=models.CharField(max_length=100)
    past_condition=models.CharField(max_length=100,default='',blank=True)
    future_condition=models.CharField(max_length=100,default='',blank=True)

class PhaseDecider(models.Model):
    """Decides which phase for particular farmer based on sow in date"""
    id=models.AutoField(primary_key=True)
    crop=models.ForeignKey(CropNames,on_delete=models.DO_NOTHING)
    phase_id=models.IntegerField()
    start_day=models.IntegerField()
    end_day=models.IntegerField()

class PhaseQuestionLinker(models.Model):
    """Links phase with question """
    id=models.AutoField(primary_key=True)
    phase=models.IntegerField()
    question_id=models.IntegerField()
    tense=models.CharField(max_length=6)


class DailyAlertCycle(models.Model):
    """Daily Alerts"""
    id=models.AutoField(primary_key=True)
    day_cycle=models.IntegerField()
    day_action=models.CharField(max_length=500,blank=True)
    day_adv=models.CharField(max_length=500,blank=True)
    fertiliser=models.CharField(max_length=500,blank=True)
    fert_spray=models.CharField(max_length=100,blank=True)
    fert_adv=models.CharField(max_length=200,blank=True)
    diseases=models.CharField(max_length=200,blank=True)
    symptoms=models.CharField(max_length=500,blank=True)
    causes=models.CharField(max_length=500,blank=True)
    prevention=models.CharField(max_length=500,blank=True)




""" MAIN TABLES """




class SeasonTable(models.Model):
    """Basic List of season"""
    season_id=models.AutoField(primary_key=True)
    season_name=models.CharField(max_length=55)

    def __str__(self):
        """Return name of season """
        return self.season_name

class PhaseDecide(models.Model):
    """Phase in terms of crop,season,daywise"""
    id=models.AutoField(primary_key=True)
    crop=models.ForeignKey(CropNames,on_delete=models.CASCADE)
    season=models.ForeignKey(SeasonTable,on_delete=models.CASCADE)
    start_day=models.IntegerField()
    end_day=models.IntegerField()
    phase_no=models.IntegerField()
    phase_name=models.CharField(max_length=55)

    def __str__(self):
        """Return Phase Number """
        return self.phase_no

class MasterIdTable(models.Model):
    """Master id in terms of crop,season,phase"""
    m_id=models.IntegerField(primary_key=True)
    phase=models.ForeignKey(PhaseDecide,db_column="phase_no",on_delete=models.CASCADE)
    season=models.ForeignKey(SeasonTable,on_delete=models.CASCADE)
    crop=models.ForeignKey(CropNames,on_delete=models.CASCADE)

    def __str__(self):
        """Return master id"""
        return self.m_id

class SoilTable(models.Model):
    """Basic List of soil type"""
    soil_id=models.AutoField(primary_key=True)
    soil_type=models.CharField(max_length=55)

    def __str__(self):
        """Return Soil Type"""
        return self.soil_type

class M2Table(models.Model):
    """M2 id based on crop and season"""
    m2=models.IntegerField(primary_key=True)
    crop_id=models.ForeignKey(CropNames,on_delete=models.CASCADE)
    season_id=models.ForeignKey(SeasonTable,on_delete=models.CASCADE)

    def __str__(self):
        """Return m2 id"""
        return self.m2
