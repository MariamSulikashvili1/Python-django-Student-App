from users2 import views
from .models import Snippet
from django.contrib import messages

def usblog(request):
    snipps = Snippet.objects.all()
    return render(request, 'indexg.html', {'snipps': snipps})


def snippet_detail(request):
    form = SnippetForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user;
            obj.save()
            form = SnippetForm()
            messages.success(request, "Successfully created")

    return render(request, 'form.html', {'form': form})