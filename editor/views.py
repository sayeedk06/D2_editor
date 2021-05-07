from django.shortcuts import render,redirect
import uuid
# Create your views here.
def create(request):
    if "text_submission" in request.POST:
        print("It works")
        unique_id = uuid.uuid1()
        return redirect('show_text', unique_id=unique_id)
    else:
        return render(request, 'editor/editor.html')
def show(request, unique_id=None):
    return render(request, 'editor/editor.html', {
        'unique_id': unique_id 
    })

def edit(request, unique_id=None):
    if unique_id:
        print(unique_id)
        return render(request, 'editor/edit_text.html', {
            'prev_text': unique_id 
        })
