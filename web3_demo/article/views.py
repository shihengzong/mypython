from django.shortcuts import render
from django.http import HttpResponse
from . import models as zsh_models
from django.views.decorators.http import require_http_methods
from django.db import models as db_models, connection


def db_save_article(request):
    a = zsh_models.article(title="上邪2",
                           content='我欲与君相知,长命无绝衰,山无陵,江水为竭,冬雷震震,夏雨雪,天地合,乃敢与君绝',
                           is_use=True)
    a.save()
    b = zsh_models.article(title="上邪3",
                           content='我欲与君相知,长命无绝衰,山无陵,江水为竭,冬雷震震,夏雨雪,天地合,乃敢与君绝',
                           is_use=True)
    b.save()
    c = zsh_models.article(title="上邪4",
                           content='我欲与君相知,长命无绝衰,山无陵,江水为竭,冬雷震震,夏雨雪,天地合,乃敢与君绝',
                           is_use=True)
    c.save()
    d = zsh_models.article(title="上邪5",
                           content='我欲与君相知,长命无绝衰,山无陵,江水为竭,冬雷震震,夏雨雪,天地合,乃敢与君绝',
                           is_use=True)
    d.save()
    return HttpResponse("success")


@require_http_methods(['GET'])
def db_get_article(request):
    # 查询全部
    print('-' * 50)
    a_list = zsh_models.article.objects.all()
    for v in a_list:
        print(v)
    # 查询一个
    print('-' * 50)
    a_one = zsh_models.article.objects.get(id=1)
    print(a_one)

    # 过滤
    print('-' * 50)
    a_list_filter = zsh_models.article.objects.filter(id=2)
    for v in a_list_filter:
        print(v)

    # 不等于 exclude
    print('-' * 50)
    a_list_exclude = zsh_models.article.objects.exclude(id=3)
    for v in a_list_exclude:
        print(v)

    # 模糊查找 LIKE(不区分大小写)
    # SELECT `zsh_article`.`id`, `zsh_article`.`title`, `zsh_article`.`content`, `zsh_article`.`is_use` FROM `zsh_article` WHERE `zsh_article`.`title` LIKE %上邪%
    print('-' * 50)
    a_list_icontains = zsh_models.article.objects.filter(title__icontains='上邪')
    print(a_list_icontains)

    # 模糊查找 LIKE BINARY(区分大小写)
    # SELECT `zsh_article`.`id`, `zsh_article`.`title`, `zsh_article`.`content`, `zsh_article`.`is_use` FROM `zsh_article` WHERE `zsh_article`.`title` LIKE BINARY %上邪%
    print('-' * 50)
    a_list_contains = zsh_models.article.objects.filter(title__contains='上邪')
    print(a_list_contains.query)
    for v in a_list_contains:
        print(v)

    # 模糊查找 (startwith 区分大小写)( istartwith 区分大小写) ==> LIKE BINARY 上邪%
    # SELECT `zsh_article`.`id`, `zsh_article`.`title`, `zsh_article`.`content`, `zsh_article`.`is_use` FROM `zsh_article` WHERE `zsh_article`.`title` LIKE BINARY 上邪%

    # 模糊查找 (endwith 区分大小写)( iendwith 区分大小写) ==> LIKE BINARY %上邪
    # SELECT `zsh_article`.`id`, `zsh_article`.`title`, `zsh_article`.`content`, `zsh_article`.`is_use` FROM `zsh_article` WHERE `zsh_article`.`title` LIKE BINARY 上邪%

    # in
    print('-' * 50)
    a_list_in = zsh_models.article.objects.filter(id__in=[1, 2, 3])
    for v in a_list_in:
        print(v)

    # 聚合函数
    # {'sql': 'SELECT AVG(`zsh_article`.`id`) AS `avg` FROM `zsh_article`', 'time': '0.001'}
    print('-' * 50)
    a_list_Avg = zsh_models.article.objects.aggregate(avg=db_models.Avg('id'))
    print(a_list_Avg)

    for v in connection.queries:
        print(v)

    return HttpResponse("success")


from django.views import View


def db_update_article(request):
    print("-" * 30, request.path)
    a_list = zsh_models.article.objects.all()
    for v in a_list:
        print(v)
    return HttpResponse("success")


class ArticleClass(View):
    def get(self, request, *args, **kwargs):
        # 查询文章等于 1 的
        a_list_first = zsh_models.article.objects.filter(id=1)
        for v in a_list_first:
            print(v)
        return HttpResponse("get success")

    def post(self, request, *args, **kwargs):
        # 查询文章等于 2 的
        a_list_second = zsh_models.article.objects.filter(id=2)
        for v in a_list_second:
            print(v)
        return HttpResponse("post success")