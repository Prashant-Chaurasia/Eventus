from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Club
from .forms import ClubForm


# Create your views here.
def View_And_Add_Club(request):
    clubs = Club.objects.all()
    if request.method == "POST":
        form = ClubForm(request.POST,request.FILES)
        if form.is_valid():
            Clubf = form.save(commit=False)
            Clubf.author = request.user
            Clubf.slug = form.cleaned_data['name']
            Clubf.created = timezone.now()
            Clubf.save()
            return HttpResponseRedirect('/clubs')

    else:
        form = ClubForm()

    return render(request, 'clubs/Club/add_club.html', {'form': form,'clubs':clubs})