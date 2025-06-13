from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post


# Create your views here.




def index(request):
    article_records = Post.objects.all()
    article_list = list()
   
   
    for count, article in enumerate(article_records):
        article_list.append("#{}: {}<br>".format(str(count), str(article)))
        article_list.append("<small>{}</small><br><hr>".format(article.content))
   
   
    return HttpResponse(article_list)


def about(request):
    return HttpResponse("hello world")

from datetime import datetime
def index_use_template(requests):
    article_records = Post.objects.all()
    now = datetime.now()
    return render(requests, "index.html", locals())
    # 等同於
    # return render(requests, "index.html", {'now': now})
