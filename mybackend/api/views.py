from django.http import JsonResponse

def get_data(request):
    data = {
        "message": "Hello from the backend!"
    }
    return JsonResponse(data)

def get_info(request):
    info = {
        "info": "This is some information from the API."
    }
    return JsonResponse(info)
