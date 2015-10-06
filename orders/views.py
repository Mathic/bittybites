from django.shortcuts import render
from django.http import Http404

from orders.models import Order
from orders.models import Flavors
from orders.models import Macaron

# Create your views here.
def index(request):
	title = 'Welcome'
	try:
		all_orders = Order.objects.all()
		flavors = Flavors.objects.all()[:3]
		if request.user.is_authenticated():
			title = "STFU %s" %(request.user)

		context = {
			"title": title,
			"all_orders": all_orders,
			"flavors": flavors,
		}
	except Order.DoesNotExist:
		raise Http404
	return render(request, "index.html", context)

def detail(request, order_id):
	try:
		order = Order.objects.get(pk=order_id)
	except Order.DoesNotExist:
		raise Http404
	return render(request, "detail.html", {'order': order})

def order(request):
	try:
		flavors = Flavors.objects.all()

		context = {
			"flavors": flavors,
		}
	except Flavors.DoesNotExist:
		raise Http404
	return render(request, "order.html", context)
