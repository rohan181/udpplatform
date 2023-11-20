from django.urls import path

from . import apis

urlpatterns = [
    path('phone_signup/',apis.UserCreateAPIViewphone.as_view(), name='create-user'),
    path('email_signup/',apis.UserCreateAPIViewemail.as_view(), name='create-user'),


    path('email_otp/',apis.emailotp.as_view(), name='otp'),


    

   # path("register/", apis.RegisterApi.as_view(), name="register"),
    path("loginemail/", apis.LoginApi.as_view(), name="login"),
    path("loginphone/", apis.LoginApi1.as_view(), name="login"),
    path("me/", apis.UserApi.as_view(), name="me"),
    path("logout/", apis.LogoutApi.as_view(), name="logout"),


    path("create-profile1/",apis.CreateProfileAPIView.as_view(), name= "create_profile"),
    path("viewcreate-profile1/",apis.ViewCreateProfileAPIView.as_view(), name= "create_profile"),
   
    path('profilelocationbd/',apis.ProfilelocationbdCreateAPIView.as_view(), name='locationbd'),
    path('viewprofilelocationbd/',apis.viewProfilelocationbdCreateAPIView.as_view(), name='locationbd'),



    path('profilelocationabroad/',apis.ProfilelocationabroadCreateAPIView.as_view(), name='locationabroad'),
    path('viewprofilelocationabroad/',apis.viewProfilelocationabroadCreateAPIView.as_view(), name='locationabroad'),



    path('profileexperience/',apis.ProfileinfoexperienceCreateAPIView.as_view(), name='locationabroad'),
    path('viewprofileexperience/',apis.viewProfileinfoexperienceCreateAPIView.as_view(), name='locationabroad'),







     path('profilecomplete1/', apis.Profilecomplete1ListCreateView.as_view(), name='profilecomplete1-list-create'),
     path('viewprofilecomplete1/',apis.viewprofilecomplete1.as_view(), name='profilecomplete1-list-create'),
     
     
     path('profilecomplete2/', apis.Profilecomplete2ListCreateView.as_view(), name='profilecomplete1-list-create'),
     path('viewprofilecomplete2/',apis.viewprofilecomplete2.as_view(), name='profilecomplete1-list-create'),

     path('profilecomplete3/', apis.Profilecomplete3ListCreateView.as_view(), name='profilecomplete1-list-create'),
     path('viewprofilecomplete3/',apis.viewprofilecomplete3.as_view(), name='profilecomplete1-list-create'),


     path('profilecomplete4/', apis.Profilecomplete4ListCreateView.as_view(), name='profilecomplete1-list-create'),
     path('viewprofilecomplete4/',apis.viewprofilecomplete4.as_view(), name='profilecomplete1-list-create'),


     path('profilecomplete5/', apis.Profilecomplete5ListCreateView.as_view(), name='profilecomplete1-list-create'),
     path('viewprofilecomplete5/',apis.viewprofilecomplete5.as_view(), name='profilecomplete1-list-create'),




    #  path('profilecomplete2/', Profilecomplete2ListCreateView.as_view(), name='profilecomplete2-list-create'),
    #  path('profilecomplete3/', Profilecomplete3ListCreateView.as_view(), name='profilecomplete3-list-create'),
    #  path('profilecomplete4/', Profilecomplete4ListCreateView.as_view(), name='profilecomplete4-list-create'),
    #  path('profilecomplete5/', Profilecomplete5ListCreateView.as_view(), name='profilecomplete5-list-create'),
    
    
]
