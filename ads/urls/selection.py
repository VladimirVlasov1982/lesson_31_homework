from django.urls import path
from ads.views.selection import SelectionDetailView, SelectionListView, SelectionCreateView, SelectionUpdateView, \
    SelectionDeleteView

urlpatterns = [
    path("", SelectionListView.as_view(), name="selections"),
    path("<int:pk>/", SelectionDetailView.as_view(), name="selections-detail"),
    path("create/", SelectionCreateView.as_view(), name="selections-create"),
    path("<int:pk>/update/", SelectionUpdateView.as_view(), name="selections-update"),
    path("<int:pk>/delete/", SelectionDeleteView.as_view(), name="selections-delete"),
]
