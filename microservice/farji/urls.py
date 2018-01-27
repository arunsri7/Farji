from django.conf.urls import url, include
from django.contrib import admin

# from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from API.views import NewsItems

# router = routers.DefaultRouter()
# router.register(r'test', NewsItems, base_name="NewsItems")
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api/', include(router.urls)),
    url(r'^api/validate-news/', NewsItems),
    url(r'^api/', include_docs_urls(title='Farji documentation')),
    url(r'^docs/', include_docs_urls(title='Farji documentation')),
]





#3111edae78f6492983bd0a6df945356e