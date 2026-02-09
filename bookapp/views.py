from django.shortcuts import render
from .models import Readers
from .models import Books

# Create your views here.
def readers(request):
    myreaders=Readers.objects.all()
    context={'myreaders':myreaders}
    return render (request, 'readers.html', context)
def mybooks(request):
    mybooks=Books.objects.all()
    return render(request, 'books.html', {'mybooks':mybooks})
