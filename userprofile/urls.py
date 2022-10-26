from django.urls import path
from userprofile.views import show_profile, edit_profile
from django.conf.urls.static import static
from django.conf import settings

app_name = 'userprofile'

urlpatterns = [
    path('', show_profile, name='show_profile'),
    path('edit', edit_profile, name='edit_profile')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
