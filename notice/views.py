from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import ImportantNotice, NormalNotice, ArchivedNotice
from django.contrib.auth.decorators import user_passes_test
staff_required = user_passes_test(lambda u: u.is_staff)

# 공지 목록
def notice_list(request):
    ImportantNotices = ImportantNotice.objects.all()
    NormalNotices = NormalNotice.objects.all()
    ArchivedNotices = ArchivedNotice.objects.all()
    return render(request, 'notice/index.html', {
        'ImportantNotices': ImportantNotices,
        'NormalNotices': NormalNotices,
        'ArchivedNotices': ArchivedNotices
    })

# 개별 공지 상세 (아카이브)
def archived_notice(request, notice_id):
    notice = get_object_or_404(ArchivedNotice, id=notice_id)
    return render(request, 'notice/detail.html', {'notice': notice})

# 공지 작성
@staff_required
def notice_create(request):
    if request.method == 'POST':
        notice_type = request.POST.get('notice_type')
        title = request.POST.get('title')
        content0 = request.POST.get('content0')
        content1 = request.POST.get('content1')

        model_map = {
            'important': ImportantNotice,
            'normal': NormalNotice,
            'archived': ArchivedNotice,
        }

        model = model_map.get(notice_type)
        if model:
            model.objects.create(
                title=title,
                content0=content0,
                content1=content1,
                created_at=timezone.now()
            )
        return redirect('notice:list')
    return render(request, 'notice/create.html')

@staff_required
def notice_edit(request, notice_type, notice_id):
    model_map = {
        'important': ImportantNotice,
        'normal': NormalNotice,
        'archived': ArchivedNotice,
    }

    Model = model_map.get(notice_type)
    notice = get_object_or_404(Model, id=notice_id)

    if request.method == 'POST':
        new_title = request.POST.get('title')
        new_content0 = request.POST.get('content0')
        new_content1 = request.POST.get('content1')
        new_type = request.POST.get('notice_type')  # ★ type 변경 값

        # 현재 타입 그대로면 그냥 save만 진행
        if new_type == notice_type:
            notice.title = new_title
            notice.content0 = new_content0
            notice.content1 = new_content1
            notice.save()
            return redirect('notice:list')

        # 타입이 바뀌는 경우 → 새 모델로 객체 이동
        NewModel = model_map.get(new_type)  
        NewModel.objects.create(
            title=new_title,
            content0=new_content0,
            content1=new_content1,
        )

        # 기존 객체 삭제
        notice.delete()

        return redirect('notice:list')

    return render(request, 'notice/edit.html', {
        'notice': notice,
        'notice_type': notice_type,
    })


# 공지 삭제
@staff_required
def notice_delete(request, notice_type, notice_id):
    model_map = {
        'important': ImportantNotice,
        'normal': NormalNotice,
        'archived': ArchivedNotice,
    }
    model = model_map.get(notice_type)
    notice = get_object_or_404(model, id=notice_id)

    if request.method == 'POST':
        notice.delete()
        return redirect('notice:list')

    return render(request, 'notice/delete_confirm.html', {'notice': notice, 'notice_type': notice_type})
