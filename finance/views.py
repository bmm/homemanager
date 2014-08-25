from django.shortcuts import render

from finance.models import Provider 

def index(request):
  providers = Provider.objects.all()
  context = { 'providers' : providers}
  return render(request, 'finance/index.html', context)
