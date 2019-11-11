from rest_framework import status, response, views
from foundation.models import MilitaryDb

# Create your views here.
class AddMember(views.APIView):

    def post(self, request):

        name = request.data.get('name', None)
        age = request.data.get('age', None)
        has_glasses = request.data.get('has_glasses', None)
        try:
            age = int(age)
            has_glasses = bool(has_glasses)

        except Exception as e:
            return response.Response( # Renders to content type as requested by the client.
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    'message': 'please enter valid information',
                }
            )


        militarydb = MilitaryDb.objects.create(
                name = name,
                age = age,
                has_glasses = has_glasses
            )

        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'message': 'Member added',
            }
        )

#http --form POST http://127.0.0.1:8000/add name=Joe age=19 has_glasses=True
# Code worked
class AcceptanceAPI(views.APIView):

    def get(self, request):

        acceptance = MilitaryDb.objects.filter(age__gte=18).all()

        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'recurits who are accepted': acceptance,
            }
        )
#http --form GET http://127.0.0.1:8000/acceptance
# Code did not work: Object of type MilitaryDb is not JSON serializable!!!


class RejectionAPI(views.APIView):

    def get(self, request):

        rejection = MilitaryDb.objects.filter(age__lt=18).all()

        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'recurits who are rejected': rejection,
            }
        )

#http --form GET http://127.0.0.1:8000/rejection
# Code did not work: Object of type MilitaryDb is not JSON serializable!!!

class AirforceAPI(views.APIView):

    def get(self, request):

        airforce = MilitaryDb.objects.filter(age__gte=18, has_glasses=True).all()

        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'Airforce lsit': airforce,
            }
        )
#http --form GET http://127.0.0.1:8000/airforce
