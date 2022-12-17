from django.shortcuts import render
from portfolio.models import Collection
from website.forms import contactform
from django.contrib import messages

def index_view(request):

    collections=Collection.objects.all()

    if request.method=='POST':
        form=contactform(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            result=form.save(commit=False)
            result.name='unknown'
            result.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your ticket did not submited')
    form=contactform()

    context={'collections':collections,'form':form}
    return render(request,'website/index.html',context)

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
