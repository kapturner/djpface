from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
from .forms import GcodeFileForm
from .models import File
from .printrun.printcore import printcore
from . import PRONSOLE, print_http_response

def printer(request):
    '''
        Handle printer interface page display and gcode upload
    '''
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
    return render_to_response('pface/pface.html', 
                              {'files': files, 'form': form}, 
                              context_instance=RequestContext(request))

@print_http_response
def command(request):
    '''
        Send command to the printer (via pronsole)
    '''
    # Make sure its a post
    if request.method != 'POST':
        return HttpResponse('Not allowed')
    
    # Make sure its ajax
    if not request.is_ajax():
        return HttpResponse('Not allowed')
    
    # Grab the command
    command = request.POST['command_text']
    
    # print it to the console
    print '>>', command
    
    # python magic to call the right function
    if 'help ' in command:
        func = command.strip().replace(' ', '_')
        if hasattr(PRONSOLE, func):
            try:
                getattr(PRONSOLE, func)()
            except Exception as ex:
                print str(ex)
                print 'XX', command
        else:
            print 'XX', command
    else:
        func = 'do_' + command.strip().split()[0].lower()
        args = ' '.join(command.strip().split()[1:])
        if hasattr(PRONSOLE, func):
            try:
                getattr(PRONSOLE, func)(args)
            except Exception as ex:
                print str(ex)
                print 'XX', command
        else:
            print 'XX', command

def rmgcode(request, id=None):
    '''
        Handle removal of the gcode files
    '''
    if not id:
        return HttpResponse('Nothing to delete. Please hit back.')
    try:
        file = File.objects.get(pk=int(id))
        file.delete()
    except:
        return HttpResponse('Object was not found!')
    
    return redirect('printer')
    
    
    
