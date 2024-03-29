from django.urls import path
from . import views

# urlpatterns = [
#     path('members/', views.members, name="members"),
# ]

urlpatterns = [
    path('members_new', views.members, name='members'),
    path('author', views.author, name='authors'),
    path('view_all', views.mymembers2, name='viewall'),
    path('books', views.book, name='book'),
    path('lists_books_author', views.listsofbooks, name='list_books_author'),
    path('listsofauthor', views.listsofauthors, name='list_author'),
    path('chart_new', views.charts, name='chart')
    # path('lent',    views.lentz, name='lent')
]
