# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
from django.http import HttpResponse
from django.shortcuts import render
from .models import Dragon_Article_Post, Category

index_information = "<h1>Welcome to DustFlight Virtual Network Studio !</h1>"


def hello(request):
    return HttpResponse("<center>[CONSOLE] Running Test => [ %s ]</center>" % str(index_information))


def index(request):
    try:
        print("[NOTICE] Running Function => [index]")
        template_page = "Blog/index.html"
        key_value_colleciton = {
            'template_title': "DustFlight VNS - Blog System Center",
            'template_header': "A technology company that make the world better!",
            'template_content': "Welcome to DustFlight Virtual Network Studio ! Enjoy yourself !",
            'template_footer': "Powered By DustFlight Ryan"
        }
        context = {'key_value_colleciton': key_value_colleciton}
        return render(request, template_page, context)
    except Exception as ex:
        print(
            "[NOTICE] There is no template built in this floder ! Details => [%s]" % str(ex))


def nav(request):
    try:
        template_page = 'Blog/header.html'
        category = Category.object.all()
        context = {
            'category_list': category
        }
        return render(request, template_page, context)
    except Exception as ex:
        print(
            "[NOTICE] There is no Category data in Database ! Details => [%s]" % str(ex))


def list_whole_article(request):
    try:
        print("[NOTICE] Running Function => [list_whole_article]")
        template_page = "Blog/blog_article.html"
        article_list = Dragon_Article_Post.objects.all()
        context = {"article_list": article_list}
        return render(request, template_page, context)
    except Exception as ex:
        print(
            "[NOTICE] There is no template built in this floder ! Details => [%s]" % str(ex))


def about(request):
    print("[NOTICE] Running Function => [about]")
    template_page = 'Blog/about.html'
    try:
        info_list_collection = {
            'master_name': '周凌翔 Ryan',
            'email_box': 'suigege23@163.com',
            'QQ_Number': '839375344',
            'Wechat': 'fengzilaozhou',
            'Telephone': '17306178678',
            'address': '江苏省昆山市',
            'post_number': '215300',
        }
        context = {'info_list_collection': info_list_collection}
        return render(request, template_page, context)
    except Exception as ex:
        print(
            "[NOTICE] There is no template built in this floder ! Details => [%s]" % str(ex))
