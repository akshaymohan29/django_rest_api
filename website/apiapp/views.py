from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .serializers import StudentsSerilizer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView



# def Home(request):





class StudentsAPI(APIView):
    def get(self,request):
        student_objs=Student.objects.all()
        serializer=StudentsSerilizer(student_objs,many=True)
        return Response({'data':serializer.data})

    def post(self, request):


            data=request.data
            print(data)
            serilizer=StudentsSerilizer(data=request.data,partial=True)

            if not serilizer.is_valid():
                print(serilizer.errors)
                return Response({ 'errors':serilizer.errors})
            serilizer.save()
            return Response({'message':serilizer.data})

class StudentsAPI2(APIView):
    def put(self,request):
        try:

            student_obj=Student.objects.get(id=request.data['id'])
            print(student_obj)
            serilizer=StudentsSerilizer(student_obj,data=request.data)

            if not serilizer.is_valid():
                print(serilizer.errors)
                return Response({ 'errors':serilizer.errors})
            serilizer.save()
            return Response({'message':serilizer.data})
        except Exception:
            return Response({'message' :'invalid id'})

    def patch(self, request):
        try:

            student_obj=Student.objects.get(id=request.data['id'])
            print(student_obj)
            serilizer=StudentsSerilizer(student_obj,data=request.data,partial=True)

            if not serilizer.is_valid():
                print(serilizer.errors)
                return Response({ 'errors':serilizer.errors})
            serilizer.save()
            return Response({'message':serilizer.data})
        except Exception:
            return Response({'message' :'invalid id'})


    def delete(self, request):
        try:
            #u can also remove id from function and use this id=request.GET.get("id")
            student_obj=Student.objects.get(id=id)
            student_obj.delete()
            return Response({'message':'delete'})
        except Exception:
            return Response({'message' :'invalid id'})


# @api_view(['GET'])
# def home(request):
#     file=Student.objects.all() #all emement must be passed via serilizer or it will create error
#     serlilzer=StudentsSerilizer(file,many=True)
#     return Response({'payload':serlilzer.data})
#
# @api_view(['POST'])
# def post_students(request):
#     data=request.data
#     print(data)
#     serilizer=StudentsSerilizer(data=request.data,partial=True)
#
#     if not serilizer.is_valid():
#         print(serilizer.errors)
#         return Response({ 'errors':serilizer.errors})
#     serilizer.save()
#     return Response({'message':serilizer.data})
#
# @api_view(['PUT'])
# def put_students(request,id):
#     try:
#         student_obj=Student.objects.get(id=id)
#         print(student_obj)
#         serilizer=StudentsSerilizer(student_obj,data=request.data)
#
#         if not serilizer.is_valid():
#             print(serilizer.errors)
#             return Response({ 'errors':serilizer.errors})
#         serilizer.save()
#         return Response({'message':serilizer.data})
#     except Exception:
#         return Response({'message' :'invalid id'})
#
# @api_view(['DELETE'])
# def delete_students(request,id):
#     try:
#         #u can also remove id from function and use this id=request.GET.get("id")
#         student_obj=Student.objects.get(id=id)
#         student_obj.delete()
#         return Response({'message':'delete'})
#     except Exception:
#         return Response({'message' :'invalid id'})



# class StudentInfo( generics.ListCreateAPIView):
#     queryset=Student.objects.all()
#     serializer_class = StudentsSerilizer
# class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student
#     serializer_class = StudentsSerilizer
