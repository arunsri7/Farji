from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.documentation import include_docs_urls

from API.views import NewsItems, ReportNews, GetFakeNews, getFakeNews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/validate-news/', NewsItems),
    # url(r'^api/fake-news/', getFakeNews),
    url(r'^api/fake-news/', GetFakeNews.as_view()),
    url(r'^api/report-news/', ReportNews.as_view()),
    # url(r'^api/test/', test.as_view()),
    # url(r'^api/', include_docs_urls(title='Farji documentation')),
    url(r'^docs/', include_docs_urls(title='Farji documentation')),
]





#3111edae78f6492983bd0a6df945356e