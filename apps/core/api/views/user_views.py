from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.core.api.serializers.user_serializers import SetPasswordSerializer, UserSerializer
from apps.core.components import Paginator
from apps.core.models import User


@extend_schema(tags=['User', ])
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = Paginator

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(deleted=None)
        return queryset

    def dispatch(self, request, *args, **kwargs):
        if any(path in request.path for path in ['get-user-no-validate', 'set-password']):
            self.authentication_classes = []
            self.permission_classes = []
        return super().dispatch(request, *args, **kwargs)

    @action(detail=False, methods=['get'], url_path='get-user-no-validate')
    def get_user_no_validate(self, request):
        username = self.request.GET.get('username')
        user = User.objects.filter(username=username, password__exact='', last_login=None).first()
        if user:
            user_serializer = self.get_serializer(user)
            return Response({**user_serializer.data})
        return Response(status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'], url_path='set-password', serializer_class=SetPasswordSerializer)
    def set_password(self, request, pk=None):
        user: User = self.get_object()
        serializer = SetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        password = serializer.validated_data['password']
        user.set_password(password)
        user.is_active = True
        user.save()

        return Response({'status': 'senha atualizada com sucesso'}, status=status.HTTP_200_OK)
