from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki_entry(request, page_title):
    return render(request, "encyclopedia/wikiPage.html", {
        "markdown_content": util.get_entry(page_title)
    })
