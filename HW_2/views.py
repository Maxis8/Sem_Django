from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, UpdateView
from .models import User, Order, Product
from .forms import UpProductForm


def my_view(request):
    context = {"name": "Welcome!"}
    return render(request, "HW_2/index.html", context)


class OrderProductsView(ListView):
    model = Order
    template_name = '/HW_2/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = User.objects.get(pk=self.kwargs['pk'])
        orders = Order.objects.filter(customer=customer).all()
        context['orders'] = orders
        return context


class ProductsByDateView(DetailView):
    model = Order
    template_name = 'HW_2/date_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = User.objects.get(pk=self.kwargs['pk'])
        orders = Order.objects.filter(customer=customer).all()

        context['orders'] = orders
        return context


class UpProductView(UpdateView):
    model = Product
    template_name = 'HW_2/up_product.html'
    form_class = UpProductForm


class ProductView(DetailView):
    model = Product
    template_name = 'HW_2/product_page.html'

