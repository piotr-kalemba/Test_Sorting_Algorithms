"""Sorting_Algorithms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
import Test_Sorting.views as views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^algorithms/', views.AllAlgTestView.as_view(), name="algorithms"),
    url(r'^algorithm/', views.SingleAlgTestView.as_view(), name="algorithm"),
    url(r'^tests', views.TestsView.as_view(), name="tests"),
    url(r'^login', views.LoginUser.as_view(), name="login"),
    url(r'^create_user', views.CreateUser.as_view(), name="create-user"),
    url(r'^all_test_view/(?P<pk>(\d)+)', views.AllAlgTestTable.as_view(), name="all-test-view"),
    url(r'^single_test_view/(?P<pk>(\d)+)', views.SingleAlgTestTable.as_view(), name="single-test-view"),
    url(r'', views.WelcomeView.as_view(), name="welcome-view"),
]