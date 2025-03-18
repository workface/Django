from gc import get_objects
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from django.shortcuts import render
from bookmark.models import Bookmark


def bookmark_list(request):
    bookmarks = Bookmark.objects.filter(id__gte=50)
    # SELECT * FROM bookmark
    context = {'bookmarks': bookmarks}
    return render(request, 'bookmark_list.html', context)

def bookmark_detail(request, pk):
    # try:
    #     bookmark = Bookmark.objects.get(pk=pk)
    # except:
    #     raise Http404
    bookmark = get_object_or_404(Bookmark, pk=pk)
    return render(request,  'bookmark_detail.html', {'bookmark': bookmark})