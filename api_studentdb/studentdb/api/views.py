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
        results = []
        for studentdatum in studentdata:
            results.append({
                'student_number': studentdatum.student_number,
                'first_name': studentdatum.first_name,
                'last_name': studentdatum.last_name,
                'age':studentdatum.age,
            })

        return response.Response(
            status=status.HTTP_200_OK,
            data={
                'result': results,
                'count':StudentDb.objects.all().count()
                }
            )
# http --form GET http://127.0.0.1:8000/studentdb


class AddStudentAPIView(views.APIView):
    def post(self, request):
        first_name = request.data.get('first_name', None)
        last_name = request.data.get('last_name', None)
        student_number = request.data.get('student_number', None)
        age = request.data.get('age', None)
        print(first_name,last_name)

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
                    first_name = first_name,
                    last_name = last_name,
                    student_number = student_number,
                    age = int(age),
                )

            return response.Response( # Renders to content type as requested by the client.
                status=status.HTTP_200_OK,
                data={
                    'message': 'student added',
                }
            )
#  http --form POST http://127.0.0.1:8000/add first_name="yi" last_name="Dang" student_number=12345 age=18


class GetStudentAPIView(views.APIView):
    def get(self, request, student_number):
        student_number = request.data.get('student_number', None)
        print(student_number)
        # student_number=int(student_number)
        try:
            studentdatum=StudentDb.objects.get(student_number=int(student_number))
            print(studentdatum)

        except Exception as e:
            print(e)
            return response.Response(
            status=status.HTTP_404_NOT_FOUND,
            data = {
                'message': 'student not found',
            }
        )

        return response.Response(
            status=status.HTTP_200_OK,
            data={
                'student_number':studentdatum.student_number,
                'first_name': studentdatum.first_name,
                'last_name':studentdatum.last_name,
                'age':student.age,
                }
            )
# http --form GET http://127.0.0.1:8000/studentdetail/<student_number>
#Code did not work for some reason!!

class UpdateStudentAPIView(views.APIView):
    def put(self, request, id):
        student_number = request.data.get('student_number', None)
        studentdatum = StudentDb.objects.get(student_number=int(student_number))
        first_name = request.data.get("first_name", None)
        last_name = request.data.get("last_name", None)
        age=request.data.get('age',None)
        age =int(age)

        studentdatum.first_name = first_name
        studentdatum.last_name = last_name
        studentdatum.age = int(age)
        studentdatum.save()


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
                'student_number':studentdatum.student_number,
                'first_name': studentdatum.first_name,
                'last_name':studentdatum.last_name,
                'age':student.age,
                }
            )
# http --form PUT http://127.0.0.1:8000/studentupdate/<student_number> first_name = joe last_name=dow age=10
#Code did not work for some reason!!

class ClearStudentAPIView(views.APIView):
    def delete(self, request, id):
        student_number = request.data.get('student_number', None)
        student_number=int(student_number)

        try:
            studentdatum = StudentDb.objects.get(student_number=int(student_number))
            delete = studentdatum.delete()
            return response.Response(
            status=status.HTTP_200_OK,
            data = {
                'message': 'Student datum deleted',
                }
            )
        except Exception as e:
            return response.Response(
            status=status.HTTP_404_NOT_FOUND,
            data = {
                'message': 'student not found',
            }
        )
# http --form DELETE http://127.0.0.1:8000/studentdelete/<student_number>
#Code worked
