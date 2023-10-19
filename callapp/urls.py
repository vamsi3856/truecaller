from django.urls import path
from . import views

urlpatterns = [
    path('',views.lookup,name="lookup"),
    path('truecaller/', views.truecaller_info, name='truecaller_info'),
]
