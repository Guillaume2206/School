from django.shortcuts import render
import logging
logger = logging.getLogger(__name__)

def error_404(request, exception):
  return render(request,'errors/404.html')

def error_500(request):
  return render(request,'errors/500.html')

def error_400(request, exception):
  return render(request,'errors/400.html')

def error_403(request, exception):
  return render(request,'errors/403.html')