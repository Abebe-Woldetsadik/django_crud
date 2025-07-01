from django.shortcuts import render, redirect
from . models import UserModel, Gender
from . forms import UserForm
# Create your views here.


def UserList(request):
    users = UserModel.objects.all()
    return render(request, 'crudapp/user_list.html', {'users': users})


def Create_Success(request):
    return render(request, 'create_success.html')


def Update_Success(request):
    return render(request, 'update_success.html')


def Delete_Success(request):
    return render(request, 'delete_success.html')


def UserCreate(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crudapp:create_success')
    else:
        form = UserForm()
    return render(request, 'crudapp/user_form.html', {'form': form})


def UserUpdate(request, pk):
    user = UserModel.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('crudapp:update_success')
    else:
        form = UserForm(instance=user)
    return render(request, 'crudapp/user_form.html', {'form': form})


def UserDelete(request, pk):
    user = UserModel.objects.get(pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('crudapp:delete_success')
    return render(request, 'crudapp/user_confirm_delete.html', {'user': user})


def UserDetail(request, pk):
    user = UserModel.objects.get(pk=pk)
    return render(request, 'crudapp/user_detail.html', {'user': user})
