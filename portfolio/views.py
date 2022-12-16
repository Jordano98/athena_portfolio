from django.shortcuts import render


def portfolio_view(request):
    return render(request,'portfolio/portfolio-single-3.html')

def portfolio_galview(request):
    return render(request,'portfolio/portfolio-gal.html')
# Create your views here.
