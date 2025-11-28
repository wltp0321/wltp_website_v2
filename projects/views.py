from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from .models import Project
from .forms import ProjectForm
import requests

GITHUB_API_URL = "https://api.github.com/repos/{}"

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/detail.html', {'project': project})

@user_passes_test(lambda u: u.is_staff)
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects:list')
    else:
        form = ProjectForm()
    return render(request, 'projects/form.html', {'form': form, 'title': '새 프로젝트 추가'})

@user_passes_test(lambda u: u.is_staff)
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects:list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/form.html', {'form': form, 'title': '프로젝트 수정'})

@user_passes_test(lambda u: u.is_staff)
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects:list')
    return render(request, 'projects/delete_confirm.html', {'project': project})

def github_last_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    repo_name = project.github_repo
    if not repo_name:
        return JsonResponse({'last_update': None})
    try:
        res = requests.get(GITHUB_API_URL.format(repo_name))
        if res.status_code == 200:
            data = res.json()
            return JsonResponse({'last_update': data.get('pushed_at')})
    except:
        return JsonResponse({'last_update': None})
    return JsonResponse({'last_update': None})
