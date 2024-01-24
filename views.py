from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CardSerializer
from .models import Card
# Create your views here.

@api_view (['GET'])
def home(request):
    msg = {
        'message':"no point is here for getting any things use this '/api/product/' "
    }
    return Response(msg)

@api_view(['GET'])
def api(request):

    card = Card.objects.all()

    serializer = CardSerializer(card, many=True)
    return Response(serializer.data)