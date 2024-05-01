from django.urls import path
import debug_toolbar
from django.urls import include
from . import views


urlpatterns = [
    path("login/", views.UserLogin.as_view(), name="login"),
    path("profile/", views.UserProfile.as_view(), name="profile"),
    path("face_auth/<int:pk>/", views.enable_face_auth, name="face_auth"),
    path("update_profile_pic/<int:pk>/", views.UpdateProfilePhoto.as_view(), name="update_profile_photo"),
    path("update_profile/<int:pk>/", views.UpdateProfile.as_view(), name="update_profile"),
    path("change_password/<int:pk>/", views.change_password, name="change_password"),
    path("logout/", views.user_logout, name="logout"),

    path('__debug__/', include(debug_toolbar.urls)),
]