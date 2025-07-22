
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("home.urls")),
    path("explore/",include("explore.urls")),
    path("leaderboard/",include("leaderboard.urls")),
    path("community/",include("community.urls")),
    path("post_dare/",include("postdare.urls")),
    path("profile/",include("userprofile.urls")),
    path("login/",include("login.urls"))
]
