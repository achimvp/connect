from django.urls import path
from .views import EntryListView

urlpatterns = [
    path('map/', EntryListView.as_view()),
]