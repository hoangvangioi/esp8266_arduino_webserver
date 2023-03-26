from django.http import JsonResponse


def handler404(request, exception):
    """
    Custom 404 error handler that returns a JSON response.
    """
    return JsonResponse({'error': 'Page not found.'}, status=404)