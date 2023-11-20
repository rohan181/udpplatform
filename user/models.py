from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(
        self,
        firstname,
      
        email=None,
        phone_number=None,
        password=None,
        is_active=True,
        is_staff=False,
        is_superuser=False,
    ):
        if not email and not phone_number:
            raise ValueError("User must have an email or phone number")
        if not  firstname:
            raise ValueError("User must have a full name")
       
        user = self.model(
            email=self.normalize_email(email) if email else None,
            phone_number=phone_number,
            firtname= firstname,
            
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,  firstname, email, password):
        user = self.create_user(
             firstname== firstname,
            
            email=email,
           # phone_number=phone_number,
            password=password,
            is_staff=True,
            is_superuser=True,
        )
        return user

class User(AbstractBaseUser, PermissionsMixin):
    #fullname= models.CharField(verbose_name="fullname", max_length=255)
    firstname= models.CharField(verbose_name="first name", max_length=255,blank=True,
        null=True)
    lastname= models.CharField(verbose_name="last name", max_length=255,blank=True,
        null=True)
    #last_name = models.CharField(verbose_name="Last Name", max_length=255)
    user_type = models.CharField(max_length=10, choices=[('parent', 'parent'), ('child', 'child')], blank=True, null=True)
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
        blank=True,
        null=True,
    )
    # Address fields
    street = models.CharField(verbose_name="street", max_length=255, blank=True, null=True)
    city = models.CharField(verbose_name="city", max_length=255, blank=True, null=True)
    state = models.CharField(verbose_name="state", max_length=255, blank=True, null=True)
    zip_code = models.CharField(verbose_name="zip code", max_length=10, blank=True, null=True)
    parent_user = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
   


    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    fcm_token = models.CharField(max_length=255, blank=True, null=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'# You can set it to 'phone_number' if you want to allow phone number as username
    REQUIRED_FIELDS = ['firstname']

    def get_username(self):
        # This method returns the username used for authentication.
        # You can modify this method to return email or phone_number based on your requirements.
        return self.email or self.phone_number

    def __str__(self):
        return self.get_username()
    



class Profileinfo1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
   
    user_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profilephoto= models.ImageField(upload_to='profilephoto/',blank= True,null= True)
    # Add other additional fields for the profile here (e.g., profile_picture, bio, etc.)

    def __str__(self):
        return self.user.get_username()
    



class Profileinfolocationbd(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    District = models.CharField(max_length=255, blank=True, null=True)
  


















class Profileinfolocationabroad(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    countryname = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    duration = models.PositiveIntegerField(default=0,null=True)




class Profileinfoexperience(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    durationstay = models.PositiveIntegerField(default=0,null=True)   

    industry = models.CharField(max_length=255, blank=True, null=True)
    areaofexpertise = models.CharField(max_length=255, blank=True, null=True) 
    durationstayexperience = models.PositiveIntegerField(default=0,null=True) 





class Profilecomplete1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
    type= models.CharField(max_length=255, blank=True, null=True)
    Designation = models.CharField(max_length=255, blank=True, null=True)
    companyname = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)



class Profilecomplete2(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    Designation = models.CharField(max_length=255, blank=True, null=True)
    companyname = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    durationstart= models.CharField(max_length=255, blank=True, null=True)
    durationend= models.CharField(max_length=255, blank=True, null=True)
    responsibility= models.CharField(max_length=1000, blank=True, null=True)



class Profilecomplete3(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    Digree = models.CharField(max_length=255, blank=True, null=True)
    
 
    durationstart= models.CharField(max_length=255, blank=True, null=True)
    durationend= models.CharField(max_length=255, blank=True, null=True)
    educationalinstitute= models.CharField(max_length=1000, blank=True, null=True)   



 






   




class Profilecomplete4(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    permanent = models.BooleanField(default=True)
    idverificationdocumenttype= models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to='license/',blank= True,null= True) 
    country= models.CharField(max_length=255, blank=True, null=True)
    




class Profilecomplete5(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    abountme= models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    whatsapp = models.CharField(max_length=255, blank=True, null=True)
    imo = models.CharField(max_length=255, blank=True, null=True)
    fblink = models.CharField(max_length=255, blank=True, null=True)
    linkdin= models.CharField(max_length=255, blank=True, null=True)
    
    
    