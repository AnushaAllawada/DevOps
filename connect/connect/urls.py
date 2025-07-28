from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Createuser.views import *
from posts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Createuser.urls')),  # API routes for user management
    path('api/', include('posts.urls')),       # API routes for posts
    
    # Template-serving routes under /
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('profile/', profile_view, name='profile'),
    path('users/<str:username>/', user_detail_view, name='user_detail'),
    path('following/', following_view, name='following'),
    path('home/', HomeView.as_view(), name='home'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create-post/', CreatePostView.as_view(), name='create_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)