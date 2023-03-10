from django.shortcuts import render

from django.http import HttpResponse, StreamingHttpResponse, FileResponse, \
    JsonResponse


def first_app(request):
    return HttpResponse('Hello my beauty world!')


def page(request, page_num):
    return HttpResponse(f'Вы на странице: {page_num}')


# def about(request):
#     return HttpResponse(f'{request.headers}')


def shr(request):
    return StreamingHttpResponse('Hello World!')


def img1(request):
    return FileResponse(open('1.jpg', 'rb'), as_attachment=True,
                        filename='123.jpg')


def json(request):
    data = {'cost': 14, 'title': 'brush'}
    return JsonResponse(data)


def portfolio(request):
    return render(request, 'project/portfolio.html')


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def about(request):
    return render(request, 'project/about.html', {'menu': menu,
                                            'title': 'Информация о сайте'})
def main(request):
    return render(request, 'project/main.html', {'menu': menu,
                                            'title': 'Главная страница'})
