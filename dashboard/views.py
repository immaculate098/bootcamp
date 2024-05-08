from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.template import loader

from django.contrib.auth.decorators import login_required

from.models import Sitter, Payment, Baby


@login_required
def dashboard(request):
    count_sitters = Sitter.objects.count()
    count_babies = Payment.objects.count()
    count_departure = Baby.objects.count()
    context = {
        "count_sitters": count_sitters,
        "count_babies": count_babies,
        "count_departure": count_departure,
    }
    template = loader.get_template("dashboard.html")
    return HttpResponse(template.render(context))