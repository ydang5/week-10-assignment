from rest_framework import status, response, views
from foundation.models import StudentDb

class StudentDbDetail(views.APIView):
#     def get_object(self, name):
#         try:
#             return StudentDb.objects.get(name=name)
#         except Exception as e:
#             return response.Response(
#             status=status.HTTP_404_NOT_FOUND,
#             data = {
#                 'message': 'student not found',
#             }
#         )

    def get(self, request):
        try:
            StudentDb.objects.get(id=1)
        except Exception as e:
            return response.Response(
            status=status.HTTP_404_NOT_FOUND,
            data = {
                'message': 'studentdatabse is empty',
            }
        )
        studentdata = StudentDb.objects.all()
        return response.Response(
            status=status.HTTP_200_OK,
            data={
                'datum': studentdata
                }
            )
# http --form GET http://127.0.0.1:8000/studentdb
#code did not work, reason: Json serializable!!!

    def post(self, request):
        # name = request.data.get('name', None)
        student_number = request.data.get('student_number', None)
        student_number = str(student_number)
        age = request.data.get('age', None)

        try:
            StudentDb.objects.get(student_number=student_number)
            return response.Response(
            status=status.HTTP_409_CONFLICT,
            data = {
                'message': 'student number already existed',
            }
        )
        except Exception as e:

            studentdb = StudentDb.objects.create(
                    # student_name = name,
                    student_number = student_number,
                    age = age,
                )
            return response.Response( # Renders to content type as requested by the client.
                status=status.HTTP_200_OK,
                data={
                    'message': 'student added',
                }
            )
# http --form POST http://127.0.0.1:8000/studentdb student_number=12345 age=18
#code worked. However, could not add name!!!

class GetStudentAPIView(views.APIView):
    def get(self, request):
        student_number = request.data.get('student_number', None)
        student_number=int(student_number)
        try:
            StudentDb.objects.get(student_number=student_number)
        except Exception as e:
            return response.Response(
            status=status.HTTP_404_NOT_FOUND,
            data = {
                'message': 'student not found',
            }
        )
        studentdatum = StudentDb.objects.get(student_number=student_number)
        return response.Response(
            status=status.HTTP_200_OK,
            data={
                'datum': studentdatum
                }
            )
# http --form GET http://127.0.0.1:8000/studentdetail/<student_number>
#Code did not work for some reason!!

class UpdateStudentAPIView(views.APIView):
    def put(self, request):
        student_number = request.data.get('student_number', None)
        student_number=int(student_number)
        age=request.data.get('age',None)
        age =int(age)
        try:
            StudentDb.objects.get(student_number=student_number)
        except Exception as e:
            return response.Response(
            status=status.HTTP_404_NOT_FOUND,
            data = {
                'message': 'student not found',
            }
        )
        studentdatum = StudentDb.objects.filter(student_number=student_number).update(age=age)
        return response.Response(
            status=status.HTTP_200_OK,
            data={
                'datum': studentdatum
                }
            )
# http --form PUT http://127.0.0.1:8000/studentupdate/<student_number>/<age>
#Code did not work for some reason!!

class ClearStudentAPIView(views.APIView):
    def delete(self, request):
        delete = StudentDb.objects.all().delete()
        return response.Response(
        status=status.HTTP_200_OK,
        data = {
            'message': 'Student database deleted',
        }
    )
# http --form DELETE http://127.0.0.1:8000/studentdelete
#Code worked
