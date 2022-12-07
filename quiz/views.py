from django.shortcuts import render

from quiz.forms import TestForm


# Create your views here.
def show_test_form(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            data = form.cleaned_data
            context = {'form': TestForm, 'text': str(data)}
    else:
        context = {'form': TestForm}

    return render(request,
                  template_name='test.html',
                  context=context)

