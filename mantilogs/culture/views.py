from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from .models import Culture, Log, Quarantine
from .forms import Create_Log_Form, Create_Culture_Form, Create_Quarantine_Form


# Index Views
def culture_index(request):
    """Display a full list of all active cultures with links to their profiles, add log, add quarantine."""
    cultures = get_list_or_404(Culture, retired=False)
    last_logs = {}
    total_cultures = 0
    for culture in cultures:
        total_cultures += 1
        # Find logs for Culture
        if (Log.objects.filter(culture=culture)):
            last_logs[culture] = Log.objects.filter(
                culture=culture).latest('date')
    return render(request, 'culture_idx.html', {'cultures': cultures, 'last_logs': last_logs,
                                                'user_info': request.user, 'page_title': 'Culture Index',
                                                'page_subtitle': f"Curently {total_cultures} active cultures"})


# Log Endpoints.
def add_log(request, cul):
    """Display form for adding a log to culture <cul>, handle POST from said form. """
    culture = get_object_or_404(Culture, id=cul)
    post_endpoint = f"/culture/add_log/{culture.id}"
    if request.method == 'POST':
        if request.user.is_superuser:
            form = Create_Log_Form(request.POST)
            if form.is_valid():
                # Process the data.
                # Just gonna save it for now without cleaning because I love me some technical debt.
                form.save()
                # Redirect
                return HttpResponseRedirect('/culture/profile/'+cul)
        else:
            HttpResponseRedirect('/culture/profile/'+cul)
    else:
        form = Create_Log_Form()
        form.fields['culture'].initial = culture

    return render(request, 'cul_add_log.html', {'form': form, 'culture': culture, 'user_info': request.user, 'endpoint': post_endpoint})


def edit_log(request, cul, log):
    """Edit Log entries. """
    culture = get_object_or_404(Culture, id=cul)
    redir_path = f'/culture/{culture.id}'
    log_instance = get_object_or_404(Log, id=log)
    # The endpoint for the form to post to.
    post_endpoint = f"/culture/edit_log/{culture.id}/{log_instance.id}"
    if request.method == 'POST':
        if request.user.is_superuser:
            form = Create_Log_Form(request.POST, instance=log_instance)
            if form.is_valid():
                # Process the data.
                # Just gonna save it for now without cleaning because I love me some technical debt.
                form.save()
                # Redirect
                return HttpResponseRedirect('/culture/profile/'+cul)
        else:
            HttpResponseRedirect('/culture/profile/'+cul)
    else:
        form = Create_Log_Form(instance=log_instance)
        form.fields['culture'].initial = culture

    return render(request, 'cul_add_log.html', {'form': form, 'culture': culture, 'user_info': request.user, 'endpoint': post_endpoint})

# Culture Views
def culture_profile(request, cul):
    """Display a full culture profile with all logs."""
    # TODO: Add Pagination. Probably another endpoint for logs and some JS fetch reqs.
    culture = get_object_or_404(Culture, id=cul)
    logs = Log.objects.filter(culture=culture).order_by("-date")
    quarantine = {}
    if logs == None:
        logs = {}
    if Quarantine.objects.filter(culture=culture):
        quarantine = Quarantine.objects.filter(culture=culture).latest()

    return render(request, 'culture_prof.html', {'culture': culture, 'logs': logs,
                                          'user_info': request.user, 'page_title': culture.name,
                                          'page_subtitle': culture.specie, 'quarantine': quarantine})


def add_culture(request):
    """Adds a culture from form data"""
    post_endpoint = f"/culture/add_culture/"
    if request.method == 'POST':
        if request.user.is_superuser:
            form = Create_Culture_Form(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/culture/index')
        else:
            HttpResponseRedirect('/culture/index')
    else:
        form = Create_Culture_Form()
        return render(request, 'add_culture.html',
                  {'form': form, 'user_info': request.user, 'endpoint': post_endpoint})


def edit_culture(request, cul):
    """Adds a culture from form data"""
    culture = get_object_or_404(Culture, id=cul)
    post_endpoint = f"/culture/edit_culture/{culture.id}"
    redir = f'/culture/profile/{culture.id}'

    if request.method == 'POST':
        if request.user.is_superuser:
            form = Create_Culture_Form(request.POST, instance=culture)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/culture/profile/' + cul)
        else:
            return HttpResponseRedirect('/culture/profile/' + cul)
    else:
        form = Create_Culture_Form(instance=culture)
        return render(request, 'add_culture.html',
                  {'form': form, 'user_info': request.user, 'endpoint': post_endpoint})


def add_quarantine(request, cul):
    """Display form for adding a log to culture <cul>, handle POST from said form. """
    culture = get_object_or_404(Culture, id=cul)
    post_endpoint = f"/culture/add_quarantine/{culture.id}"
    if request.method == 'POST':
        if request.user.is_superuser:
            form = Create_Quarantine_Form(request.POST)
            if form.is_valid():
                # Process the data.
                # Just gonna save it for now without cleaning because I love me some technical debt.
                form.save()
                # Redirect
                return HttpResponseRedirect('/culture/profile/' + cul)
        else:
            HttpResponseRedirect('/culture/profile/' + cul)
    else:
        form = Create_Quarantine_Form()
        form.fields['culture'].initial = culture

    return render(request, 'cul_add_quarantine.html', {'form': form, 'culture': culture, 'user_info': request.user, 'endpoint': post_endpoint})


def edit_quarantine(request, quar):
    """Display form for adding a log to culture <cul>, handle POST from said form. """
    quarantine = get_object_or_404(Quarantine, id=quar)
    post_endpoint = f"/culture/edit_quarantine/{quarantine.id}"
    print(quarantine.culture.id)
    if request.method == 'POST':
        if request.user.is_superuser:
            form = Create_Quarantine_Form(request.POST, instance=quarantine)
            if form.is_valid():
                # Process the data.
                # Just gonna save it for now without cleaning because I love me some technical debt.
                form.save()
                # Redirect
                return HttpResponseRedirect('/culture/profile/' + str(quarantine.culture.id))
        else:
            HttpResponseRedirect('/culture/profile/' + str(quarantine.culture.id))
    else:
        form = Create_Quarantine_Form(instance=quarantine)


    return render(request, 'cul_add_quarantine.html', {'form': form, 'user_info': request.user, 'endpoint': post_endpoint})



