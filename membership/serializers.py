from rest_framework.serializers import ModelSerializer
from .models import Member, Contact

class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
