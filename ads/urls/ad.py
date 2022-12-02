from django.urls import path
from ads.views.ad import AdsListView, get_ad_by_id, AdsCreateView, AdsUpdateView, AdsDeleteView, AdsUploadImage

urlpatterns = [
    path("", AdsListView.as_view(), name="ads"),
    path("<int:pk>/", get_ad_by_id, name="ads-detail"),
    path("create/", AdsCreateView.as_view(), name="ads-create"),
    path("<int:pk>/update/", AdsUpdateView.as_view(), name="ads-update"),
    path("<int:pk>/delete/", AdsDeleteView.as_view(), name="ads-delete"),
    path("<int:pk>/upload_image/", AdsUploadImage.as_view(), name="ads-upload_image"),
]
