from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from LogHoursApp.forms import LogHoursForm
from LogHoursApp.models import LogHours


# Create your views here.
@login_required(login_url='/accounts/login/')
def log(request):
    if request.method == "POST":
        form = LogHoursForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Registro creado correctamente')
                form.clean()
                return redirect("log/show")
            except:
                pass
        else:
            for error in form.errors:
                messages.error(request, 'Tenga en cuenta {0}'.format(error))
    else:
        initial = {'author': request.user}
        form = LogHoursForm(initial=initial)
    return render(request, 'log_hour.html', {'form': form})


@login_required(login_url='/accounts/login/')
def show_all(request):
    if not request.user:
        return redirect('accounts/login')

    log_hours = LogHours.objects.all()
    return render(request, "log_show.html", {'logHours': log_hours})


@login_required(login_url='/accounts/login/')
def show(request):
    log_hours = LogHours.objects.filter(author=request.user)
    return render(request, "log_show.html", {'logHours': log_hours})


@login_required(login_url='/accounts/login/')
def edit(request, id):
    log_hours = LogHours.objects.get(id=id)
    initial = {'author': request.user}
    form = LogHoursForm(instance=log_hours, initial=initial)
    return render(request, 'log_edit.html', {'logHour': log_hours, 'form': form})


@login_required(login_url='/accounts/login/')
def update(request, id):
    log_hours = LogHours.objects.get(id=id)
    form = LogHoursForm(request.POST, instance=log_hours)
    if form.is_valid():
        form.save()
        messages.success(request,
                         'Registro (' + str(log_hours.id) + ') actualizado.')
        form.clean()
        return redirect("log/show")
    else:
        messages.error(request, form.errors)

    return render(request, 'log_edit.html', {'LogHours': log_hours})


@login_required(login_url='/accounts/login/')
def destroy(request, id):
    log_hours = LogHours.objects.get(id=id)
    log_hours.delete()
    return redirect("log/show")
