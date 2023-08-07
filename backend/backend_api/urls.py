# urls.py

from django.urls import path
from backend_api.views import UserRegistrationView, UserLoginView, UserProfileView,SortedInputView,AllInputView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/', UserProfileView.as_view()),
    path('searchinput/', SortedInputView.as_view()),
    path('allinput/', AllInputView.as_view()),

]
