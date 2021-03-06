from .models import *
from django.contrib import admin


class ConnectorQuestionnaireAdmin(admin.ModelAdmin):
        list_display = ('name',)
        class Meta:
                verbose_name = 'connector'


admin.site.register(ConnectorQuestionnaire, ConnectorQuestionnaireAdmin)
