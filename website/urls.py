from django.urls import path
from website.views import index_view,contact_view

app_name='website'

urlpatterns=[
    path('',index_view,name='index'),
    path('contact/',contact_view,name="contact"),
]