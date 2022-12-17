from portfolio.models import Project,Collection
from django.shortcuts import redirect, render


def portfolio_galview(request,pid):

    projects=Project.objects.filter(collection_name_id=pid)
    collection=Collection.objects.get(col_name_id=pid)

    context={'projects':projects,'collection':collection }
    print(collection)
    return render(request,'portfolio/portfolio-gal.html',context)

def portfolio_view(request,did):

    #detail=Project.objects.filter(id=did)
    detail=Project.objects.get(id=did)
    
    nextpost = Project.objects.filter(created_date__gt=detail.created_date).order_by('created_date').first()
    prevpost = Project.objects.filter(created_date__lt=detail.created_date).order_by('created_date').last()


    context={'prevpost': prevpost , 'nextpost' : nextpost ,'detail':detail}
    return render(request,'portfolio/portfolio-single-3.html',context)
# Create your views here.
