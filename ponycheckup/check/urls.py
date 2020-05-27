from django.urls import path

from .views import EnterUrlView, ResultView, ResultAjaxView


app_name = "check"
urlpatterns = [
    path("", EnterUrlView.as_view(), name="enterurl"),
    path("result/", ResultView.as_view(), name="result"),
    path("result_ajax/", ResultAjaxView.as_view(), name="result_ajax"),
]
