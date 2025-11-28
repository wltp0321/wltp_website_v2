from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from .models import CrewMember
from .forms import CrewMemberForm  # 아래에서 form 정의

# staff 체크
def staff_required(user):
    return user.is_staff

# 팀원 리스트
def crew_list(request):
    crews = CrewMember.objects.all()
    return render(request, 'about_crewones/crew_list.html', {'crews': crews})

# 팀원 추가
@login_required
@user_passes_test(staff_required)
def add_crew(request):
    if request.method == 'POST':
        form = CrewMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('about_crewones:crew_list')
    else:
        form = CrewMemberForm()
    return render(request, 'about_crewones/crew_form.html', {'form': form, 'action': '추가'})

# 팀원 수정
@login_required
@user_passes_test(staff_required)
def edit_crew(request, pk):
    crew = get_object_or_404(CrewMember, pk=pk)
    if request.method == 'POST':
        form = CrewMemberForm(request.POST, request.FILES, instance=crew)
        if form.is_valid():
            form.save()
            return redirect('about_crewones:crew_list')
    else:
        form = CrewMemberForm(instance=crew)
    return render(request, 'about_crewones/crew_form.html', {'form': form, 'action': '수정'})

# 팀원 삭제
@login_required
@user_passes_test(staff_required)
def delete_crew(request, pk):
    crew = get_object_or_404(CrewMember, pk=pk)
    if request.method == 'POST':
        crew.delete()
        return redirect('about_crewones:crew_list')
    return render(request, 'about_crewones/crew_confirm_delete.html', {'crew': crew})
