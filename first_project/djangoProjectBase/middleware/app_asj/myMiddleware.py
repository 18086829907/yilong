from django.utils.deprecation import MiddlewareMixin
class MyMiddle(MiddlewareMixin):
    def process_request(self, request):
         print(request.GET.get('a'))
    def process_view(self, request, view_function, view_args, view_kwargs):
         pass
    def process_template_response(self, request, response):
         pass
    def process_response(self, request, response):
         return response