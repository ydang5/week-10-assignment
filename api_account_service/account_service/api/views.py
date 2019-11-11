from rest_framework import status, response, views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class AccountLoginAPI(views.APIView):
    def post(self, request):

        username = request.data.get('username', None)
        password = request.data.get('password', None)


        try:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return response.Response(
                status=status.HTTP_200_OK,
                data = {
                    'message': 'Login success',
                })
            else:
                return response.Response(
                status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                data = {
                    'message': 'Cannot log in, username or password is wrong.',
                })
        except Exception as e:

            return response.Response(
            status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
            data = {
                'message': 'Cannot log in, username or password is wrong.',
            })
# http --form POST http://127.0.0.1:8000/login username=yi password=123

class AccountRegisterAPI(views.APIView):

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        first_name = request.data.get('first_name', None)
        last_name = request.data.get('last_name', None)
        email = request.data.get('email', None)

        try:
            user = User.objects.create_user(username, email, password)
            user.last_name = last_name
            user.first_name = first_name
            user.save()

            return response.Response(
            status=status.HTTP_201_CREATED,
            data = {
                'message': 'User acoount created',
            })
        except Exception as e:

            return response.Response(
            status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
            data = {
                'message': 'Cannot create user, username already existed',
            })
# http --form POST http://127.0.0.1:8000/register username=yi password=123 first_name=yi last_name=dang email=y@y.com


class AccountDetailAPI(views.APIView):
    def get(self, request):
        try:
            user = User.objects.all()

            return response.Response(
            status=status.HTTP_200_OK,
            data = {
                'User account detail:': user,
            })

        except Exception as e:
            return response.Response(
            status=status.HTTP_404_NOT_FOUND,
            data = {
                'message': 'Please login first',
            })
# http --form GET http://127.0.0.1:8000/detail
# Code did not work: Object of type User is not JSON serializable

class ChangePasswordAPI(views.APIView):
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('new_password', None)
        try:
            user = authenticate(username=username, password=password)
            user = User.objects.get(username=username)
            user.set_password('new_password')
            user.save()
            return response.Response(
            status=status.HTTP_200_OK,
            data = {
                'message:': 'password reset',
            })
        except Exception as e:

            return response.Response(
            status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
            data = {
                'message': 'Please enter valid username',
            })
 #http --form POST http://127.0.0.1:8000/changepassword username=yi new_password=123
