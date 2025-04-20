from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Muvaffaqiyatli ro'yxatdan o'tdingiz"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.authtoken.models import Token

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "message": "Muvaffaqiyatli kirildi!",
                "token": token.key
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class LogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Muvaffaqiyatli chiqildi"}, status=status.HTTP_200_OK)


class ProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class ProfileUpdateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Ma'lumotlar to'liq yangilandi"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Ma'lumotlar qisman yangilandi"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        user.delete()
        return Response({"message": "Akkount o'chirildi"}, status=status.HTTP_200_OK)