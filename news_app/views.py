from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from .models import News, Category
from .forms import ContactForm


# Create your views here.

def homePageView(request):
    news_list = News.published.all().order_by('-publish_time')[:5]
    categories = Category.objects.all()
    local_news = News.published.all().filter(category__name='Mahalliy').order_by('-publish_time')[1:6]
    local_one = News.published.all().filter(category__name='Mahalliy').order_by('-publish_time')[:1]
    xorij_news = News.published.all().filter(category__name='Xorij').order_by('-publish_time')[1:6]
    xorij_one = News.published.all().filter(category__name='Xorij').order_by('-publish_time')[:1]
    sport_news = News.published.all().filter(category__name='Sport').order_by('-publish_time')[1:6]
    sport_one = News.published.all().filter(category__name='Sport').order_by('-publish_time')[:1]
    techno_news = News.published.all().filter(category__name='Texnologiya').order_by('-publish_time')[1:6]
    techno_one = News.published.all().filter(category__name='Texnologiya').order_by('-publish_time')[:1]
    politics_news = News.published.all().filter(category__name='Siyosat').order_by('-publish_time')[1:6]


    context = {
        'news_list': news_list,
        'categories': categories,
        'local_news': local_news,
        'local_one': local_one,
        'xorij_news': xorij_news,
        'xorij_one': xorij_one,
        'sport_news': sport_news,
        'sport_one': sport_one,
        'techno_news': techno_news,
        'techno_one': techno_one,
        'politics_news': politics_news,

    }

    return render(request, 'home.html', context)


class HomePageView(ListView):
    model = News
    template_name = 'home.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.model.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')[:5]
        context['local_news'] = News.published.all().filter(category__name='Mahalliy').order_by('-publish_time')[1:6]
        context['local_one'] = News.published.all().filter(category__name='Mahalliy').order_by('-publish_time')[:1]
        return context


def contactView(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponse("Biz bilan bog'langaningiz uchun rahmat!")
    context = {
        'form': form
    }
    return render(request, 'pages/contact.html', context)


def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        'news': news
    }
    return render(request, 'news/news_detail.html', context)


class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'pages/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST':
            form.is_valid()
            form.save()
            return HttpResponse("Xabar yuborildi")
        context = {
            'form': form
        }
        return render(request, 'pages/contact.html', context)


def notFountPage(request):
    return render(request, 'pages/404.html')


class LocalNewsView(ListView):
    model = News
    template_name = 'news/local_news.html'
    context_object_name = 'local_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Mahalliy")
        return news


class EuroNewsView(ListView):
    model = News
    template_name = 'news/euro_news.html'
    context_object_name = 'euro_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Xorij")
        return news


class TechnoNewsView(ListView):
    model = News
    template_name = 'news/techno_news.html'
    context_object_name = 'techno_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Texnologiya")
        return news


class SportNewsView(ListView):
    model = News
    template_name = 'news/sport_news.html'
    context_object_name = 'sport_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Sport")
        return news


class SiyosatNewsView(ListView):
    model = News
    template_name = 'news/politics_news.html'
    context_object_name = 'Siyosat'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Siyosat")
        return news




class NewsCreateView(CreateView):
    model = News
    template_name = 'crud/news_create.html'
    fields = ('title', 'slug', 'body', 'image', 'category', 'status')


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'crud/news_edit.html'
    fields = ('title', 'slug', 'body', 'image', 'category', 'status')


class NewsDeleteView(DeleteView):
    model = News
    template_name = 'crud/news_delete.html'
    success_url = reverse_lazy('home-page')