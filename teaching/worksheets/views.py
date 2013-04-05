# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    context = RequestContext(request, {})
    return render_to_response('worksheets/home.html', context)