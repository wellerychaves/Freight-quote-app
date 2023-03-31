from rest_framework.views import APIView, Response, Request, status
from django.forms.models import model_to_dict

from .models import Order


class OrderView(APIView):
    def get(self, request: Request) -> Response:
        orders = Order.objects.all()

        orders_list = []

        for order in orders:
            orders_dict = model_to_dict(order)
            orders_list.append(orders_dict)

        return Response(orders_list, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        order = Order.objects.create(**request.data)
        order_list = model_to_dict(order)

        return Response(order_list, status.HTTP_201_CREATED)
