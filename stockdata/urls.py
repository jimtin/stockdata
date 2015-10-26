from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    url(r'^stock_analysis/', include('stock_analysis.urls', namespace="stock_analysis")),
    url(r'^admin/', include(admin.site.urls)),
]
