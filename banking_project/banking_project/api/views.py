from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Account
from .serializers import AccountSerializer
from rest_framework import viewsets


class AccountListCreate(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDeposit(APIView):
    def post(self, request, pk):
        try:
            account = Account.objects.get(pk=pk)
            amount = float(request.data.get('amount', 0))
            account.balance += amount
            account.save()
            return Response({
                'message': 'Deposit successful',
                'balance': account.balance
            })
        except:
            return Response({'error': 'Invalid operation'})


class AccountWithdraw(APIView):
    def post(self, request, pk):
        try:
            account = Account.objects.get(pk=pk)
            amount = float(request.data.get('amount', 0))
            if account.balance >= amount:
                account.balance -= amount
                account.save()
                return Response({
                    'message': 'Withdrawal successful',
                    'balance': account.balance
                })
            return Response({'error': 'Insufficient funds'})
        except:
            return Response({'error': 'Invalid operation'})
