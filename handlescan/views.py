from django.shortcuts import redirect, render
import os
from django.http import HttpResponse, Http404, HttpResponseRedirect

from qrgen.models import QrCode, File

# Create your views here.

def dynamic_code_scan(request, code_id, *args, **kwargs):
    qrcode = QrCode.objects.get(id=code_id)

    # getting the no of scans
    
    if qrcode.scan_count is not None:
        qrcode.scan_count += 1
    else:
        qrcode.scan_count = 1

    qrcode.save()

    # get the qrcode action_type
    uploads = ['pdf', 'biz', 'img']

    # if dynamic, these types won't autoredirect, will give us headache instead
    email_txt = ['eml', 'txt']
    print('type: ', qrcode.type)
    if qrcode.action_type not in uploads and qrcode.action_type not in email_txt:
        # get and redirect to the qrcode action_url
        print('qrcode.type not in uploads and qrcode.type not in email_txt')
        return redirect(qrcode.input_url)

    else:
        if qrcode.action_type == 'eml':

            # open the default mail app and compose main to the input email address

            return render(request, 'email.html', {'email':qrcode.input_url})
        
        elif qrcode.action_type == 'txt':

            # for text input
            # 
            # return redirect()
            pass
            
        else:
            # if it was an uploaded file (if qrcode.type in uploads)

            # get file_id from code
            file = File.objects.get(id=qrcode.file_id)
            return HttpResponseRedirect('handlescan:download', args=(qrcode.file_id,))

def download(request, pk):
    try:
        file = File.objects.get(id=pk)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = BASE_DIR + file.file.url
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response
    except:
        # return HttpResponse('File does not exit!!!')
        raise Http404
