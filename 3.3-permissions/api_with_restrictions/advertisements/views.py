from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django_filters import rest_framework as filters

from .models import Advertisement
from .serializers import AdvertisementSerializer, FavoriteSerializer, UserAdvertisementSerializer
from .permissions import IsAdminOrOwnerOrReadOnly
from .filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsAdminOrOwnerOrReadOnly()]
        return []

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = AdvertisementSerializer(instance)
        if instance.status == 'DRAFT':
            if request.user == instance.creator:
                return Response(serializer.data)
            raise PermissionDenied
        return super().retrieve(request)

    def list(self, request, *args, **kwargs):
        queryset_with_draft = Advertisement.objects.all()
        queryset_without_draft = Advertisement.objects.exclude(status='DRAFT')
        if request.user.is_anonymous:
            serializer = self.AdvertisementSerializer(queryset_without_draft, many=True)
            return Response(serializer.data)
        queryset = queryset_with_draft.filter(creator=request.user) | queryset_without_draft
        serializer = AdvertisementSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def favorites(self, request):
        user = request.user
        if user.is_anonymous:
            raise PermissionDenied
        serializer = UserAdvertisementSerializer(user)
        serializer.to_representation(user)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def favorite(self, request, pk=None):
        object = self.get_object()
        if request.user.id != object.creator.id and object.status != 'DRAFT':
            serializer = FavoriteSerializer(data=request.data, context={"request": request, "view": object})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        raise PermissionDenied





