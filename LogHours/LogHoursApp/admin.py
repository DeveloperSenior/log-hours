from django.contrib import admin
import csv
from django.http import HttpResponse

# Register your models here.
from LogHoursApp.models import Enterprises, Charges, Projects, Statuses, LogHours, Priorities, ChargesUser, \
    EnterprisesUser


class ExportCsv:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Exportar selección (CSV)"


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
        return obj.owner

    owner.short_description = 'Dueño Proyecto'

    def priority(self, obj):
        return obj.priority

    priority.short_description = 'Prioridad'

    def status(self, obj):
        return obj.status

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


@admin.register(Priorities)
class PrioritiesAdmin(admin.ModelAdmin):
    list_display = ("id", "description")

    def id(self, obj):
        return obj.id

    id.short_description = 'ID'

    def description(self, obj):
        return obj.dsNamePriority

    description.short_description = 'Prioridad'


@admin.register(LogHours)
class LogHoursAdmin(admin.ModelAdmin, ExportCsv):
    list_display = ("id", "description", "project", "priority", "business_hour", "not_business_hour", "date_hour")

    def id(self, obj):
        return obj.id

    id.short_description = 'ID'

    def description(self, obj):
        return obj.dsActivity

    description.short_description = 'Actividad'

    def project(self, obj):
        return obj.project

    project.short_description = 'Proyecto'

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

    actions = ["export_as_csv"]


@admin.register(ChargesUser)
class ChargesUserAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "charge")

    def id(self, obj):
        return obj.id

    id.short_description = 'ID'

    def user(self, obj):
        return obj.user

    user.short_description = 'Usuario'

    def charge(self, obj):
        return obj.charge

    charge.short_description = 'Cargo'


@admin.register(EnterprisesUser)
class EnterprisesUserAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "enterprise")

    def id(self, obj):
        return obj.id

    id.short_description = 'ID'

    def user(self, obj):
        return obj.user

    user.short_description = 'Usuario'

    def enterprise(self, obj):
        return obj.enterprise

    enterprise.short_description = 'Empresa'
