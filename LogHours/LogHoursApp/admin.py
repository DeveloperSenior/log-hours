from django.contrib import admin

# Register your models here.
from LogHoursApp.models import Enterprises, Charges, Projects, Statuses, LogHours, Priority


@admin.register(Enterprises)
class EnterprisesAdmin(admin.ModelAdmin):
    list_display = ("id", "description")

    def id(self, obj):
        return obj.id

    id.short_description = 'ID'

    def description(self, obj):
        return obj.dsNameEnterprise

    description.short_description = 'Nombre Empresa'


@admin.register(Charges)
class ChargesAdmin(admin.ModelAdmin):
    list_display = ("id", "description")

    def id(self, obj):
        return obj.id

    id.short_description = 'ID'

    def description(self, obj):
        return obj.dsNameCharge

    description.short_description = 'Nombre Cargo'


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "owner", "priority", "status")

    def id(self, obj):
        return obj.id

    id.short_description = 'ID'

    def description(self, obj):
        return obj.dsNameProject

    description.short_description = 'Nombre Proyecto'

    def owner(self, obj):
        return obj.dsOwner

    owner.short_description = 'Dueño Proyecto'

    def priority(self, obj):
        return obj.dsPriority

    priority.short_description = 'Prioridad'

    def status(self, obj):
        return obj.idStatus

    status.short_description = 'Estado'


@admin.register(Statuses)
class StatusesAdmin(admin.ModelAdmin):
    list_display = ("id", "description")

    def id(self, obj):
        return obj.id

    id.short_description = 'ID'

    def description(self, obj):
        return obj.dsNameStatus

    description.short_description = 'Estado'


@admin.register(Priority)
class StatusesAdmin(admin.ModelAdmin):
    list_display = ("id", "description")

    def id(self, obj):
        return obj.id

    id.short_description = 'ID'

    def description(self, obj):
        return obj.dsNamePriority

    description.short_description = 'Prioridad'


@admin.register(LogHours)
class LogHoursAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "priority", "business_hour", "not_business_hour","date_hour")

    def id(self, obj):
        return obj.id

    id.short_description = 'ID'

    def description(self, obj):
        return obj.dsActivity

    description.short_description = 'Actividad'

    def priority(self, obj):
        return obj.dsPriority

    priority.short_description = 'Prioridad'

    def business_hour(self, obj):
        return obj.nmBusinessHour

    business_hour.short_description = 'Horas'

    def not_business_hour(self, obj):
        return obj.nmNoBusinessHour

    not_business_hour.short_description = 'Horas extras'

    def date_hour(self, obj):
        return obj.date

    date_hour.short_description = 'Fecha registro'

