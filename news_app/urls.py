from django.urls import path
from .views import homePageView,contactView,LocalNewsView,news_detail,EuroNewsView,TechnoNewsView,NewsCreateView, \
    NewsUpdateView,NewsDeleteView,SportNewsView,SiyosatNewsView

urlpatterns=[
    path('',homePageView,name='home-page'),
    path('news/create/',NewsCreateView.as_view(),name='news-create'),
    path('news/<slug>/edit/',NewsUpdateView.as_view(),name='news-edit'),
    path('news/<slug>/delete/',NewsDeleteView.as_view(),name='news-delete'),
    path('news/<slug:news>/',news_detail,name='news-detail'),
    path('local-news/',LocalNewsView.as_view(),name='local-news'),
    path('euro-news/',EuroNewsView.as_view(),name='euro-news'),
    path('techo-news/',TechnoNewsView.as_view(),name='techo-news'),
    path('sport-news/',SportNewsView.as_view(),name='sport-news'),
    path('siyosat/', SiyosatNewsView.as_view(), name='siyosat'),
    path('contact/',contactView,name='contact-page')
]
