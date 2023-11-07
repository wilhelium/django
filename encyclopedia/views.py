from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki_entry(request, page_title):
    wiki_content = util.get_entry(page_title)
    if wiki_content is None:
        wiki_content = f"Error. There is no page for '{ page_title }'"

    return render(request, "encyclopedia/wikiPage.html", {
        "markdown_content": wiki_content
    })
