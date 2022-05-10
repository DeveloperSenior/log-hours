from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Enterprises(models.Model):
    id = models.AutoField(primary_key=True)
    dsNameEnterprise = models.CharField(max_length=45, verbose_name="Nombre Empresa",
                                        help_text="Ingrese nombre de la empresa máximo 45 caracteres")

    def __str__(self):
        return self.dsNameEnterprise

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"


class Charges(models.Model):
    id = models.AutoField(primary_key=True)
    dsNameCharge = models.CharField(max_length=45, verbose_name="Nombre Cargo",
                                    help_text="Ingrese nombre del cargo máximo 45 caracteres")

    def __str__(self):
        return self.dsNameCharge

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"


class Statuses(models.Model):
    id = models.AutoField(primary_key=True)
    dsNameStatus = models.CharField(max_length=24, verbose_name="Estado",
                                    help_text="Ingrese nombre del estado máximo 24 caracteres")

    def __str__(self):
        return self.dsNameStatus

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"


class Priority(models.Model):
    id = models.AutoField(primary_key=True)
    dsNamePriority = models.CharField(max_length=10, verbose_name="Prioridad",
                                    help_text="Ingrese nombre de la prioridad máximo 10 caracteres")

    def __str__(self):
        return self.dsNamePriority

    class Meta:
        verbose_name = "Prioridad"
        verbose_name_plural = "Prioridades"


class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    dsNameProject = models.CharField(max_length=45, verbose_name="Nombre Proyecto",
                                     help_text="Ingrese nombre del proyecto máximo 45 caracteres")
    dsOwner = models.CharField(max_length=45, verbose_name="Dueño Proyecto",
                               help_text="Ingrese dueño del proyecto máximo 45 caracteres")
    dsPriority = models.CharField(max_length=45, verbose_name="Prioridad",
                                  help_text="Ingrese prioridad del proyecto máximo 45 caracteres")
    idStatus = models.OneToOneField(Statuses, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"


class LogHours(models.Model):
    id = models.AutoField(primary_key=True)
    dsActivity = models.CharField(max_length=200, verbose_name="Actividad",
                                  help_text="Actividad realizada máximo 200 caracteres")
    dsPriority = models.ForeignKey(Priority, on_delete=models.CASCADE, verbose_name="Prioridad")
    nmBusinessHour = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Hora laboral",
                                         help_text="Ingrese hora laboral maximo 8 caracteres")
    nmNoBusinessHour = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Hora no laboral",
                                           help_text="Ingrese hora no laboral maximo 8 caracteres")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    date = models.DateTimeField(auto_now=True, blank=True, verbose_name="Fecha registro",
                                help_text="Ingresa la fecha de registro/actualización")

    class Meta:
        verbose_name = "Resgistro de horas"
        verbose_name_plural = "Resgistro de horas"
