from django.contrib import admin
from .models import Poll, QVariant, Question, Person, PollResultQuestion, Answer, PollResult


# Register your models here.


class QuestionInLine(admin.StackedInline):
    model = Question
    extra = 2
    fields = ['question_text', 'attribute']


class QVariantInLine(admin.StackedInline):
    model = QVariant
    extra = 1
    fields = ['q_variant_text']


@admin.register(Poll)
class PollAdmin (admin.ModelAdmin):
    list_display = ('pk', 'name', 'start_date', 'end_date')
    inlines = [QuestionInLine]


@admin.register(Question)
class QuestionAdmin (admin.ModelAdmin):
    list_display = ('question_text', 'attribute')
    inlines = [QVariantInLine]


@admin.register(QVariant)
class QVariantAdmin (admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin (admin.ModelAdmin):
    pass


class PollResultQuestionInLine (admin.StackedInline):
    model = PollResultQuestion
    fields = ['question_text']
    extra = 1


class AnswerInLine (admin.StackedInline):
    model = Answer
    fields = ['answer_text']
    extra = 1


@admin.register(PollResult)
class PollResultAdmin (admin.ModelAdmin):
    list_display = ('pk', 'poll_result_name', 'usr', 'poll')
    inlines = [PollResultQuestionInLine]


@admin.register(PollResultQuestion)
class PollResultQuestionInLine (admin.ModelAdmin):
    list_display = ('pk', 'question_text')
    inlines = [AnswerInLine]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass

