from django.contrib import admin
from .models import Poll, Variant, Answer
# Register your models here.


class VariantInLine(admin.StackedInline):
    model = Variant
    extra = 2


@admin.register(Poll)
class PollAdmin (admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'question_text', 'attribute')
    inlines = [VariantInLine]


@admin.register(Variant)
class VariantAdmin (admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin (admin.ModelAdmin):
    pass