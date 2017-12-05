from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import College
from .forms import CollegeForm
from django.shortcuts import redirect
from django.utils import timezone
from account.views import is_secretory
# Create your views here.
from django.contrib.auth.decorators import login_required



@login_required(login_url='/accounts/login')
def College_list(request):
    college = College.posted.all()
    sec = False
    if is_secretory(request.user):
        sec = True
    return render(request,'college/College/list.html',{'colleges':college, 'sec': sec})


@login_required(login_url='/accounts/login')
def College_detail(request, year, month, day, event):
    event = get_object_or_404(College, slug=event,
                            postdate__year=year,
                            postdate__month=month,
                            postdate__day=day)
    sec = False
    if is_secretory(request.user):
        sec = True

    return render(request,'events/Events/detail.html',{'event': event, 'sec':sec})

@login_required(login_url='/accounts/login')
def Add_College(request):
    sec = False
    if is_secretory(request.user):
        sec = True
    if request.method == "POST":
        form = CollegeForm(request.POST,request.FILES)
        if form.is_valid():
            College = form.save(commit=False)
            College.author = request.user
            College.slug = form.cleaned_data['name']
            College.created = timezone.now()
            College.save()
            return HttpResponseRedirect('/colleges')

    else:
        form = CollegeForm()

    return render(request, 'college/College/add_college.html', {'form': form, 'sec': sec})