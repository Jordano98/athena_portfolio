from django.urls import path
from portfolio.views import portfolio_view
app_name='portfolio'

urlpatterns=[
    path('details/',portfolio_view,name='index'),
]