# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    test = "Test"

    return render_to_response('main/index.html', {'test': test},
            context_instance=RequestContext(request))
