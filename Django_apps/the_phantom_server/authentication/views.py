from django.shortcuts import render, redirect
from base64 import b64decode
import face_recognition
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from sesame.utils import get_token
from django.shortcuts import get_object_or_404
from django_descope.models import DescopeUser
from datetime import datetime
import logging

from django.http import HttpRequest
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

logger = logging.getLogger(__name__)


def user_login(request):

    if request.method == "POST":
        face_match = False
        image = request.POST.get("image_src")
        email_src = request.POST.get("email_src")
        is_face = request.POST.get("is_face_auth")

        if is_face == "true" and image and email_src:
            try:
                user = User.objects.get(email=email_src)
                if user:
                    profile = Profile.objects.get(user=user)
            except Exception as e:
                messages.success(request, "User not found, Please check your email!")
                return redirect("login")

            try:
                if profile.is_face_recohnisation:
                    data_uri = image
                    header, encoded = data_uri.split(",", 1)
                    data = b64decode(encoded)
                    auth_image_name = f"media/auth_user_photo/{user.first_name}_{user.last_name}_{profile.id}.png"
                    with open(auth_image_name, "wb") as f:
                        f.write(data)

                    got_image = face_recognition.load_image_file(auth_image_name)
                    auth_image_path = f"media/media/user_login/{user.first_name}_{user.last_name}_{profile.id}.png"
                    existing_image = face_recognition.load_image_file(auth_image_path)
                    got_image_facialfeatures = face_recognition.face_encodings(
                        got_image
                    )[0]
                    existing_image_facialfeatures = face_recognition.face_encodings(
                        existing_image
                    )[0]
                    results = face_recognition.compare_faces(
                        [existing_image_facialfeatures], got_image_facialfeatures
                    )

                    if results[0]:
                        face_match = True
                    else:
                        face_match = False

                    if face_match and user:
                        login(request, user)
                        token = get_token(user)
                        user = authenticate(sesame=token)
                        messages.success(
                            request,
                            f"Welcome {profile.user.first_name},You are Logged in Successfully!",
                        )
                        return redirect("home")
                messages.success(
                    request,
                    f"Doesn't Enable Face Auth, Please try to login with credentials.",
                )
                return redirect("login")

            except Exception as e:
                print(str(e))
                messages.success(request, "Something went wrong, Please try again!")
                return redirect("login")

        if is_face == "false":
            email = request.POST.get("email", None)
            password = request.POST.get("password", None)
            remember_me = (
                True if request.POST.get("remember_me", None) == "on" else False
            )
            user_data = User.objects.get(email=email)
            user = authenticate(username=email, password=password)
            if user:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                token = get_token(user)
                user = authenticate(sesame=token)
                messages.success(
                    request,
                    f"Welcome {user_data.first_name},You are Logged in Successfully!",
                )
                return redirect("home")
        messages.success(request, "Something went wrong, Please try again!")
    return render(request, "login.html")

class UserProfile(LoginRequiredMixin, View):
    template_name = "profile.html"

    def get(self, request, *args, **kwargs):
        user = request.user
        profile = Profile.objects.get(user=user)
        return render(request, self.template_name, {"profile": profile})
    
    def post(self, request, *args, **kwargs):
        try:
            user = request.user
            user = get_object_or_404(DescopeUser, id=user.id)
            profile = get_object_or_404(Profile, user=user)
            is_photo = True if request.POST.get("is_photo", None) == 'true' else False
            if is_photo:
                photo = request.FILES.get("fileToUpload")
                if photo and profile:
                    profile.profile_photo = photo
                    profile.save()
                    messages.info(request, "Profile Photo Updated Successfully")
                    return redirect("profile")
            else:
                email = request.POST.get("email", None)
                first_name = request.POST.get("first_name", None)
                last_name = request.POST.get("last_name", None)
                if email and first_name and last_name:
                    user.email = email
                    user.first_name = first_name
                    user.last_name = last_name
                    user.save()
                    messages.success(request, 'Profile has been updated successfully')
                    return redirect('profile')
            messages.success(request, 'Something went wrong, Please try again!')
            return redirect('profile')
        except Exception as e:
            messages.success(request, 'Something went wrong, Please try again!')
            return redirect('profile')

@login_required
def user_profile(request: HttpRequest):
    user = request.user
    profile = Profile.objects.get(user=user)
    return render(request, "profile.html", {"profile": profile})

def enable_face_auth(request, pk):
    if request.method == "POST":
        profile = get_object_or_404(Profile, id=pk)
        email = request.POST.get("email_enable", None)
        image_data = request.POST.get("image_src_enable", None)
        if profile.user.email == email and image_data:
            header, encoded = image_data.split(",", 1)
            data = b64decode(encoded)
            auth_image_name = f"media/media/user_login/{profile.user.first_name}_{profile.user.last_name}_{profile.id}.png"
            with open(auth_image_name, "wb") as f:
                f.write(data)
            profile.login_photo = f"/media/user_login/{profile.user.first_name}_{profile.user.last_name}_{profile.id}.png"
            profile.is_face_recohnisation = True
            profile.updated_at = datetime.now()
            profile.save()
            messages.info(request, "Face Auth Enabled Successfully")
        return redirect("profile")
    messages.info(request, "Something went wrong, Please try again!")
    return redirect("profile")

class UpdateProfilePhoto(View):
    def post(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, id=kwargs.get('pk'))
        photo = request.FILES.get("fileToUpload")
        if photo and profile:
            profile.profile_photo = photo
            profile.save()
            messages.info(request, "Profile Photo Updated Successfully")
            return redirect("profile")
        messages.info(request, "Something went wrong, Please try again!")
        return redirect("profile")

class UpdateProfile(View):
    def post(self, request, *args, **kwargs):
        user = get_object_or_404(DescopeUser, id=kwargs.get('pk'))
        email = request.POST.get("email", None)
        first_name = request.POST.get("first_name", None)
        last_name = request.POST.get("last_name", None)
        if email and first_name and last_name:
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.success(request, 'Profile has been updated successfully')
            return redirect('profile')
        messages.success(request, 'Something went wrong, Please try again!')
        return redirect('profile')

def update_profile(request: HttpRequest, pk):
    if request.method  == 'POST':
        user = get_object_or_404(DescopeUser, id=pk)
        email = request.POST.get("email", None)
        first_name = request.POST.get("first_name", None)
        last_name = request.POST.get("last_name", None)
        if email and first_name and last_name:
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.success(request, 'Profile has been updated successfully')
            return redirect('profile')
        messages.success(request, 'Something went wrong, Please try again!')
        return redirect('profile')
    return redirect('profile')

def change_password(request, pk):
    if request.method == "POST":
        user = get_object_or_404(User, id=pk)
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        if user:
            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                user = authenticate(username=user.email, password=new_password)
                if user:
                    login(request, user)
                    token = get_token(user)
                    user = authenticate(sesame=token)
                messages.info(request, "User Password has been changed Successfully")
                return redirect("profile")
            messages.info(request, "Your old password isn't matched.")
            return redirect("profile")
        messages.info(request, "User doesn't exists.")
        return redirect("profile")
    messages.info(request, "Something went wrong, Please try again!")
    return redirect("profile")

def user_logout(request: HttpRequest):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")

class UserLogin(View):
    template_name = "descope/descope_login.html"
    
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, self.template_name)
        