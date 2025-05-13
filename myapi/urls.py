from django.urls import path
from .views import *


urlpatterns=[

    path("",home_view, name="home"),
    path("details",banklist_view, name="banklist"),
    path("details/branches/<str:bank>", branches_view, name="branches"),
    path("details/branchdetails/<str:ifsc>",branch_details_view, name="branchdetails")
    
    
]