from django.shortcuts import render

# Create your views here.
def edit(request):
    return render(request, 'editor/editor.html')