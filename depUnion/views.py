from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.models import User
from commonDatas .models import Docpersonalinfo
from commonDatas .models import Unioncomment
from commonDatas .models import Uniondetail
from commonDatas .models import Unionoutline
from photologue.models import *
from django.conf import settings
from PIL import Image
import datetime
import os

def depUnion(request):
    if not request.user.is_authenticated():
        return render_to_response("userLoginin/login.html")
    else:
        detail_list = Uniondetail.objects.all()
        usernameGet = request.user
        aa = Docpersonalinfo.objects.get(userid=usernameGet.username)
        bb = Uniondetail.objects.filter(pubname=aa.username)

        return render_to_response('depUnion/depUnion.html',{'detail_list':detail_list,'bb':bb})


def pubContent(request):
    selectPrivate= request.POST.get('selectPrivate')
    workTxt = request.POST.get('workTxt')

    unionDetail=Uniondetail()                           #获取工会动态详细表
    unionDetail.contenttext=workTxt
    unionDetail.contentnum=str(random.random())[2:18] + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    usernameGet = request.user
    unionDetail.userid = usernameGet
    unionDetail.save()



    unionOutline = Unionoutline()  # 获取工会动态概要表
    unionOutline.jurisdiction=selectPrivate
    unionOutline.contentnum=unionDetail.contentnum
    unionOutline.save()

    aa = Docpersonalinfo.objects.get(userid=usernameGet.username)
    bb = Uniondetail.objects.get(pubname=aa.username)
    detail_list=Uniondetail.objects.all()


    # 上传图片
    try:
        f = request.FILES['uploadInput']
        if f.size > 5000000:
            return HttpResponse("it is large!")
        try:
            parser = ImageFile.Parser()
            for chunk in f.chunks():
                parser.feed(chunk)
            img = parser.close()
        except IOError:
            return HttpResponse("it is an io error!")

        imageName = 'photologue/photos/' + f.name
        name = settings.STATIC_PATH + '/' + imageName
        img = Image.open(f)
        img.save(name)
    except UnicodeEncodeError:
        return render_to_response('depUnion/depUnion.html', {'image_error': "please use English", 'detail_list': detail_list, 'bb': bb})

        # now ='TB'+datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    photoInfo = Photo(image=imageName, title=unionDetail.contentnum, slug='00' +unionDetail.contentnum, is_public=True)
    photoInfo.save()

    return HttpResponse("it is ok!")



def comment(request):
    commenttext = request.POST.get('commenttext')
    comTable=Unioncomment()
    comTable.commenttext = commenttext


    usernameGet = request.user                                  #获取当前登陆用户
    bb = Docpersonalinfo.objects.get(userid=usernameGet)
    comTable.commentpersonid=bb.userid

    # comment_list=comTable.object.filter()

    comTable.save()
    return HttpResponse(bb.username)
