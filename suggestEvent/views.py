from django.shortcuts import render
from.forms import SuggestForm
from account.models import Students
# Create your views here.


def Suggest_Event(request):
    if request.method == "POST":
        form = SuggestForm(request.POST)
        if form.is_valid():
            stud = Students.objects.get(user= request.user)
            Event = form.save(commit=False)
            Event.author = request.user
            Event.Code = stud.Code
            Event.save()
            return render(request, 'suggest/success.html', {})

    else:
        form = SuggestForm()
    return render(request, 'suggest/suggest_event.html', {'form': form})