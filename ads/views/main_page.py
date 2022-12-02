from django.http import JsonResponse


def main(request):
    """Главная страница"""
    return JsonResponse({"status": "Ok"}, status=200)
