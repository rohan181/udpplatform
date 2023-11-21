from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(
        self,
        firstname,
        lastname,
        user_type,
        email=None,
        street=None,
        city=None,
        state=None,
        zip_code=None,
        parent_user =None,
        password=None,
        is_active=True,
        is_staff=False,
        is_superuser=False,
    ):
       
        if not  firstname:
            raise ValueError("User must have a full name")
       
        user = self.model(
            email=self.normalize_email(email) if email else None,
           
            firstname= firstname,
            lastname=lastname,
            user_type= user_type,
            street=street,
            city=city,
            state=state,
            zip_code=zip_code,
            parent_user =parent_user ,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser
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

    def __str__(self):
        return f"{self.firstname} {self.lastname}" if self.firstname and self.lastname else self.email

    




