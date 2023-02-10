from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from UserApp.models import User
from UserApp.serializers import UserSerializer

@csrf_exempt
def userAPI(request, id=0):
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data,safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse('Add Sucessfully', safe=False)
        return JsonResponse('Failed')
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(id=id)
        user.__dict__.update({ **user.__dict__, **user_data})
        users_serializer = UserSerializer(user, data=user.__dict__)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse('Update Sucessfully', safe=False)
        return JsonResponse('Failed')
    elif request.method == 'DELETE':
        user = User.objects.get(id=id)
        user.delete()
        return JsonResponse('Deleted Sucessfully', safe=False)
