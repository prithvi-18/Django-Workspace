from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<str:post_id>/", views.detail, name="detail"),
    path("new-something-urls", views.new_urls_view, name="new_page_urls"),
    path("old-urls", views.old_urls_redrict, name="OLD_URL_REDIRECT"),
]