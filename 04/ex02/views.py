from django.shortcuts import render
from .form import MyForm
from django.http import HttpResponse
import datetime
from django.shortcuts import redirect

def form(request):

    message = ""
    if(request.method == 'POST'):
        form = MyForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            timestamp=datetime.datetime.now()
            log = open('message.log', 'a')
            log.write (str(timestamp) + " message: " + message + "\n")
            log.close()
        return redirect("form")
    else:
        form = MyForm()
    try:
        message = open ('message.log', 'r')
        history = message.readlines()        
    except:
        history = ""

    return render(request, 'ex02/form.html',{'form': form, 'message': history})