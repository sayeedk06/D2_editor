from django.shortcuts import render,redirect
from .models import TextData, TextHist
from .forms import TextDataForm,TextHisForm
from django.http import Http404
import uuid
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name
# creates a random id. If random id already exists, recursively creates another random id.
def random_id_gen():
    unique_code = uuid.uuid1()
    if TextData.objects.filter(text_url_id=unique_code):
        random_id_gen()
    else:
        return unique_code 

def findhis(id):
    list_his = []
    while(TextHist.objects.filter(current_text=id)):
        model = TextHist.objects.get(current_text=id)
        list_his.append(model.prev_text)
        id = model.prev_text
    return list_his
"""This function accepts form submission from a button(name='text_submission'),
creates a unique id for the text and saves the information in the database after form validation 
URL: '/' """
def create(request):
    if "text_submission" in request.POST:
        unique_id = random_id_gen()
        incoming_data = TextDataForm({
            'text': request.POST['text'],
            'text_url_id': unique_id
        })

        if incoming_data.is_valid():
            incoming_data.save()

        return redirect('show_text', unique_id=unique_id)
    else:
        return render(request, 'editor/editor.html')

"""This function gets the unique id from url. Then uses the unique id to find the 
text field with matching unique id and displayes it to the user
URL: '/<unique_id>' """
def show(request, unique_id=None):
    try:
        text_info = TextData.objects.get(text_url_id=unique_id)
        lexer = get_lexer_by_name("python", stripall=True)
        style = get_style_by_name('friendly')
        formatter = HtmlFormatter(style=style,linenos='inline',nobackground=True,lineseparator='<br>')
        formatted = highlight(text_info.text, lexer, formatter)

        history = findhis(unique_id)

        return render(request, 'editor/editor.html', {
        'unique_id': text_info.text_url_id,
        'text': formatted,
        'hist': history,
    })
    except TextData.DoesNotExist:
        raise Http404("No TextData matches the given query.")
        

"""if -> 
form submission from a button(name='text_submission') is received creates a new
text field by generating a unique id 
else ->
uses the unique id from the url to find the 
text field with matching unique id and displayes it to the user. And then lets them edit 
the existing text and save new text in the database with another unique id
URL: '/edit/<unique_id>' """
def edit(request, unique_id=None):
    if "text_submission" in request.POST:
        print(unique_id)
        unique_id = random_id_gen()
        
        incoming_data = TextDataForm({
            'text': request.POST['text'],
            'text_url_id': unique_id
        })
        print("prev_text", request.POST['prev_id'])
        print("Current_text", unique_id)
        form = TextHisForm({
                'prev_text': request.POST['prev_id'],
                'current_text': unique_id
            })
        if incoming_data.is_valid():
            incoming_data.save()
            
        if form.is_valid():
            form.save()
        else:
            print("This didn't work")

        return redirect('show_text', unique_id=unique_id)
    elif unique_id:
        text_info = TextData.objects.get(text_url_id=unique_id)
        history = findhis(unique_id)
        return render(request, 'editor/edit_text.html', {
            'prev_text': text_info.text,
            'prev_url_id': unique_id,
             'hist': history
        })
