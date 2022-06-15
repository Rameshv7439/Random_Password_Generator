"""Password_Generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Generator_app import views
from Generator_app.views import IndexView, RegistrationView, Login, RejectView, Forgot_Password
from Generator_app import user_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view()),
    # path('password_generate',Password_Generate.as_view()),
    path('password/', views.password, name= 'password'),
    path('password2/', views.password2, name= 'password2'),
    path('password1/', views.password1, name= 'password1'),
    path('generator/', views.generator, name = 'generator'),
    path('generator3/', views.generator3, name = 'generator3'),
    path('generator2/', views.generator2, name = 'generator2'),
    path('view_password',views.View_Password, name='View_Password'),
    path('registration',RegistrationView.as_view()),
    path('login',views.Login, name='login'),
    path('user/',user_urls.urls()),
    path('generator1/', views.generator1, name = 'generator1'),
    path('remove',RejectView.as_view()),
    path('forgot_password',Forgot_Password.as_view())



]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
