from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from meal_tracker.meal.views.generic_views import unauthorized

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meal_tracker.meal.urls')),
    path('user/', include('meal_tracker.auth_user.urls')),
    path('unauthorized/', unauthorized, name='unauthorized'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = 'meal_tracker.meal.views.generic_views.handler400'
handler404 = 'meal_tracker.meal.views.generic_views.handler404'
handler500 = 'meal_tracker.meal.views.generic_views.handler500'
