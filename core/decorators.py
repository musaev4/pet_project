from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from core.models import NFT


def login_required(login_url='/'):

    def inner_func_as_args(func):

        def inner_func(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.warning(request, 'You should be authenticated!')
                return redirect(login_url)
            return func(request, *args, **kwargs)

        return inner_func

    return inner_func_as_args


def own_nfts(func):

    def inner_func(request, id, *args, **kwargs):
        user = request.user
        nft = get_object_or_404(NFT, id=id)
        if user != nft.owner:
            messages.warning(request, 'You cannot make any actions, it\'s not your news.')
            return redirect('/')

        return func(request, id, *args, **kwargs)

    return inner_func