from django.contrib import admin
from django.urls import path,re_path
from Demo_App import views as da

urlpatterns = [
    path("homepage/",da.HomePage),
    path("loginpage/",da.LoginPage),
    path("template/",da.TemplateTest),
    path("test/",da.indexing),
    path("base/",da.BasePage),
    path("register/",da.registerPage),
    path("demopage/",da.DemoPage),
    path("delete/<int:id>",da.deleterec),
    path("update/<int:id>",da.updatepage),
    path("login/",da.loginform),
    #re_path(r'^delete/(?P<id>\d+)/$',da.deleterec)
]