from django.shortcuts import render
from portfolio.models import Collection
from website.forms import contactform
from django.contrib import messages
from website.models import CV,Artist_statement

def index_view(request):

    collections=Collection.objects.all()
    cv=CV.objects.last()

    if request.method=='POST':
        form=contactform(request.POST)
        if form.is_valid():
            result=form
            result.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your ticket did not submited')
    form=contactform()

    context={'collections':collections,'form':form,'cv':cv}
    return render(request,'website/index.html',context)

def as_view(request):

    statement=Artist_statement.objects.last()
    context={'statement':statement}

    return render(request,'website/as.html',context)

# def contact_view(request):
#     if request.method=='POST':
#         form=contactform(request.POST)
#         if form.is_valid():
#             name=form.cleaned_data['name']
#             result=form.save(commit=False)
#             result.name='unknown'
#             result.save()
#             messages.add_message(request,messages.SUCCESS,'your ticket submited successfully')
#         else:
#             messages.add_message(request,messages.ERROR,'your ticket did not submited')
#     form=contactform()

#     return render(request,"website/index.html",{'form':form})

# Create your views here.
