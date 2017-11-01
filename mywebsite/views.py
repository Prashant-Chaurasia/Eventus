from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
from mywebsite.forms import SignUpForm, SignUpFormForOrganizer
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from mywebsite.tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.models import User
import smtplib
from .models import Event , Comment, Exhibition
from django.utils import timezone
from .forms import EventForm, CommentForm, ExhibitionForm
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

def home(request):
    return render(request, "mywebsite/home.html")


def firstpage(request):
    return render(request, 'mywebsite/firstPage.html', {})


def view_profile(request):
    args = {'user': request.user}
    return render(request, 'mywebsite/profile.html', args)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your InterAdicr Account'
            message = render_to_string('mywebsite/account_activation_email.html',
                                       {'user': user, 'domain': current_site.domain,
                                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                        'token': account_activation_token.make_token(user), })
            user.email_user(subject, message)
            send_verification_mail(user.email, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'mywebsite/signup.html', {'form': form})


def signupForOrganizer(request):
    if request.method == 'POST':
        form = SignUpFormForOrganizer(request.POST)
        print(form)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your InterAdicr Account'
            message = render_to_string('mywebsite/account_activation_emailForOrganizer.html',
                                       {'user': user, 'domain': current_site.domain,
                                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                        'token': account_activation_token.make_token(user), })
            user.email_user(subject, message)
            send_verification_mail(user.email, message)
            return redirect('account_activation_sent')

    else:
        form = SignUpFormForOrganizer()
    return render(request, 'mywebsite/signupForOrganizer.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'mywebsite/account_activation_sent.html')


email_address = 'deployment334@gmail.com'
email_password = 'Dipadi@god5'


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        user.is_active = True
        return render(request, 'mywebsite/firstPage.html', {})
    else:
        return render(request, 'mywebsite/profile.html', {})


def activateForOrganizer(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        user.is_active = True
        return render(request, 'mywebsite/firstPage.html', {})
    else:
        return render(request, 'mywebsite/firstPage.html', {})


def send_verification_mail(email, msg):
    print("send verificaion mail")
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(email_address, email_password)
        server.sendmail(email_address, email, msg)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")


def events_list(request):
    events = Event.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # print("Posts: ", events)
    return render(request, 'mywebsite/event_list.html', {'events': events})

@login_required()
def events_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'mywebsite/event_detail.html', {'event': event})

@login_required()
def events_new(request):
    if request.method == "POST":
        print(request.FILES)
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            print("Post: ", form)
            event.author = request.user
            event.save()
            return redirect('mywebsite:events_detail', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'mywebsite/event_edit.html', {'form': form})

def add_comment_to_post(request, pk):
    event = get_object_or_404(Event, pk=pk)
    #print("Ankur" + event)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.event = event
            comment.save()
            return redirect('mywebsite:events_detail', pk=event.pk)
    else:
        form = CommentForm()
    return render(request, 'mywebsite/add_comment_to_post.html', {'form': form})

@login_required()
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('mywebsite:events_detail', pk=comment.event.pk)


@login_required()
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.event.pk)


def exhibitions_list(request):
    exhibitions = Exhibition.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return  render(request,'mywebsite/exhibition_list.html',{'exhibitions': exhibitions})

@login_required()
def exhibitions_detail(request, pk):
    exhibition = get_object_or_404(Exhibition, pk=pk)
    return render(request, 'mywebsite/exhibition_detail.html', {'exhibition': exhibition})

@login_required()
def exhibitions_new(request):
    if request.method == "POST":
        print(request.FILES)
        form = ExhibitionForm(request.POST, request.FILES)
        if form.is_valid():
            exhibition = form.save(commit=False)
            print("Post: ", form)
            exhibition.author = request.user
            exhibition.save()
            return redirect('mywebsite:exhibitions_detail', pk=exhibition.pk)
    else:
        form = ExhibitionForm()
    return render(request, 'mywebsite/exhibition_edit.html', {'form': form})

