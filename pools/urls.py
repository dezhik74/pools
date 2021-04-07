from django.urls import path
from .views import PollList, ActivePolls

urlpatterns = [
    path('polls', PollList.as_view(), name='poll_list_url'),
    path('active-polls', ActivePolls.as_view(), name='active_poll_list_url'),
]