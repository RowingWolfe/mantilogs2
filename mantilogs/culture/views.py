from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from .models import Culture, Log, Quarantine
from .forms import Create_Log_Form


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

def culture_profile(request, cul):
    """Display a full culture profile with all logs."""
    # TODO: Add Pagination.
    culture = get_object_or_404(Culture, id=cul)
    logs = Log.objects.filter(culture=culture)
    quarantine = {}
    if logs == None:
        logs = {}
    if Quarantine.objects.filter(culture=culture):
        quarantine = Quarantine.objects.filter(culture=culture).latest()

    return render(request, 'culture_prof.html', {'culture': culture, 'logs': logs,
                                          'user_info': request.user, 'page_title': culture.name,
                                          'page_subtitle': culture.specie, 'quarantine': quarantine})


def add_log(request, cul):
    """Display form for adding a log to culture <cul>, handle POST from said form. """
    redir_path = f'/culture/{cul}'
    culture = get_object_or_404(Culture, id=cul)
    if request.method == 'POST':
        form = Create_Log_Form(request.POST)
        if form.is_valid():
            # Process the data.
            # Redirect
            HttpResponseRedirect(redir_path)
    else:
        form = Create_Log_Form()

    return render(request, 'cul_add_log.html', {'form': form, 'culture': culture})

# Profile Views
