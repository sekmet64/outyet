from django.http import HttpResponse
from models import TrustedUrl

def index(request):
    return HttpResponse('hello you')

def add_entry_by_url(request):
    return HttpResponse('added')

def trusted_url(request, url):
    if request.method == 'GET':
        try:
            trustedUrl = TrustedUrl.objects.get(url=url)
        except TrustedUrl.DoesNotExist:
            trustedUrl = parse_trusted_url(url)
        except TrustedUrl.MultipleObjectsReturned:
            pass
    return HttpResponse(trustedUrl)
            
def parse_trusted_url(url):
    pass
        