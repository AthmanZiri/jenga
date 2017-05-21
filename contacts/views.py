from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Contact, Contact_Group
from .forms import ContactForm, Contact_GroupForm

from django.contrib import messages


contact_object = Contact.objects.all()

@login_required(login_url='/login/')
def contact_list(request):
    contacts = contact_object
    return render(request, 'contacts.html', {'contacts': contacts})


@login_required(login_url='/login/')
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            id_number = form.cleaned_data['id_number']
            mobile = form.cleaned_data['mobile']
            category = form.cleaned_data['category']

            form.save()

            form = ContactForm()

            messages.success(request, "Successfully Created")
    else:
        form = ContactForm()
    return render(request, 'contact_create.html', {'form': form})


@login_required(login_url='/login/')
def contact_update(request):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            id_number = form.cleaned_data['id_number']
            mobile = form.cleaned_data['mobile']
            category = form.cleaned_data['category']

            form.save()

            form = ContactForm()

            messages.success(request, "Successfully Created")
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact_update.html', {'form': form})


@login_required(login_url='/login/')
def group_list(request):
    groups = contact_object
    return render(request, 'group_list.html', {'groups': groups})


@login_required(login_url='/login/')
def group_create(request):
    if request.method == 'POST':
        form = Contact_GroupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            # contact = form.cleaned_data['contact']

            form.save()

            form = Contact_GroupForm()
    else:
        form = Contact_GroupForm()
    return render(request, 'group_create.html', {'form': form})


@login_required(login_url='/login/')
def group_update(request):
    group = get_object_or_404(Contact_Group, pk=pk)
    if request.method == 'POST':
        form = Group_ContactForm(request.POST, instance=group)
        if form.is_valid():
            name = form.cleaned_data['name']
            # contact = form.cleaned_data['contact']

            form.save()

            form = Contact_GroupForm()
    else:
        form = Group_ContactForm(instance=group)
    return render(request, 'group_update.html', {'form': form})
