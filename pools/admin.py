from django.contrib import admin
from .models import Poll, Variant, Answer, Person
# Register your models here.


class VariantInLine(admin.StackedInline):
    model = Variant
    extra = 2
    fields = ['variant', 'poll']


@admin.register(Poll)
class PollAdmin (admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'question_text', 'attribute', 'pk')
    inlines = [VariantInLine]


@admin.register(Variant)
class VariantAdmin (admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin (admin.ModelAdmin):
    list_display = ('answer_text', 'usr', 'poll')


@admin.register(Person)
class PersonAdmin (admin.ModelAdmin):
    pass

