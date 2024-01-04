from django.urls import path
from . import views

# urlpatterns = [
#     path('members/', views.members, name="members"),
# ]

urlpatterns = [
    path('members/', views.members, name='members'),
    # path('show/',views.show,name='show'),
    path('viewall/', views.mymembers2, name='viewall')
]
