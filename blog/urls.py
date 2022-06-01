from django.urls import path

from .views import calc_page, index_page

urlpatterns = [
    # path("<int:id>/", index_page),
    # path("calc/<str:name>/", calc_page),
    path("", index_page, name="index_page"),
    path("calc/", calc_page, name="calc_page"),
    # path("test/", test_page, name="test_page"),
]