
from django.urls import path
from Generator_app import user_views
from Generator_app.user_views import IndexView


urlpatterns = [
    path('', user_views.IndexView),
    path('password/', user_views.password, name= 'password'),
    path('generator/', user_views.generator, name = 'generator'),
    path('view_password',user_views.View_Password, name='View_Password'),

]
def urls():
    return urlpatterns, 'user', 'user'