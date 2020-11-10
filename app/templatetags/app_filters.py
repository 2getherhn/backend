import os
from datetime import datetime, timedelta
from django import template
from django.template.defaultfilters import stringfilter
from app.utils import long_ago
from app.models import TempData
import pytz
import json
register = template.Library()


REQUISITION_STATUS = {
	'PENDING': {
		'text': 'Nueva solicitud de insumos',
		'css': 'secondary'
	},
	'SUPPLY_PROPOSED': {
		'text': 'Tiene una nueva oferta de insumos',
		'css': 'success'
	},
	'SUPPLY_ACCEPTED': {
		'text': 'La oferta de insumos fue aceptada',
		'css': 'primary'
	},
	'DELIVERY_SCHEDULED': {
		'text': 'La entrega esta programada',
		'css': 'warning'
	},
	'PAUSED': {
		'text': 'Todas las acciones estan detenidas sobre la solicitud',
		'css': 'secondary'
	},
	'COMPLETED': {
		'text': 'Se entregaron todos los insumos solicitados!',
		'css': 'success'
	},
	'CANCELLED': {
		'text': 'La solicitud fue cancelada',
		'css': 'danger'
	}
}


@register.filter()
def case_status_text(str_status):
	if str_status:
		if str_status in REQUISITION_STATUS:
			return REQUISITION_STATUS[str_status]['text']
	return ""


@register.filter()
def case_status_class(str_status):
	if str_status:
		if str_status in REQUISITION_STATUS:
			return REQUISITION_STATUS[str_status]['css']
	return ""


@register.filter()
def format_date(str_date):
	try:
		return datetime.strptime(str(str_date), "%Y-%m-%d").strftime("%m/%d/%Y")
	except ValueError:
		return ""


@register.filter()
def format_date_ymd(str_date):
	try:
		return datetime.strptime(str(str_date), "%Y-%m-%d").strftime("%Y-%m-%d")
	except ValueError:
		return ""


@register.filter()
def format_datetime(value):
	return value.strftime("%m/%d/%Y %I:%M %p")


@register.filter()
def relative_time(obj):
	now = datetime.now(tz=None)
	naive = obj.replace(tzinfo=None)
	return long_ago((now - naive).total_seconds())


@register.filter()
def format_bool(val):
	if val:
		return "SI"
	return "NO"


@register.filter()
def format_none(val):
	if val is None:
		return ""
	return val


@register.filter()
def scheduling_success_value(current_status):
	if current_status == "SUPPLY_PROPOSED":
		return "30%"
	if current_status == "SUPPLY_ACCEPTED":
		return "60%"
	if current_status == "DELIVERY_SCHEDULED":
		return "80%"
	if current_status == "COMPLETED":
		return "100%"
	if current_status == "PAUSED" or current_status == "CANCELLED":
		return "0%"
	return "10%"

