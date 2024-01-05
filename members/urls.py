from django.urls import path
from . import views

# urlpatterns = [
#     path('members/', views.members, name="members"),
# ]

urlpatterns = [
    path('members_new', views.members, name='members'),
    path('view_all', views.mymembers2, name='viewall'),
    path('books', views.book, name='book')
]
