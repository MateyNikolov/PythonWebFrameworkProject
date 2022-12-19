from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.template import loader
from rest_framework import response


def handler500(request, *args, **kwargs):
    template = loader.get_template('error_500.html')
    response.status_code = 500

    return HttpResponse(template.render({}, request))


def handler404(request, *args, **kwargs):
    template = loader.get_template('error_404.html')
    response.status_code = 404

    return HttpResponse(template.render({}, request))


def handler403(request, *args, **kwargs):
    template = loader.get_template('error_403.html')
    response.status_code = 403

    return HttpResponse(template.render({}, request))


