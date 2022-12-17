from django.urls import path
from portfolio.views import portfolio_view,portfolio_galview
app_name='portfolio'

urlpatterns=[
    path('details/<int:did>',portfolio_view,name='details'),
    path('<int:pid>',portfolio_galview,name='gallery'),
]