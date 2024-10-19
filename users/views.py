from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm

def user_list(request):
    # Fetch all users from the database
    users = UserProfile.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

def user_create(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # Save the form and redirect to the list view
            form.save()
            return redirect('user_list')  # Correct redirection to user list
    else:
        form = UserProfileForm()  # Provide an empty form for GET request
    return render(request, 'users/user_form.html', {'form': form})

def user_update(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Correct redirection to user list
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')  # Correct redirection to user list
    return render(request, 'users/user_confirm_delete.html', {'user': user})
