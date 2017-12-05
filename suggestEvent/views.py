from django.shortcuts import render
from.forms import SuggestForm
from account.models import Students
from account.views import is_secretory
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login')
def Suggest_Event(request):
    sec = False
    if is_secretory(request.user):
        sec = True
    if request.method == "POST":
        form = SuggestForm(request.POST)
        if form.is_valid():
            stud = Students.objects.get(user= request.user)
            Event = form.save(commit=False)
            Event.author = request.user
            Event.Code = stud.Code
            Event.save()
            return render(request, 'suggest/success.html', {'sec': sec})

    else:
        form = SuggestForm()
    return render(request, 'suggest/suggest_event.html', {'form': form, 'sec': sec})