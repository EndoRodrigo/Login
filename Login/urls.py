#Django
from django.contrib import admin
from django.urls import path
from inicio import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='Login'),
    path('index', views.contenido, name='Contenido'),

]
