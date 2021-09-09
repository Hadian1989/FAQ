from faq.views import HomePageView
from faq.views import show_categories
from django.urls import path


urlpatterns = [
    path(r'categories/', show_categories),
    path('', HomePageView.as_view(), name='home'),
    # path('', HomePageView.as_view(), name='home'),
]
