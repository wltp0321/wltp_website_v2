from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
staff_required = user_passes_test(lambda u: u.is_staff)
from .models import aboutCrewonessSettings
from .forms import CrewSettingForm

def crew_settings_list(request):
    settings = aboutCrewonessSettings.objects.all()
    return render(request, 'crew_setting/crew_setting_list.html', {'about_crew_settings': settings})

def crew_setting_detail(request, pk):
    setting = get_object_or_404(aboutCrewonessSettings, pk=pk)
    return render(request, 'crew_setting/crew_setting_detail.html', {'setting': setting})

@staff_required
def crew_setting_create(request):
    if request.method == 'POST':
        form = CrewSettingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about_crew:list')
    else:
        form = CrewSettingForm()
    return render(request, 'crew_setting/crew_setting_form.html', {'form': form, 'create': True})

@staff_required
def crew_setting_edit(request, pk):
    setting = get_object_or_404(aboutCrewonessSettings, pk=pk)
    if request.method == 'POST':
        form = CrewSettingForm(request.POST, instance=setting)
        if form.is_valid():
            form.save()
            return redirect('about_crew:list')
    else:
        form = CrewSettingForm(instance=setting)
    return render(request, 'crew_setting/crew_setting_form.html', {'form': form, 'create': False})

@staff_required
def crew_setting_delete(request, pk):
    setting = get_object_or_404(aboutCrewonessSettings, pk=pk)
    if request.method == 'POST':
        setting.delete()
        return redirect('about_crew:list')
    return render(request, 'crew_setting/crew_setting_confirm_delete.html', {'setting': setting})
