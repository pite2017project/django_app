# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Event
from .utils import Calendar, Import
import datetime
import calendar
from django.utils.safestring import mark_safe
from django.urls import reverse
from .forms import EventForm, UploadFileFrom
from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    after_day = request.GET.get('day__gte', None)
    extra_context =  {}

    if not after_day:
        day = datetime.date.today()
    else:
        try:
            split_after_day = after_day.split('-')
            day = datetime.date(year=int(split_after_day[0]), month=int(split_after_day[1]), day=1)
        except:
            day = datetime.date.today()

    previous_month = datetime.date(year=day.year, month=day.month, day=1)
    previous_month -= datetime.timedelta(days=1)
    previous_month = datetime.date(year=previous_month.year, month=previous_month.month, day=1)

    last_day = calendar.monthrange(day.year, day.month)
    next_month = datetime.date(year=day.year, month=day.month, day=last_day[1])  # find last day of current month
    next_month = next_month + datetime.timedelta(days=1)  # forward a single day
    next_month = datetime.date(year=next_month.year, month=next_month.month,
                               day=1)  # find first day of next month

    extra_context['previous_month'] = '?day__gte=' + str(
       previous_month)
    extra_context['next_month'] = '?day__gte=' + str(next_month)
    cal = Calendar(request=request.get_full_path())
    extra_context['cos'] = request.get_full_path()
    html_calendar = cal.formatmonth(day.year, day.month, user=request.user, withyear=True)
    extra_context['calendar'] = mark_safe(html_calendar)

    extra_context['text'] = request.get_full_path()


    extra_context['message'] = request.session.get('info') or ''
    request.session['info'] = ''

    form = UploadFileFrom()
    extra_context['form'] = form

    return render(request, "kalendar/calendar.html", extra_context)


@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)


        if form.is_valid():
            obj = Event()
            obj.user = request.user
            obj.title = form.cleaned_data['title']
            obj.day = form.cleaned_data['day']
            obj.starting_time = form.cleaned_data['starting_time']
            obj.ending_time = form.cleaned_data['ending_time']
            obj.personal_notes = form.cleaned_data['personal_notes']
            obj.save()

            #text = '<div class="respond"><h3>You successfully added new event </h3></div>'

            return HttpResponseRedirect(reverse('index'))
    else:
        form = EventForm()
        form.fields['day'].initial = datetime.datetime.now()
    return render(request, "kalendar/addEvent.html", {'form':form})

@login_required
def modify_event(request, object_id):
    object = Event.objects.get(pk=object_id)
    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            object.user = request.user
            object.title = form.cleaned_data['title']
            object.day = form.cleaned_data['day']
            object.starting_time = form.cleaned_data['starting_time']
            object.ending_time = form.cleaned_data['ending_time']
            object.personal_notes = form.cleaned_data['personal_notes']
            object.save()

            #text = '<div class="respond"><h3>You successfully modified new event </h3></div>'

            return HttpResponseRedirect(reverse('index'))
    else:
        form = EventForm()
        form.fields['title'].initial = object.title
        form.fields['day'].initial = object.day
        form.fields['starting_time'].initial = object.starting_time
        form.fields['ending_time'].initial = object.ending_time
        form.fields['personal_notes'].initial = object.personal_notes

    return render(request, "kalendar/modifyEvent.html", {'form':form, 'id':object_id})


@login_required
def delete_event(request, object_id):
    Event.objects.filter(id=object_id).delete()

    return HttpResponseRedirect(reverse('index'))

@login_required
def all_event_list(request):
    objects = Event.objects.filter(user=request.user).order_by('day', 'starting_time')


    data = {'objects' : objects}

    return render(request, "kalendar/allEvents.html", data )

@login_required
def import_events_from_unitime(request):
    if request.method == 'POST':
        form = UploadFileFrom(request.POST, request.FILES)


        if form.is_valid():
            paramFile = request.FILES['file']

            imp = Import(form.cleaned_data['file'],paramFile, request.user )
            try:
                imp.check_right_name()
                imp.check_right_content()
                imp.save_events()
            except NameError:
                request.session['info'] = "The file must be csv type"
                return HttpResponseRedirect(reverse('index'))
            except IOError:
                request.session['info'] = 'The file includes wrong content'
                return HttpResponseRedirect(reverse('index'))
            except :
                request.session['info'] = 'Undefined error occur, not all records has been saved'
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponseRedirect(reverse('index'))

    else:
        return HttpResponseRedirect(reverse('index'))