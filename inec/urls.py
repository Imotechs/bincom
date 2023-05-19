from django.urls import path
from inec.views import (
    home,PollDetailView,local_gov_results,search,new_polling_unit
)
urlpatterns = [
    path('', home,name='home'),
    path('poll/unit/<int:pk>/',PollDetailView.as_view(),name='detail'),
    path('local/govt/result/',local_gov_results,name = 'results'),
    path('search/',search, name = 'search'),
    path('add/new/unit/',new_polling_unit,name = 'new_unit')


]
