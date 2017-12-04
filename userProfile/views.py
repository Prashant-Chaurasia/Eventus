from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from account.models import Students, Faculty
from .forms import StudentForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied


@login_required()  # only logged in users should access this
def edit_user(request):
    # querying the User object with pk from url
    user = request.user

    # prepopulate StudentForm with retrieved user values from above.
    user_form = StudentForm(instance=user)

    if is_faculty(request.user):
        ProfileInlineFormset = inlineformset_factory(User, Faculty,
                                                     fields=('Name', 'Education', 'Area', 'About'))
        formset = ProfileInlineFormset(instance=user)

        if request.user.is_authenticated() and request.user.id == user.id:
            if request.method == "POST":
                user_form = StudentForm(request.POST, request.FILES, instance=user)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

                if user_form.is_valid():
                    created_user = user_form.save(commit=False)
                    formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

                    if formset.is_valid():
                        created_user.save()
                        formset.save()
                        return HttpResponseRedirect('/')

            return render(request, "userProfile/faculty.html", {
                "noodle": user.pk,
                "noodle_form": user_form,
                "formset": formset,
            })
        else:
            raise PermissionDenied
    else:
        ProfileInlineFormset = inlineformset_factory(User, Students,
                                                     fields=('Name', 'RollNo', 'Course', 'Batch', 'Year', 'About'))
        formset = ProfileInlineFormset(instance=user)

        if request.user.is_authenticated() and request.user.id == user.id:
            if request.method == "POST":
                user_form = StudentForm(request.POST, request.FILES, instance=user)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

                if user_form.is_valid():
                    created_user = user_form.save(commit=False)
                    formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

                    if formset.is_valid():
                        created_user.save()
                        formset.save()
                        return HttpResponseRedirect('/')

            return render(request, "userProfile/fun.html", {
                "noodle": user.pk,
                "noodle_form": user_form,
                "formset": formset,
            })
        else:
            raise PermissionDenied


def is_faculty(user):
    return user.groups.filter(name='FacultyOnly').exists()