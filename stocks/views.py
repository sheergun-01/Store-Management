from django.shortcuts import render,redirect
from .forms import StockCreateForm,StockSearchForm,StockUpdateForm,IssueForm, ReceiveForm,ReorderLevelForm
from .models import Stock
from django.http import HttpResponse
import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request,'stocks/index.html')

@login_required
def item_list(request):
    if request.method == 'POST':
        form = StockSearchForm(request.POST)
        stock = Stock.objects.filter(category__icontains=form['category'].value(),product_name__icontains=form['product_name'].value())
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
            writer = csv.writer(response)
            writer.writerow(['CATEGORY', 'PRODUCT NAME', 'QUANTITY'])
            instance = stock
            for s in instance:
                writer.writerow([s.category, s.item_name, s.quantity])
            return response
        context = {
            'stock':stock,
            'form':form
            }
    else:
        form = StockSearchForm()
        stock = Stock.objects.all()
        context = {
            'stock':stock,
            'form':form
        }
    return render(request,'stocks/item_list.html',context)
@login_required
def add_item(request):
    
    if request.method == 'POST':
        form = StockCreateForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Successfully Added')
            form.save()
            return redirect('add_item')
    else:
        form = StockCreateForm()
    context = {'form':form}
    return render(request,'stocks/add_item.html',context)

@login_required
def update_item(request,pk):
    item = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=item)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated')
            return redirect('stocks:item_list')
    else:
        form = StockUpdateForm()
    context = {
        'form':form
    }
    return render(request,'stocks/add_item.html',context)

@login_required
def delete_item(request,pk):
    item = Stock.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('stocks:item_list')
    return render(request,'stocks/delete_item.html',{'item':item})

def stock_detail(request, pk):
	item = Stock.objects.get(id=pk)
	context = {
		"item": item,
	}
	return render(request, "stocks/stock_detail.html", context)

@login_required
def issue_item(request,pk):
    item = Stock.objects.get(id=pk)
    if request.method == 'POST':
        form = IssueForm(request.POST,instance=item)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.quantity -= instance.issue_quantity
            instance.issue_by = str(request.user)
            messages.success(request, "Issued SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.item_name) + "s now left in Store")
            instance.save()

        return redirect('stocks/stock_detail'+str(item.id))
    else:
        form = IssueForm()

    context = {
        "title": 'Issue ' + str(item.product_name),
        "item": item,
        "form": form,
        "username": 'Issue By: ' + str(request.user),
    }
    return render(request, "stocks/add_item.html", context)


@login_required
def receive_item(request, pk):
    item = Stock.objects.get(id=pk)
    if request.method == 'POST':
        form = ReceiveForm(request.POST,instance=item)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.quantity += instance.quantity_received
            instance.save()
            messages.success(request, "Received SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.product_name)+"s now in Store")
            return redirect('stocks/stock_detail'+str(instance.id))
    else:
        form = ReceiveForm()
    context = {
            "title": 'Receive ' + str(item.product_name),
            "instance": item,
            "form": form,
            "username": 'Receive By: ' + str(request.user),
        }
    return render(request, "stocks/add_item.html", context)

@login_required
def reorder_level(request,pk):
    item = Stock.objects.get(id=pk)
    if request.method == 'POST':
        form = ReorderLevelForm(request.POST,instance=item)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "Reorder level for " + str(instance.product_name) + " is updated to " + str(instance.reorder_level))
            return redirect("stocks:item_list")
    else:
        form = ReorderLevelForm()
    context = {
            "instance": item,
            "form": form,
        }
    return render(request, "stocks/add_item.html", context)