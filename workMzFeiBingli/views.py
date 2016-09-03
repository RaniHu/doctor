from django.shortcuts import render, render_to_response

from django.template import RequestContext

from .models import Feibingli

from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger

from django.core.paginator import Paginator

# Create your views here.
ONE_PAGE_OF_DATA = 2


def fbingli(rq):
    try:
        curPage = int(rq.GET.get('curPage', '1'))
        allPage = int(rq.GET.get('allPage', '1'))
        pageType = str(rq.GET.get('pageType', ''))
    except ValueError:
        curPage = 1
        allPage = 1
        pageType = ''
        # 判断点击了【下一页】还是【上一页】
    if pageType == 'pageDown':
        curPage += 1
    elif pageType == 'pageUp':
        curPage -= 1

    if curPage == 1 and allPage == 1:  # 标记1
        allPostCounts = Feibingli.objects.count()
        allPage = allPostCounts // ONE_PAGE_OF_DATA
        remainPost = allPostCounts % ONE_PAGE_OF_DATA
        if remainPost > 0:
            allPage += 1

    startPos = (curPage - 1) * ONE_PAGE_OF_DATA
    endPos = startPos + ONE_PAGE_OF_DATA
    Feibingli_list = Feibingli.objects.all()[startPos:endPos]

    # 获取用户输入的页数
    middlepos = rq.POST.get('goPage')
    # 如果输入的页数不为空
    if middlepos is not None:
        if int(middlepos) <= int(allPage):
            startPos = (int(middlepos) - 1) * ONE_PAGE_OF_DATA
            endPos = startPos + ONE_PAGE_OF_DATA
            Feibingli_list = Feibingli.objects.all()[startPos:endPos]
            curPage = int(middlepos)
        else:
            startPos = (int(allPage) - 1) * ONE_PAGE_OF_DATA
            endPos = startPos + ONE_PAGE_OF_DATA
            Feibingli_list = Feibingli.objects.all()[startPos:endPos]
            curPage = int(allPage)

    return render_to_response('workMzFeiBingli/fbingli.html',
                              {'Feibingli_list': Feibingli_list, 'allPage': allPage, 'curPage': curPage},
                              context_instance=RequestContext(rq))
