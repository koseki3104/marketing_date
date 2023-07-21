from django.contrib import admin
from django.urls import path
from marketing_data_analytics.views import top_page, save_data, success_page, export_to_excel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', top_page, name='top_page'),
    path('save_data/', save_data, name='save_data'),
    path('success/', success_page, name='success_page'),
    path('export_to_excel/', export_to_excel, name='export_to_excel'),
]