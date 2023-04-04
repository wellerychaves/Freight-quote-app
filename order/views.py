from datetime import datetime
import re

from rest_framework.views import APIView, Response, Request, status
from django.forms.models import model_to_dict

from .models import Order
from .serializers import OrderSerializer


class OrderView(APIView):
    def get(self, request: Request) -> Response:
        orders = Order.objects.all()

        orders_list = []

        for order in orders:
            orders_dict = model_to_dict(order)
            orders_list.append(orders_dict)

        return Response(orders_list, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        # logica que adiciona a data atual como número para order.
        now = str(datetime.now())
        now = now[7:-3]
        now = int(re.sub(r"[-:. ]", "", now))
        request.data["number"] = now
        # ...

        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order = Order.objects.create(**serializer.validated_data)

        serializer = OrderSerializer(order)

        return Response(serializer.data, status.HTTP_201_CREATED)
