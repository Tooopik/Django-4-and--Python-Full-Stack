from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}


def news_view(request, topic):
    try:
        return HttpResponse(articles[topic])  # TEMPLATE HTML (JINJA)
    except:
        raise Http404("404 GENERIC ERROR")  # 404.html
        #message = f"PAGE NOT FOUND"
        # return HttpResponseNotFound(message)


def add_view(request, num1, num2):
    # domain.com/first_app/num1/num2 ---> num1+num2
    add_result = num1 + num2
    result = f"{num1} + {num2} = {add_result}"
    return HttpResponse(str(result))


# domian.com/first_app/0 ---> domian.com/first_app/sports

def num_page_view(request, num_page):
    topic_list = list(articles.keys())
    topic = topic_list[num_page]

    return HttpResponseRedirect(reverse('topic-page', args=[topic]))
