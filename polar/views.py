from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, JsonResponse

from django.utils.html import strip_tags

from .models import Query

from .news import buildSources

from .forms import QueryForm

import json, re

def index(request):
    # sources = get_object_or_404(buildSources, pk=question_id)
    # return render(request, 'polar/index.html', {'sources': sources})
    context = {'form': QueryForm() }
    return render(request, 'polar/index.html', context)
    # return HttpResponse("You're looking at the index.")

def latest(request):
    return HttpResponse("You're looking at the latest.")

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def build(request):
    response_data = {}
    text = "trump fake"
    response_data = buildSources(text)

    return JsonResponse(response_data)


    # return HttpResponse(
    #     json.dumps(response_data),
    #     content_type="application/json"
    # )

def query_polar(request):
    if request.method == 'POST':
        query_text = strip_tags(request.POST.get('query'))
        query_text = re.sub(r'\W|_', ' ', query_text)
        response_data = {}

        query = Query(query = query_text)
        query.save()

        response_data['query_text'] = query_text
        response_data['results'] = buildSources(query_text)


        return JsonResponse(response_data)
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
