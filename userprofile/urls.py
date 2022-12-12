from django.urls import path
from userprofile.views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'userprofile'

urlpatterns = [
    path('', show_profile, name='show_profile'),
    path('edit', edit_profile, name='edit_profile'),
    path('edit-profile-flutter', edit_profile_flutter, name='edit_profile_flutter'),
    path('json', show_json, name='show_json'),
    path('saldo', edit_saldo, name='edit_saldo'),
    path('topup', show_topup, name='show_topup'),
    path('json-flutter', show_json_flutter, name='show_json_flutter'),
    path('saldo-flutter', edit_saldo_flutter, name='edit_saldo_flutter')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
