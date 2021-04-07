from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import PollList, ActivePolls, PersonView, PollView, CreateAnswer

urlpatterns = [
    # полный список опросов (прошедших и нет)
    path('polls', PollList.as_view(), name='poll_list_url'),
    # полный список активных опросов
    path('active-polls', ActivePolls.as_view(), name='active_poll_list_url'),
    # по id юзера список его опросов (id юзера - его pk)
    path('person/<int:pk>', PersonView.as_view(), name='person_url'),
    # по номеру опроса выводит его инфу для формирования фронтэнда ответа на опрос
    path('poll/<int:pk>', PollView.as_view(), name='poll_url'),
    # по id юзера (если не было такого id, создается новый юзер) создается ответ на опрос
    path('answer/<int:poll>/<int:usr>', CreateAnswer.as_view(), name='new_answer_url'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)