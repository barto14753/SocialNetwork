from django.http.response import HttpResponse, HttpResponseServerError, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View
from home.models import User
from home.views import getUser
from django.template import RequestContext, context
import json


def requests_view(request):
    if request.method == 'GET':
        user_username = request.user.username
        user = get_object_or_404(User, username=user_username)
        received_requests = user.get_received_requests()
        sent_requests = user.get_sent_requests()
        received_requests_count = len(received_requests)
        sent_requests_count = len(sent_requests)
        context = {
            'received_requests': received_requests,
            'received_requests_count': received_requests_count,
            'sent_requests': sent_requests,
            'sent_requests_count': sent_requests_count,
        }

        return render(request, 'requests.html', context=context)
