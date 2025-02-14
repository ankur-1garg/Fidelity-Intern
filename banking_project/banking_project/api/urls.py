from django.urls import path
from .views import AccountListCreate, AccountDetail, AccountDeposit, AccountWithdraw

urlpatterns = [
    path('accounts/', AccountListCreate.as_view(), name='account-list'),
    path('accounts/<int:pk>/', AccountDetail.as_view(), name='account-detail'),
    path('accounts/<int:pk>/deposit/',
         AccountDeposit.as_view(), name='account-deposit'),
    path('accounts/<int:pk>/withdraw/',
         AccountWithdraw.as_view(), name='account-withdraw'),
]
