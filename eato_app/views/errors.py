from django.shortcuts import render

def custom_404_view(request, exception):
    # Render custom 404 template
    # The status=404 parameter ensures the correct HTTP status code is sent
    return render(request, '404.html', status=404)
