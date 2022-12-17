from django.shortcuts import render
from portfolio.models import Collection

def index_view(request):

    collections=Collection.objects.all()

    context={'collections':collections}
    return render(request,'website/index.html',context)

# Create your views here.
