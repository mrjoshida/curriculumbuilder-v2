from django.shortcuts import render, get_object_or_404
from multiurl import ContinueResolving

from models import IDE, Block, Map
from curricula.models import Curriculum


def ide_view(request, slug):
    try:
        ide = IDE.objects.get(slug=slug)
    except IDE.DoesNotExist:
        raise ContinueResolving

    return render(request, 'documentation/ide.html', {'ide': ide})


def block_view(request, slug, ide_slug):
    try:
        ide = IDE.objects.get(slug=ide_slug)
    except IDE.DoesNotExist:
        raise ContinueResolving

    try:
        block = Block.objects.get(slug=slug, IDE=ide)
    except Block.DoesNotExist:
        raise ContinueResolving

    return render(request, 'documentation/block.html', {'code_block': block, 'ide': ide})


def embed_view(request, slug, ide_slug):
    try:
        ide = IDE.objects.get(slug=ide_slug)
    except IDE.DoesNotExist:
        raise ContinueResolving

    try:
        block = Block.objects.get(slug=slug, IDE=ide)
    except Block.DoesNotExist:
        raise ContinueResolving

    return render(request, 'documentation/embed.html', {'code_block': block, 'ide': ide})


def page_view(request, slug, curric_slug):
    try:
        page = Map.objects.get(slug=slug, parent__slug=curric_slug)
    except Map.DoesNotExist:
        raise ContinueResolving

    return render(request, 'documentation/page.html', {'page': page})


def maps_view(request, curric_slug):
    curriculum = Curriculum.objects.get(slug=curric_slug)
    maps = Map.objects.filter(parent__slug=curric_slug)
    return render(request, 'documentation/pages.html', {'curriculum': curriculum, 'pages': maps, 'type': 'Maps'})
