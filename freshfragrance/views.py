from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def error404_page(request):
    return render(request, 'templates/404.html')

def get_queryset(request):
    query = request.GET.get("q")
    if query:
        object_list = Post.objects.filter(ingredients__icontains=query)
        return render(request, 'templates/base.html', {'object_list': object_list})
    else:
        return render(request, '404.html')


    
