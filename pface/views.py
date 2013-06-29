from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
from .forms import GcodeFileForm
from .models import File
from .printrun.printcore import printcore

def printer(request):
    # process the file upload form
    if request.method == 'POST':
        form = GcodeFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = File(gcode_file = request.FILES['gcodefile'])
            new_file.save()
    else:
        form = GcodeFileForm()

    # Get the list of uploaded files
    files = File.objects.all()
    
    # Send everything to the template engine
    return render_to_response('pface/pface.html', {'files': files, 'form': form}, context_instance=RequestContext(request))

def command(request):
    if not request.is_ajax():
        return HttpResponse('Not allowed')
    command = request.body
    
def rmgcode(request, id):
    if not id:
        return HttpResponse('Nothing to delete. Please hit back.')
    try:
        file = File.objects.get(pk=int(id))
        file.delete()
    except:
        return HttpResponse('Object was not found!')
    
    return redirect('printer')
    
    
    
