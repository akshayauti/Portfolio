from django.urls import path
from portfolio import views

app_name = "portfolio"

urlpatterns = [
    path('',views.index,name = 'index'),
    path('about/',views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('work/',views.work, name = 'work'),
]
