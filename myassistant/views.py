# views.py

from django.http import HttpResponse
from django.template.loader import render_to_string

def home_view(request):
    # Generate an HTML string with an h1 tag
    HTML_STRING = "<h1>Hello Malika</h1>"

    # Return the HTML as a response
    return HttpResponse(HTML_STRING)
