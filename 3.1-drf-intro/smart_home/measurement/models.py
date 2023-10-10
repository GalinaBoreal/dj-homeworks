from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Датчик')
    description = models.CharField(max_length=100)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата измерения')
    photo = models.ImageField(null=True, verbose_name='Изображение')
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="measurements")
    objects = models.Manager()

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
