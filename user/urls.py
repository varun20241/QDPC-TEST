from django.contrib import admin
from django.urls import path,include
from .views.user_dashbord import UserDashboard
from .views.userlist_view import UserFetch,UserListView
from .views.user_approval import UserApprovalView
from .views.user_approval import UpdateUserStatusView
urlpatterns = [
 
path('user-dashboard/',UserDashboard.as_view(),name='user-dashboard'),
path('user-fetch/', UserFetch.as_view(), name='user-fetch'),
path('userlist/',UserListView.as_view(),name='user-list'),
path('user-update/<int:user_id>/', UserListView.as_view(), name='user-update'),
path('approve-user/<int:user_id>/', UserApprovalView.as_view(), name='approve-user'),
path('api/update-user-status/', UpdateUserStatusView.as_view(), name='update_user_status'),

 
]
