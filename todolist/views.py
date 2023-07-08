from django.shortcuts import render, redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from todolist.forms import ItemsForm
from django.contrib import messages
from todolist.models import Items
from django.core.paginator import Paginator
# Create your views here.

@method_decorator(login_required, name='dispatch')
class ItemsView(View):
    def get(self, request):
        all_item = Items.objects.all()
        p = Paginator(all_item, 3)  # creating a paginator object
        # getting the desired page number from url
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)  # returns the desired page object
        except PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            page_obj = p.page(1)
        except EmptyPage:
            # if page is empty then return last page
            page_obj = p.page(p.num_pages)
        context = {'page_obj': page_obj}
        # sending the page object to index.html
        all_item = Items.objects.all()
        return render(request, 'items.html', context={'user': request.user, 'page_obj': page_obj})


@method_decorator(login_required, name='dispatch')
class AddEditItemsView(View):
    def get(self, request, pk):
        if pk != 0:
            item = Items.objects.get(id=pk)
            form = ItemsForm(instance=item)
            return render(request, 'add-edit-item.html', context={'form': form})
        form = ItemsForm()
        return render(request, 'add-edit-item.html', context={'form': form})
    
    def post(self, request, pk):
        if pk !=0:
            item = Items.objects.get(id=pk)
            form = ItemsForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                messages.success(request=request, message='Item updated successfully!')
        else:
            form = ItemsForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                messages.success(request=request, message='Item added successfully!')
        return render(request, 'add-edit-item.html', context={'form': form})
    
@method_decorator(login_required, name='dispatch')
class DeleteItemsView(View):
    def get(self, request, pk):
        item = Items.objects.get(id=pk)
        item.delete()
        messages.success(request=request, message='Item deleted successfully !')
        return redirect('home')
