from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import home, HomeView
from django.views.generic import TemplateView
from tuition.views import PostListView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', home, name='home'),
    path('', PostListView.as_view(), name='homeview'),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('tuition/', include('tuition.urls')),
    path('session/', include('session.urls')),
    path('inbox/notifications/', include('notifications.urls', namespace="notifications")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
