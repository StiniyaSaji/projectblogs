from django.urls import path

from newproject import views

urlpatterns = [
    path('',views.Userlogin),
    path('register',views.UserRegister),
    path('logout/',views.Userlogout),
    path('dashboard',views.home),
    path('verify',views.ForgotPassword),
    path('reset',views.ResetPassword),
    path('changepass',views.Change_password),
    path('propic',views.upload_image),
    path('create',views.CreateBlog),
    path('view', views.ViewBlog),
    path('details/<int:id>',views.View_details),
    path('delete/<int:id>',views.DeleteBlog),
    path('update/<int:id>',views.UpdateBlog),
    path('createpro',views.CreateProfile),
    path('viewpro', views.ViewProfile),
    path('editpro',views.EditProfile),
    path('profilepic',views.upload_image),

]
