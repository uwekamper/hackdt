# Create your views here.
from django.core.urlresolvers import reverse
from django.http import Http404
from django.http.response import HttpResponseForbidden
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from evernote.api.client import EvernoteClient
from rest_framework import generics
from serializers import *
from models import *
from forms import WebHookForm
import evernote.edam.type.ttypes as Types

def home(request):
    context = RequestContext(request, {})
    return render_to_response('worksheets/home.html', context)


class TeacherList(generics.ListAPIView):
    model = User
    serializer_class = TeacherSerializer


class TeacherDetails(generics.RetrieveUpdateAPIView):
    slug_field = 'username'
    model = User
    serializer_class = TeacherSerializer


class StudentList(generics.ListCreateAPIView):
    model = Student
    serializer_class = StudentSerializer


class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    model = Student
    serializer_class = StudentSerializer





def overlord_webhook(request):
    #http[s]://[your base URL][? |&]userId=[evernoteUserId]&guid=[noteGuid]&reason=[create | update]
    if request.method == 'GET':
        form = WebHookForm(request.GET)
        if form.is_valid():
            print("%s, %s %s") % (form.cleaned_data['userId'], form.cleaned_data['guid'], form.cleaned_data['reason'])
            if form.cleaned_data['reason'] == 'create':
                client = get_evernote_client()
                note_store = client.get_note_store()
                # note = note_store.getNote(guid=form.cleaned_data['guid'])
                taglist = note_store.getNoteTagNames(guid=form.cleaned_data['guid'])
                print "Taglist: ", taglist
                if "overlord" in taglist:
                    overlord = Overlord.objects.get(pk=1)
                    overlord.is_angry = True
                    overlord.save()

    return render_to_response('worksheets/overlord_webhook.html', {})

def overlord(request):
    overlord = Overlord.objects.get(pk=1)
    if overlord.is_angry == True:
        overlord.is_angry = False
        overlord.save()
        return render_to_response('worksheets/overlord.html', {})
    else:
        return HttpResponseForbidden()

def index(request):
    return render(request, 'worksheets/index.html', {})


def get_evernote_client():
    return EvernoteClient(consumer_key='uwekamper-3546', consumer_secret='f405b23d1c27e7bf', sandbox=True)


def login(request):
    if 'oauth_token' not in request.session:
        print 'User is not authenticated'
        client = get_evernote_client()
        request_token = client.get_request_token('http://%s%s' % (request.get_host(), reverse('oauth_callback')))
        client.get_authorize_url(request_token)

        # Save the tokens inside session variables
        request.session['oauth_token_secret'] = request_token['oauth_token_secret']

        return render(request, 'worksheets/redirect_to_login.html', {'oauth': request_token['oauth_token']})
    else:
        print 'User is authenticated exist'
        return render(request, 'worksheets/logged_in.html')

def oauth_callback(request):
    #profile = request.user.get_profile()
    try:
        client = get_evernote_client()
        access_token = client.get_access_token(request.GET['oauth_token'], request.session['oauth_token_secret'], request.GET['oauth_verifier'])

        print access_token
        request.session['oauth_token'] = access_token

        return render(request, 'worksheets/logged_in.html')

    except KeyError:
        return redirect('/login/')






