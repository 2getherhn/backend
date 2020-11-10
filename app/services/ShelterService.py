import sys
import logging
import random
import string
# import traceback
from django.db import transaction
from app.models import Shelter
from app.exceptions import *

logger = logging.getLogger("together")


class ShelterService:
    """
    Handles main request operations
    """

    @staticmethod
    def generate_shelter_number(letters_count=6, digits_count=6):
        sample_str = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
        sample_str += ''.join((random.choice(string.digits) for i in range(digits_count)))

        # Convert string to list and shuffle it to mix letters and digits
        sample_list = list(sample_str)
        random.shuffle(sample_list)
        ret = ''.join(sample_list).upper()
        return ret[0:4] + "-" + ret[4:8]

    @staticmethod
    def save_request(request, form_data):
        with transaction.atomic():
            is_update = False
            try:
                # update existing reservation
                shelter = Shelter.objects.get(number=form_data['number'])

                # changed_by
                shelter.updated_by = request.user.username

                is_update = True
            except Shelter.DoesNotExist:
                # create a reservation
                shelter = Shelter()
                shelter.shelter_number = form_data['shelter_number']
                shelter.name = form_data['name']
                shelter.created_by = request.user.username
            finally:
                try:
                    shelter.save()
                except Exception as err:
                    logger.error(str(err))
                    raise SavingException("Error saving shelter:" + str(err))
