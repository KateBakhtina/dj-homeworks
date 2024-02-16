from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django_filters import rest_framework as filters

from .models import Advertisement
from .serializers import AdvertisementSerializer, FavoriteSerializer, UserAdvertisements
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

    @action(detail=False, methods=["get"])
    def favorites(self, request):
        user = request.user
        if user.is_anonymous:
            raise PermissionDenied
        serializer = UserAdvertisements(user)
        data = serializer.to_representation(user)
        return Response(data)

    @action(detail=True, methods=["post"])
    def favorite(self, request, pk=None):
        object = Advertisement.objects.get(pk=pk)
        if request.user.id != object.creator.id:
            serializer = FavoriteSerializer(data=request.data, context={"request": request, "view": object})

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        raise PermissionDenied





