from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

# Create your views / business logic here👇.

def home_view(request):
    return render(request, 'testapp/index.html')

class HelloWorld(View):
    def get(self, request):
        return HttpResponse('<h1 style="color:yellow; backGround:black; text-align:center; padding:12px;">This response is comming from Class Base View(CBV)</h1>')
        

class TemplateCBV(TemplateView):
    template_name = 'testapp/result.html'


# Send context Dictionary sing CBV
class TemplateCBV2(TemplateCBV):
    template_name = 'testapp/outcome.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['name'] = 'Sajjad Ali'
        context['rollno'] = 128
        context['course'] = 'Full Stack Python'

        return context
