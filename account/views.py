from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
from account.forms import SignUpForm, SignUpFormForOrganizer
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from account.tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.models import User
import smtplib
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

def home(request):
    return render(request, "account/home.html")

@login_required(login_url='/accounts/login')
def firstpage(request):
    return render(request, 'account/firstPage.html', {})


def view_profile(request):
    args = {'user': request.user}
    return render(request, 'account/profile.html', args)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your EvenTUs Account'
            message = render_to_string('account/account_activation_email.html',
                                       {'user': user, 'domain': current_site.domain,
                                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                        'token': account_activation_token.make_token(user), })
            user.email_user(subject, message)
            send_verification_mail(user.email, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})


def signupForOrganizer(request):
    if request.method == 'POST':
        form = SignUpFormForOrganizer(request.POST)
        print(form)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your EvenTUs Account'
            message = render_to_string('account/account_activation_emailForCompany.html',
                                       {'user': user, 'domain': current_site.domain,
                                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                        'token': account_activation_token.make_token(user), })
            user.email_user(subject, message)
            send_verification_mail(user.email, message)
            return redirect('account_activation_sent')

    else:
        form = SignUpFormForOrganizer()
    return render(request, 'account/signupForOrganizer.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'account/account_activation_sent.html')


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
        return render(request, 'account/firstPage.html', {})
    else:
        return render(request, 'account/profile.html', {})


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
        return render(request, 'account/firstPage.html', {})
    else:
        return render(request, 'account/firstPage.html', {})


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
