from django.shortcuts import get_object_or_404, redirect, render

from NamuKiwi.forms import EditForm, CreateForm
from .models import PageData
from django.utils import timezone


def MainPage(request):
    data_list = PageData.objects.order_by('create_date')
    if request.method == "POST":
        searchData = request.POST.get('search', '')
    else:
        searchData = ''
    context = {'pageDataList' : data_list, 'searchData' : searchData}
    return render(request, 'NamuKiwi/MainPage.html', context);

def DetailPage(request, page_subject):
    """
    pybo 목록 출력
    """
    data = PageData.objects.get(pk=page_subject)
    data_list = PageData.objects.order_by('create_date')
    context = {'pageData': data, 'pageDataList' : data_list}
    return render(request, 'NamuKiwi/DetailPage.html', context)

def EditPage(request, page_subject):
    """
    pybo 목록 출력
    """
    data = PageData.objects.get(pk=page_subject)

    if request.method == "POST":
        form = EditForm(request.POST, instance=data)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('kiwi:DetailPage', page_subject=data.subject)
    else:
        form = EditForm(instance=data)
    context = {'form': form, 'pageData': data}
    return render(request, 'NamuKiwi/EditPage.html', context)

def DeletePage(request, page_subject):
    """
    pybo 질문삭제
    """
    data = get_object_or_404(PageData, pk=page_subject)
    data.delete()
    return redirect('kiwi:MainPage')

def CreatePage(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('kiwi:MainPage')
    else:
        form = CreateForm()
    context = {'form': form}
    return render(request, 'NamuKiwi/CreatePage.html', context)