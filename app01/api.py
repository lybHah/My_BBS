# -*- coding:utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib import auth
from django.http import JsonResponse
import datetime
import models


