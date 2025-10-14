import stripe
from rest_framework import viewsets, status
from .serializer import CartSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import CartModel
from rest_framework.views import APIView
from products.models import Product
from rest_framework.response import Response
from dotenv import load_dotenv
import os



class CartView(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartModel.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartAction(APIView):
    permission_classes = [IsAuthenticated]

    def get_cart_response(self, user):
        cart_items = CartModel.objects.filter(user=user)
        serializer = CartSerializer(cart_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, product_id):
        product = Product.objects.get(id=product_id)
        cart_item, created = CartModel.objects.get_or_create(
            user = request.user,
            product = product,
            defaults={'quantity': 1}
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return self.get_cart_response(request.user)
    
    def patch(self, request, product_id):
        try:
            cart_item = CartModel.objects.get(user=request.user, product_id=product_id)
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
                return self.get_cart_response(request.user)
            else:
                cart_item.delete()
                return self.get_cart_response(request.user)
        except CartModel.DoesNotExist:
            return Response({'error': 'Item not in cart'}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, product_id=None):
        if product_id:
            CartModel.objects.filter(user=request.user, product_id=product_id).delete()
            return Response({
                'message': 'Product removed from cart',
                'cart': self.get_cart_response(request.user).data
            })
        else:
            CartModel.objects.filter(user=request.user).delete()
            return Response({
                'message': 'Cart cleared',
                'cart': self.get_cart_response(request.user).data
            })


load_dotenv()
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
stripe.api_key = STRIPE_SECRET_KEY

class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request,):
        cart_items = CartModel.objects.filter(user=request.user)

        line_items = [
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.product.title,
                    },
                    'unit_amount': int(item.product.price * 100),
                },
                'quantity': int(item.quantity),
            } for item in cart_items
        ]
        
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items,
                mode='payment',
                success_url='https://ecommerceapi/success',
                cancel_url='https://ecommerceapi/cancel'
            )
            return Response({'checkout_url': session.url})
        except stripe._error.InvalidRequestError as e:
            return Response({'error': str(e)}, status=400)
        