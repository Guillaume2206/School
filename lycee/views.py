from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Cursus, Student, Presence
from .form import StudentForm, PresenceForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.shortcuts import get_object_or_404


#def index(request):
#  return HttpResponse("Racine de lycee")

# index : utilisation de HttpResponse
#def index(request):
#  result_list = Cursus.objects.order_by('name')
#  # chargement du template
#  template = loader.get_template('lycee/index.html')
#  # contexte
#  context = { 'liste' : result_list}
#  return HttpResponse(template.render(context, request))

# index : variante avec template intEgrE
def index (request):
  result_list = Cursus.objects.order_by('name')
  # contexte
  context = { 'liste' : result_list}
  # utilisation du template intEgrE
  return render (request, 'lycee/index.html', context)

def detail(request, cursus_id):
  result_list = Student.objects.filter(cursus=cursus_id)

  context = { 'liste' : result_list}

  return render (request, 'lycee/cursus/detail_cursus.html', context)

def detail_student(request,student_id):
    #result_list = Student.objects.get(pk=student_id)
    result_list = get_object_or_404(Student, pk=student_id)
    # context
    context = {'student': result_list}
    return render (request, 'lycee/student/detail_student.html' , context)

def call_of_roll(request,cursus_id):
    result_list = Student.objects.filter(cursus=cursus_id)
    context = {'student_list': result_list}
    return render (request, 'lycee/student/call_of_roll.html' , context)

class StudentCreateView(CreateView):
  # ref au modEle
  model = Student
  # ref au formulaire
  form_class = StudentForm
  # le nom du render
  template_name = "lycee/student/student_create_form.html"

  # page appelee si creation ok
  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))

class ParticularCallOfRollCreateView(CreateView):
  # ref au modEle
  model = Presence
  # ref au formulaire
  form_class = PresenceForm
  # le nom du render
  template_name = "lycee/student/particular_call_of_roll_form.html"

  # page appelee si creation ok
  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))

class StudentEditView(UpdateView):
  # ref au modEle
  model = Student
  # ref au formulaire
  form_class = PresenceForm
  # le nom du render
  template_name = "lycee/student/student_update_form.html"

  template_name_suffix = '_update_form'

  # page appelee si creation ok
  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))





  
    
