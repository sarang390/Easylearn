"""
URL configuration for Easylearn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from Myapp import views

urlpatterns = [
    path('login/',views.login),
    path('login_post/',views.login_post),
    path('forgotpswd/',views.forgot),
    path('forgotpswd_post/',views.forgot_post),
    path('home/',views.home),
    path('homepage/',views.homepage),
    path('adminchangepwd/',views.admin_change_password),
    path('adminchangepwd_post/',views.admin_change_password_post),
    path('sentreply/<id>',views.sent_reply),
    path('sentreply_post/',views.sent_reply_post),
    path('viewreview/',views.view_reviews),
    path('viewreview_post/',views.view_reviews_post),
    path('viewcomplaints/',views.view_complaints),
    path('viewcomplaints_post/',views.view_complaints_post),
    path('viewusers/',views.view_users),
    path('viewusers_post/',views.view_users_post),


#     user

    path('userchangepwd/',views.user_change_password),
    path('userchangepwd_post/',views.user_change_password_post),
    path('editprofile/',views.edit_profile),
    path('editprofile_post/',views.edit_profile_post),
    path('qnageneration/',views.QnA_generation),
    path('qnageneration_post/',views.QnA_generation_post),
    path('sentreview/',views.Sent_review),
    path('sentreview_post/',views.Sent_reviews_post),
    path('sentcomplaint/',views.Sent_complaint),
    path('sentcomplaint_post/',views.Sent_complaint_post),
    path('signup/',views.Signup),
    path('signup_post/',views.Signup_post),
    path('viewqna/',views.View_QnA),
    path('userhome/',views.User_home),
    path('viewprofile/',views.View_profile),
    path('viewreply/',views.View_reply),
    path('viewreply_post/',views.View_reply_post),
    path('logout/',views.logout)

]
