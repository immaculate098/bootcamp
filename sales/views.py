from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Sale
from .filters import ProductFilter
from .forms import MadeSaleForm, AddForm
from django.contrib.auth.decorators import login_required

@login_required
def manage(request):
    products = Product.objects.all().order_by('-id')
    product_filters = ProductFilter(request.GET, queryset=products)
    products = product_filters.qs
    return render(request, 'manage.html', {'products': products, 'products_filter': product_filters})

@login_required
def issue_item(request, pk):
    issued_item = Product.objects.get(id=pk)
    made_sales_form = MadeSaleForm()

    if request.method == "POST":
        made_sales_form = MadeSaleForm(request.POST)

        if made_sales_form.is_valid():
            new_sale = made_sales_form.save(commit=False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_price
            new_sale.save()

            issued_quantity = new_sale.quantity
            issued_item.total_quantity -= issued_quantity
            issued_item.save()

            return redirect('receipt_detail', receipt_id=new_sale.id)  

 

    return render(request, 'issue_item.html', {'made_sales_form': made_sales_form})



@login_required
def add_to_stock(request, pk):
    issued_item = Product.objects.get(id=pk)

    if request.method == 'POST':
        received_quantity_str = request.POST.get('received_quantity')
        if received_quantity_str is not None:
            try:
                received_quantity = int(received_quantity_str)
                issued_item.total_quantity += received_quantity
                issued_item.save()
                print(issued_item.total_quantity)
            
                return redirect('manage')
            except ValueError:
                
                pass
        else:
            
            pass

    return render(request, 'add_to_stock.html', {'issued_item': issued_item})



@login_required
def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_details.html', {'product': product})

@login_required
def receipt(request):
    sales = Sale.objects.all()
    return render(request, 'receipt.html', {'sales': sales})

@login_required
def receipt_detail(request, receipt_id):
    receipt = Sale.objects.get(id=receipt_id)
    return render(request, 'receipt_detail.html', {'receipt': receipt})


@login_required
def made_sales(request):
    sales = Sale.objects.all()
    total = sum(item.amount_received for item in sales)
    change = sum(item.get_change() for item in sales)
    net = total - change
    return render(request, 'made_sales.html', {'sales': sales, 'total': total, 'change': change, 'net': net})
