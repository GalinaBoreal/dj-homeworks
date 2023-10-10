from django.urls import path
from django.contrib import admin

from measurement.views import SensorListCreate, MeasurementCreate, SensorRetrieveUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', SensorListCreate.as_view()),
    path('measurements/', MeasurementCreate.as_view()),
    path('sensors/<pk>/', SensorRetrieveUpdate.as_view()),
]
