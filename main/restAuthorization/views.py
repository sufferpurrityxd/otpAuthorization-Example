from .services import send_otp_code
from .serializers import UserSerializer
from customUser.models import User
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from rest_framework.mixins import CreateModelMixin


class UserRegistration(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            code = send_otp_code(f'{serializer.validated_data["phonenumber"].replace("+", "")}')
            serializer.validated_data['code'] = code
            serializer.save()
