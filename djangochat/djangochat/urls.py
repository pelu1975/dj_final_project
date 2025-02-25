from django.contrib import admin
from django.urls import path, include
from pages.urls import pages_patterns
from profiles.urls import profiles_patterns
from messenger.urls import messenger_patterns
from django.conf import settings

urlpatterns = [
    path('', include('core.urls')),
    path('rooms/', include('room.urls')),
    path('todo/', include('todo_app.urls')),
    
    path('admin/', admin.site.urls),
    # Paths de Auth
    path('pages/', include(pages_patterns)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    # Paths de profiles
    path('profiles/', include(profiles_patterns)),
    # Paths de Messenger
    path('messenger/', include(messenger_patterns)),

]
