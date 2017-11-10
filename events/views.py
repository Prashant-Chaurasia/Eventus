from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Events
from .forms import EventForm
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.shortcuts import redirect
from django.utils import timezone
# Create your views here.

def events_list(request):
    event_list = Events.posted.all()
    paginator = Paginator(event_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    return render(request,'events/Events/list.html',{'page':page,'events':events})

def event_detail(request, year, month, day, event):
    event = get_object_or_404(Events, slug=event,
                            postdate__year=year,
                            postdate__month=month,
                            postdate__day=day)
    return render(request,'events/Events/detail.html',{'event':event})

def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST,request.FILES)
        if form.is_valid():
            Events = form.save(commit=False)
            Events.author = request.user
            Events.slug = form.cleaned_data['title']
            Events.created = timezone.now()
            Events.save()
            return HttpResponseRedirect('/events')

    else:
        form = EventForm()
    return render(request, 'events/Events/create_event.html', {'form': form})