from django.views.generic import TemplateView
from django.http import response

# Create your views here.


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contacts"] = [
            {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHcrhA',
                'city': 'Санкт‑Петербург',
                'phone': '+7-999-11-11111',
                'email': 'geeklab@spb.ru',
                'addres': 'территория Петропавловская крепость, 3Ж',
            },{
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHX3xB',
                'city': 'Казань',
                'phone': '+7-999-22-22222',
                'email': 'geeklab@kz.ru',
                'addres': 'территория Кремль, 11, Казань, Республика Татарстан, Россия',
            },{
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHh9kD',
                'city': 'Москва',
                'phone': '+7-999-33-33333',
                'email': 'geeklab@msk.ru',
                'addres': 'Красная площадь, 7, Москва, Россия',
            },
        ]   
        return context



class courses_listView(TemplateView):
    template_name = 'mainapp/courseslist.html'


class Doc_siteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] =[
            {
                'title': 'Первая новость',
                'preview': 'превью к новсти один',
                'data': '2022-02-01'
            },{
                'title':'Вторая новость',
                'preview': 'превью к новсти Второй',
                'data': '2022-02-02'
            },{
                'title':'третья новость',
                'preview': 'превью к новсти третий',
                'data': '2022-02-03'
            },{
                'title':'Четыре новость',
                'preview': 'превью к новсти четыре',
                'data': '2022-02-04'
            },{
                'title':'пять новость',
                'preview': 'превью к новсти пятая',
                'data': '2022-02-05'
            },
        ] 
        return context
        

