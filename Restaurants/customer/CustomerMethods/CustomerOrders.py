# noinspection PyUnresolvedReferences
from manager.models import Table ,FinalOrder ,OrderFood ,CustomerOrder ,FoodItem

def getCustomerOrders(request):
    orders =  FinalOrder.objects.filter( customer_id = request.user)
    return orders
