from django.urls import path, include

user_urlpatterns = {
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
}
