from django.urls import path
from .views import *
urlpatterns=[
    path('',SignUp.as_view()),
    path('mashq/',Mashq.as_view()),
    path('mavzu/',Mavzu.as_view()),
    path('comment/',Comments.as_view()),
    path('detail/<int:pk>/',DetailView.as_view())
]