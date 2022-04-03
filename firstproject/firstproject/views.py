from django.shortcuts import render, HttpResponse
from tuition.models import Contact
from django.views.generic import TemplateView

# create views
def home(request):
    if request.method=="GET":
        name = ['jubayer', 'rabiul', 'hossian', 'khalid']

    else:
        name = {}
    context = {
        'name':name,
    }
    return render(request, 'home.html', context)

class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg']="Welcome to our website"
        context['msg2']="Welcome to our website again"
        return context