from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import GcodeFileForm
from .models import File
from printrun_app.printcore import printcore

def printer(request):
    if request.method == 'POST':
        form = GcodeFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = File(gcode_file = request.FILES['gcodefile'])
            new_file.save()
    else:
        form = GcodeFileForm()

    # Get the list of uploaded files
    files = File.objects.all()
   
    return render_to_response('pface/pface.html', {'files': files, 'form': form}, context_instance=RequestContext(request))
