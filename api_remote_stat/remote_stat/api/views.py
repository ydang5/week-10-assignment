from rest_framework import status, response, views
from foundation.models import Memory



class InputDataAPIView(views.APIView):

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

        memory = Memory.objects.create(
            value = number,
        )

        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'message': 'data stored',
            }
        )
# http --form POST http://127.0.0.1:8000/api/add number=10


class AverageAPIView(views.APIView):

    def get(self, request):
        items = Memory.objects.all()
        sum = 0
        for item in items:
            value = item.value

            sum = sum + value

        length = len(items)

        average = sum/length

        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'Average': average,
            }
        )
# http --form get http://127.0.0.1:8000/api/average


class MeanAPIView(views.APIView):

        def get(self, request):
            items = Memory.objects.all()
            sum = 0
            for item in items:
                value = item.value

                sum = sum + value

            length = len(items)

            mean = sum/length

            return response.Response( # Renders to content type as requested by the client.
                status=status.HTTP_200_OK,
                data={
                    'Mean': mean,
                }
            )
# http --form get http://127.0.0.1:8000/api/mean

class StatAPIView(views.APIView):

        def get(self, request):
            items = Memory.objects.all()
            sum = 0
            for item in items:
                value = item.value

                sum = sum + value

            length = len(items)

            average = sum/length

            return response.Response( # Renders to content type as requested by the client.
                status=status.HTTP_200_OK,
                data={
                    'Average': average,
                }
            )

        def get(self, request):
            items = Memory.objects.all()
            sum = 0
            for item in items:
                value = item.value

                sum = sum + value

            length = len(items)

            mean = sum/length

            return response.Response( # Renders to content type as requested by the client.
                status=status.HTTP_200_OK,
                data={
                    'Mean': mean,
                }
            )
# http --form get http://127.0.0.1:8000/api/stat


class ClearResult(views.APIView):

    def post(self, request):
        try:
            memory = Memory.objects.get(id =1)
        except Exception as e:
            memory = Memory.objects.create(
                id =1,
                saved_data = 0,
            )
        memory.value = 0
        memory.save()

        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'result': memory.value,
            }
        )
