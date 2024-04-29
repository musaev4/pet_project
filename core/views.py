from django.contrib.auth import logout, authenticate, login
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages

from .decorators import login_required, own_nfts
from .forms import LoginForm, RegisterForm
from .models import NFT, Collection, Tag

from django.contrib.auth.password_validation import validate_password


@login_required(login_url='/auth/login/')
def home(request):
    nft = NFT.objects.all()
    if "search" in request.GET:
        nft = nft.filter(title__icontains=request.GET.get('search'))
    paginator = Paginator(nft, 8)
    page = int(request.GET.get('page', 1))
    nft = paginator.get_page(page)
    return render(request, 'main.html', {'nft': nft})


@login_required()
def create_nft(request):
    if request.method == 'POST':
        collection_l = list(map(int, request.POST.get('collection')))
        tag_ids = list(map(int, request.POST.getlist('tags')))
        tags = Tag.objects.filter(id__in=tag_ids)
        image = request.FILES.get('image')
        collections = Collection.objects.filter(id__in=collection_l)
        data = {
            'title': request.POST.get('title'),
            'description': request.POST.get('description'),
        }

        nft = NFT.objects.create(**data, owner_id=request.user.id)

        nft.collections.add(*collections)
        nft.tags.add(*tags)

        nft.image.save(image.name, image)
        messages.success(request, f'The news "{nft.title}" has been successfully created!')
        return redirect('/')
    # else:
    #     messages.error(request, f'Correct errors below')

    collections = Collection.objects.all()
    tags = Tag.objects.all()
    nft = NFT.objects.all()
    context = {'nft': nft, 'collections': collections, 'tags': tags}

    return render(request, 'create_nft.html', context)


@login_required()
@own_nfts
def update_nft(request, id):
    nft = NFT.objects.get(id=id)
    collections = Collection.objects.all()
    tags = Tag.objects.all()
    if request.method == 'POST':
        collection_ids = None
        if request.POST.get('collections'):
            collection_ids = [int(i) for i in request.POST.get('collections')]
        collections.filter(id__in=collection_ids)
        tag_ids = None
        if request.POST.get('tags'):
            tag_ids = [int(i) for i in request.POST.get('tags')]
        tags.filter(id__in=tag_ids)
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        content_file = request.FILES.get('content_file')

        nft.title = title
        nft.description = description
        nft.collections.clear()
        if collection_ids:
            nft.collections.add(*collections)
        if tag_ids:
            nft.tags.add(*tags)

        if image:
            nft.image = image
        if content_file:
            nft.content_file = content_file
        nft.save()
        messages.success(request, f'The news "{nft.title}" has been successfully updated!')
        return redirect('/')

    return render(request, 'update_nft.html', {"nft": nft, 'collections': collections, 'tags': tags})


@login_required()
@own_nfts
def delete_nft(request, id):
    nft = NFT.objects.get(pk=id)
    nft.delete()
    return redirect('/')



def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome to workspace "{user.first_name} {user.last_name}"')
                return redirect('/')
            else:
                messages.error(request, 'The user does not exist or the password is incorrect.')
    else:
        form = LoginForm()

    return render(request, 'auth/login.html', {'form': form})



def user_logout(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('/')


def user_register(request):
    if request.user.is_authenticated:
        return redirect('/')

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to workspace "{user.first_name} {user.last_name}"')
            return redirect('/workspace/')

    return render(request, 'auth/register.html', {'form': form})
