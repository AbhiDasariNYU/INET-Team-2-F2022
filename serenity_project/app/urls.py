from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ScoreTableViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import logout

# from django.conf.urls import patterns,url
from . import views

# api router
api_router = DefaultRouter()
api_router.register("table", ScoreTableViewSet)

urlpatterns = [
    path("", views.index, name="home"),
    path("api/", include(api_router.urls)),
    path("search", views.search, name="search"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("rate/", views.submit_rating, name="rate"),
    path("thanks/", views.get_rating, name="thanks"),
    path("forumPosts", views.forum_home, name="forum_home"),
    path("addInForumPost/", views.addInForumPost, name="addInForumPost"),
    path("addInComment/", views.addInComment, name="addInComment"),
]

handler404 = "app.views.page_not_found_view"
handler500 = "app.views.internal_error_view"
