from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import PollsList, ActivePolls, PollDetailView, PersonView, CreatePollResultView

urlpatterns = [
    # полный список опросов (прошедших и нет)
    path('polls', PollsList.as_view(), name='poll_list_url'),
    # полный список активных опросов
    path('active-polls', ActivePolls.as_view(), name='active_poll_list_url'),
    # по номеру опроса выводит его инфу для формирования фронтэнда ответа на опрос
    path('poll/<int:pk>', PollDetailView.as_view(), name='poll_url'),
    # по id юзера список его опросов (id юзера - его pk)
    path('person/<int:pk>', PersonView.as_view(), name='person_url'),
    # по id юзера (если не было такого id, создается новый юзер) создается ответ на опрос
    path('create-poll-result', CreatePollResultView.as_view(), name='new_poll_result_url'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)