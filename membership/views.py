from rest_framework.response import Response
from rest_framework.decorators import api_view
from membership.serializers import MemberSerializer, ContactSerializer
from rest_framework import status
from membership.models import Member, Contact

@api_view(['GET'])
def id_maker(request):
    id = Member.objects.all().count()
    return Response({"id": id+1})


@api_view(['GET'])
def contact(request):
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def register(request):
    serializer = MemberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data="Details submitted successfully!")
    return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data="Something went wrong, try again!")