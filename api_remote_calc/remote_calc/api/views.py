from rest_framework import status, response, views
from foundation.models import Memory


class GetVersion(views.APIView):

    def get(self, request):
        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'version': '0.1.0',
            }
        )


class AddNumber(views.APIView):

    def post(self, request):

        number = request.data.get('number', None)
        try:
            number = float(number)

        except Exception as e:
            return response.Response( # Renders to content type as requested by the client.
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    'message': 'Please enter a number = (value)',
                }
            )

        try:
            memory = Memory.objects.get(id =1)
        except Exception as e:
            memory = Memory.objects.create(
                id =1,
                saved_data = 0,
            )
        memory.saved_data = memory.saved_data + float(number)
        memory.save()

        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'message': 'added',
            }
        )


class ResultAPIView(views.APIView):

    def get(self, request):
        try:
            memory = Memory.objects.get(id =1)
        except Exception as e:
            memory = Memory.objects.create(
                id =1,
                saved_data = 0,
            )
        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'result': memory.saved_data
            }
        )


class ClearResult(views.APIView):

    def post(self, request):
        try:
            memory = Memory.objects.get(id =1)
        except Exception as e:
            memory = Memory.objects.create(
                id =1,
                saved_data = 0,
            )
        memory.saved_data = 0
        memory.save()

        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'result': memory.saved_data,
            }
        )
