import sys
import logging
import json

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, QueryDict, JsonResponse
from django.contrib import messages

from app.forms import ShelterForm
from app.models import TempData
from app.services.ShelterService import ShelterService
from app.exceptions import *
from together import settings

logger = logging.getLogger("together")
USER_LOGIN_URL = "/login"


# home view
def home_view(request):
    return render(request, 'home.html')


# @login_required(login_url=settings.USER_LOGIN_URL)
# @permission_required('app.add_reservation')
# @permission_required('app.change_reservation')
def save_shelter(request):
    shelter_number = ""
    if request.method == 'POST':
        form = ShelterForm(request.POST or None)
        if form.is_valid():
            data = form.cleaned_data
            case_id = data['case_id']
            try:
                ShelterService.save_request(request, data)
                return redirect('/view/' + case_id)
            except SavingException as err:
                logger.error("Error saving request: %s" % str(err))
                return HttpResponse("Error saving request")
        else:
            for field in form:
                if field.errors:
                    logger.error("form field error: FIELD = %s" % field.name)
                for error in field.errors:
                    messages.add_message(request, messages.ERROR, "%s :  %s " % (str(error), field.label))
                    logger.error("form field error: %s = %s " % (field.label, str(error)))
                logger.error(form.errors)

    if request.method == 'GET':
        shelter_number = ShelterService.generate_shelter_number()

    return render(request, 'shelter.html', {
        'shelter_number': shelter_number,
        'current_status': 'PENDING',
        'data': TempData
    })


def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if request.method == 'POST':
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'incorrect username or password')
    return render(request, 'login.html')
