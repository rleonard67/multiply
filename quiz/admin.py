from django.contrib import admin
from multiply.models import Quizzes

class QuizzesAdmin(admin.ModelAdmin):
    pass

admin.site.register(QuizzesAdmin)
