from django.urls import path
from portfolio.views import portfolio_view,portfolio_galview
app_name='portfolio'

urlpatterns=[
    path('details/',portfolio_view,name='details'),
    path('gallery/',portfolio_galview,name='gallery'),
]