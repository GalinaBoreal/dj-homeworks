from django.urls import path
from django.contrib import admin

from school.views import students_list

urlpatterns = [
    path('', students_list, name='students'),
    path('admin/', admin.site.urls),
]