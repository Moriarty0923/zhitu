from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app01 import models
import json


# Create your views here.


# 登录
def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        # 验证用户名密码是否正确，然后登陆存入session

        uid = request.POST.get("uid")
        pwd = request.POST.get("pwd")
        print(type, uid, pwd)
        if len(models.User.objects.filter(username=uid, password=pwd)) != 0:
            # 登录成功

            return HttpResponse("登录成功")
        else:
            return HttpResponse("登录失败")


def user_register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        models.User.objects.create(username=username, password=pwd)
        return redirect("/user/register")


def admin_home(request):
    if request.method == 'GET':
        list = models.User.objects.all()
        return render(request, 'admin_home.html', {'topics': list})


def user_delete(request):
    id = request.GET.get('id')
    models.User.objects.filter(id=id).delete()
    return redirect("/admin/home/")


def home(request):
    return render(request, 'home.html')
    if request.method == 'GET':
        response = {}

        # top 10（公告）的处理，筛选10个也要改
        announcements = models.Announcement.objects.filter()
        # 把这10个公告封装成字典
        a_list = []
        for a in announcements:
            dic = {'a_id': a.id, 'a_title': a.a_title}
            a_list.append(dic)
        # 把列表装进回复字典里
        n = 10 if len(a_list) < 10 else len(a_list)

        response['a_list'] = a_list[::-1][0:n-1]

        # 帖子推荐列表，推荐8个帖子，推荐8个要改
        recommends = models.Topic.objects.filter(recommend=True)
        # 推荐列表
        r_list = []

        for t in recommends:
            dic = {'t_id': t.id, 't_title': t.t_title, 't_introduce': t.t_introduce, 't_photo': t.t_photo}
            r_list.append(dic)
        # 把列表装进response
        response['r_list'] = r_list

        # 把uid装进返回字典里
        response['uid'] = request.session['uid']

        # 把所有类别装入返回字典里
        kinds = models.Kind.objects.filter()
        response['kinds'] = kinds

        return render(request, 'home.html', response)


# 所有帖子
def all_tie(request, kid, reply_limit, time_limit):
    return render(request, 'all.html')
    uid = request.session.get('uid')
    if request.method == 'GET':
        kinds = models.Kind.objects.filter()
        if kid == '0' and reply_limit == '0' and time_limit == '0':
            # 默认时间排序把帖子传过去
            topics = models.Topic.objects.filter()
        else:
            # request.path_info   # 获取当前url
            # from django.urls import reverse
            # reverse('all_tie', kwargs={'kid': '0', 'reply_limit': '0', 'time_limit': '0'})

            topics = models.Topic.objects.filter()

            # 筛选分类
            if kid != '0':
                topics = models.Topic.objects.filter(t_kind=kid)

            # 筛选回复数量
            tmp = []
            for topic in topics:
                # 查看每个帖子的回复数量
                count = len(models.Reply.objects.filter(r_tid=topic.id))
                # print(count)
                print(reply_limit)
                if reply_limit == '0':
                    pass
                elif reply_limit == '1':  # 1是大于100
                    print('到1了')
                    if count < 100:
                        print('到了')
                        continue
                elif reply_limit == '2':  # 2是30-100
                    if count < 30 or count > 100:
                        continue
                elif reply_limit == '3':  # 3是小于30
                    if count > 30:
                        continue
                tmp.append(topic)
            topics = tmp
            print(topics)

            # 筛选发布时间
            tmp = []
            for topic in topics:
                if time_limit == '0': # 0是全部时间
                    pass
                elif time_limit == '1':   # 1是1个月内
                    # 如果在限制之前，就筛掉
                    pass
                elif time_limit == '2':   # 2是3个月内
                    # 如果在限制之前，就筛掉
                    pass
                elif time_limit == '3':   # 3是6个月内
                    # 如果在限制之前，就筛掉
                    pass
                elif time_limit == '4':   # 4是1年内
                    # 如果在限制之前，就筛掉
                    pass
                tmp.append(topic)
            topics = tmp

        response = {
            'topics': topics,
            'kinds': kinds,
            'kid': kid,
            'time_limit': time_limit,
            'reply_limit': reply_limit,
            'uid': uid,
        }
        return render(request, 'all.html', response)

    elif request.method == 'POST':
        # 搜索接收一个字段，查询标题或者简介里有关键字的帖子
        keys = request.POST.get('keys')
        # 按关键字查询标题里含有关键字的
        topics = models.Topic.objects.filter(t_title__icontains=keys)

        kinds = models.Kind.objects.filter()
        return render(request, 'all.html', {'topics': topics, 'kinds': kinds, 'uid': uid})