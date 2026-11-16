from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Main page</h1>")


def posts(request, post_id):
    return HttpResponse(f"<h1>Post</h1><p>id: {post_id}</p>")


def posts_by_slug(request, post_slug):
    return HttpResponse(f"<h1>Post</h1><p>slug: {post_slug}</p>")
