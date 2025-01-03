from django.utils.translation import activate

class SetLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lang = request.GET.get('lang')
        if lang:
            activate(lang)
        response = self.get_response(request)
        return response
