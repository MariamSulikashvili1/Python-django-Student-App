
from formRegister.models import FormRegister


#  views

def register(request):
    if request.method == 'post':

        first_name = request.POST['fisrt_name']
        last_name = request.POST['last_name']
        username = request.POST['username']

        user = FormRegister.objects.create_user(username=username, first_name=first_name,
                                                last_name=last_name)
        user.save(commit=True);

        return redirect('/')
    else:
        return render(request, 'formRegister.html')