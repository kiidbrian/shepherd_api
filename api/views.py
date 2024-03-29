from rest_framework.response import Response
from api.models import User,Member,Attendance
from api.serializers import UserSerializer,MemberSerializer,AttendanceSerializer
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def user_list(request):
    """
    List all users, or create a new user.
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def user_detail(request,pk):
    """
    Retrieve, update or delete a user.
    """
    try:
         user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def member_list(request):
    """
    List all members, or create a new member.
    """
    if request.method == 'GET':
        members = Member.objects.all()
        serializer = MemberSerializer(members,many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def member_detail(request,pk):
    """
    Retrieve, update or delete a member.
    """
    try:
         member = Member.objects.get(pk=pk)
    except Member.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = MemberSerializer(user)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = MemberSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   