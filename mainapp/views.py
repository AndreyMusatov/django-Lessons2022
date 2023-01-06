from django.views.generic import TemplateView
from django.http import response

# Create your views here.


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'


class courses_listView(TemplateView):
    template_name = 'mainapp/courseslist.html'


class Doc_siteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsView(TemplateView):
    template_name = 'mainapp/news.html '

