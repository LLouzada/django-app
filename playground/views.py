from django.shortcuts import render

# Create your views here.
# request -> response
# request handler
# action

from django.http import HttpResponse

def say_hello(request):
    # Pull data
    # Transform data
    # Send email/data
    # return HttpResponse('Hello World!')
    return render(request, 'hello.html', { 'name': 'LLouzada'})
