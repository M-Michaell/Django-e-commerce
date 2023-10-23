from django.urls import path,include
from django.contrib.auth.views import  LogoutView
from accounts.views import logout,CustomUserCreate,UserProfileView,UserProfileUpdateView,profile,DeleteUser
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.views import LogoutView

urlpatterns =[
    path("",include('django.contrib.auth.urls')),
    path('register/', CustomUserCreate.as_view(), name='accounts.create'),
    path("profile/<int:pk>/",login_required(UserProfileView.as_view()),name="account.profile"),
    path("profile/",profile,name="account.profile2"),
    path('profile/update/<int:pk>/', UserProfileUpdateView.as_view(), name='profile-update'),
    path('<int:pk>/delete', login_required(DeleteUser.as_view()), name='profile.delete'),

    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
]