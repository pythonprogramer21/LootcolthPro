from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Shopdata

# Create your views here.
def home(request):
    #Shopdata.objects.all().delete()
    items = Shopdata.objects.all()#delete_info()
    return render(request, 'home.html',{'items': items})

def add_item(request):
    if request.method == 'POST':
        item = request.POST['product']
        size = request.POST['size']
        count = request.POST['count']
        if count and count.isdigit():
            data_queryset = Shopdata.objects.filter(item=item, size=size)
            if data_queryset.exists():
                pass
            else:
                Shopdata.objects.create(item=item, size=size, count=int(count))
        else:
            # Handle the case where count is not a valid integer
            # You might want to add a message or redirect the user
            pass

    return redirect('home')

def update_item(request):
    if request.method == 'POST':
        # Implement your logic to update data here
        item = request.POST['product1']
        size = request.POST['size1']
        count = request.POST['count1']
        if count and count.isdigit():
            data_queryset = Shopdata.objects.filter(item=item, size=size)

            if data_queryset.exists():
                # Get the first object from the queryset
                first_data_instance = data_queryset.first()

                # Access the count attribute of the first instance
                existing_count = int(first_data_instance.count)
                new_val=existing_count-int(count)
                # Now you can use the existing_count as needed
                #print(existing_count)
                data_queryset.update(count=new_val)
            else:
                # Handle the case where no matching data is found
                pass
            
    return redirect('home')
