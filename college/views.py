from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import College
from .forms import CollegeForm
from django.shortcuts import redirect
from django.utils import timezone
# Create your views here.

def College_list(request):
    college = College.posted.all()
    return render(request,'college/College/list.html',{'colleges':college})

def College_detail(request, year, month, day, event):
    event = get_object_or_404(College, slug=event,
                            postdate__year=year,
                            postdate__month=month,
                            postdate__day=day)
    return render(request,'events/Events/detail.html',{'event':event})

def Add_College(request):
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
    return render(request, 'college/College/add_college.html', {'form': form})