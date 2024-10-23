from django.db.models.options import Options
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet
import csv

class ExportAsCSVMixin:
    def export_csv(self, request: HttpRequest, queryset: QuerySet):
        meta: Options = self.model._meta
        fields_name = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Description'] = f'attachment; filename={meta}-export.csv'

        csv_writer = csv.writer(response)
        csv_writer.writerow(fields_name)
        for obj in queryset:
            csv_writer.writerow([getattr(obj, field) for field in fields_name])

        return response

    export_csv.short_description = 'Export as csv'