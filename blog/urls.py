from django.urls import path
from .views import registration,redirect_to_user_profile,login_in,PostSearchResultsView
from .views import BlogListView, AboutPageView, ImputPageView,UserProfileView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('imput/', ImputPageView.as_view(), name='imput'),
    path('register/', registration, name='register'),
    path('user_profile/', UserProfileView.as_view(), name='user_profile'),
    path('registration_success/', redirect_to_user_profile, name='registration_success'),
    path('login/', login_in, name='login'),
    path('search/', PostSearchResultsView.as_view(), name='search_results'),  # Маршрут для обработки поиска

]
