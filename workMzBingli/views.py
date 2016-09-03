from django.shortcuts import render, render_to_response

from django.template import RequestContext

from .models import Bingli

from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger

from django.core.paginator import Paginator

# def bingli(request):
#     bingli_list = Bingli.objects.all()  
#     paginator=JuncheePaginator(bingli_list,2)
#     try:
#         page=int(request.GET.get('page',1))
#         bingli_list=paginator.page(page)
#     except (EmptyPage,InvalidPage,PageNotAnInteger):
#         bingli_list=paginator.page(1)
#              
#     return render_to_response('workMzBingli/bingli.html',{'bingli_list':bingli_list})
#     return render(request,'workMzBingli/bingli.html',locals())
# 
# 
#   
# class JuncheePaginator(Paginator):
#       def __init__(self, object_list, per_page, range_num=5, orphans=0, allow_empty_first_page=True):
#           Paginator.__init__(self, object_list, per_page, orphans, allow_empty_first_page)
#           self.range_num = range_num
#   
#       def page(self, number):
#           self.page_num = number
#           return super(JuncheePaginator, self).page(number)
#  
#       def _page_range_ext(self):
#           num_count = 2 * self.range_num + 1
#           if self.num_pages <= num_count:
#               return range(1, self.num_pages + 1)
#           num_list = []
#           num_list.append(self.page_num)
#           for i in range(1, self.range_num + 1):
#               if self.page_num - i <= 0:
#                   num_list.append(num_count + self.page_num - i)
#               else:
#                   num_list.append(self.page_num - i)
#  
#               if self.page_num + i <= self.num_pages:
#                   num_list.append(self.page_num + i)
#               else:
#                   num_list.append(self.page_num + i - num_count)
#           num_list.sort()
#           return num_list
#       page_range_ext = property(_page_range_ext)

# 分页
ONE_PAGE_OF_DATA = 2


def turnPage(rq):
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
        allPostCounts = Bingli.objects.count()
        allPage = allPostCounts // ONE_PAGE_OF_DATA
        remainPost = allPostCounts % ONE_PAGE_OF_DATA
        if remainPost > 0:
            allPage += 1

    startPos = (curPage - 1) * ONE_PAGE_OF_DATA
    endPos = startPos + ONE_PAGE_OF_DATA
    bingli_list = Bingli.objects.all()[startPos:endPos]

    # 获取用户输入的页数
    middlepos = rq.POST.get('goPage')
    # 如果输入的页数不为空
    if middlepos is not None:
        if int(middlepos) <= int(allPage):
            startPos = (int(middlepos) - 1) * ONE_PAGE_OF_DATA
            endPos = startPos + ONE_PAGE_OF_DATA
            bingli_list = Bingli.objects.all()[startPos:endPos]
            curPage = int(middlepos)
        else:
            startPos = (int(allPage) - 1) * ONE_PAGE_OF_DATA
            endPos = startPos + ONE_PAGE_OF_DATA
            bingli_list = Bingli.objects.all()[startPos:endPos]
            curPage = int(allPage)

    return render_to_response('workMzBingli/bingli.html',{'bingli_list': bingli_list, 'allPage': allPage, 'curPage': curPage},
                              context_instance=RequestContext(rq))

    # def turnPage(request):
    #     limit = 2  # 每页显示的记录数
    #     bingli_list = Bingli.objects.all()
    #     paginator = Paginator(bingli_list, limit)  # 实例化一个分页对象
    #     page = request.GET.get('page')  # 获取页码
    #     try:
    #         bingli_list = paginator.page(page)  # 获取某页对应的记录
    #     except PageNotAnInteger:  # 如果页码不是个整数
    #         bingli_list = paginator.page(1)  # 取第一页的记录
    #     except EmptyPage:  # 如果页码太大，没有相应的记录
    #         bingli_list = paginator.page(paginator.num_pages)  # 取最后一页的记录
    #     return render_to_response('workMzBingli/bingli.html',{'bingli_list':bingli_list})
