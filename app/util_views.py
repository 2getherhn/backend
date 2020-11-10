import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.shortcuts import redirect
from django.conf import settings

logger = logging.getLogger('together')

def healthcheck(request):
    try:
        return HttpResponse(status=200)
    except Exception as ex:
        logger.error(str(ex))
        raise ex

