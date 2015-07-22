from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import models


def index(request):
    bbs_list = models.BBS.objects.all()
    return render_to_response('index.html', {'bbs_list': bbs_list})


def bbs_detail(request, bbs_id):
    bbs = models.BBS.objects.get(id=bbs_id)
    return render_to_response('bbs_detail.html', {'bbs_obj': bbs})