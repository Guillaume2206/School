from django.shortcuts import render
from django.http import HttpResponseForbidden
from .models import Cursus, Student, Presence, CallOfRoll
from .form import StudentForm, PresenceForm, CallOfRollForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from django.utils import timezone, dateformat

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
# index : variante avec template intEgrE
def index (request):
  checkUserAuth(request)
  result_list = Cursus.objects.order_by('name')
  group_list = request.user.groups.all()
  # contexte
  context = { 'liste' : result_list, 'groups': group_list}
  # utilisation du template intEgrE
  return render (request, 'lycee/index.html', context)

def detail(request, cursus_id):
  checkUserAuth(request)
  result_list = Student.objects.filter(cursus=cursus_id)

  context = { 'liste' : result_list}

  return render (request, 'lycee/cursus/detail_cursus.html', context)

def detail_student(request,student_id):
  checkUserAuth(request)
  #result_list = Student.objects.get(pk=student_id)
  result_list = get_object_or_404(Student, pk=student_id)
  # context
  context = {'student': result_list}
  return render (request, 'lycee/student/detail_student.html' , context)

def call_of_roll_history(request):
  cursus_list = Cursus.objects.all()
  group_list = request.user.groups.all()
  context = {'defaultdate': now(), 'cursus_list':cursus_list, 'groups': group_list}
  return render (request, 'lycee/callofroll/call_of_roll_history.html',context)

def call_of_roll_history_search(request):
  datecall = request.POST.get("searchdate")
  cursusid = request.POST.get("cursus")
  cursus = Cursus.objects.filter(id=cursusid)
  calls = CallOfRoll.objects.filter(date = datecall).filter(cursus=cursus[0])
  context = {'calls': calls, 'defaultdate': datecall, 'cursus':cursus[0]}
  return render (request, 'lycee/callofroll/call_of_roll_history_search.html' , context)

class StudentCreateView(CreateView):
  # ref au modEle
  model = Student
  # ref au formulaire
  form_class = StudentForm
  # le nom du render
  template_name = "lycee/student/student_create_form.html"

  # page appelee si creation ok
  def get_success_url(self):
    return reverse ("index", args=(self.object.pk,))

class CallOfRollView(CreateView):
  # ref au modEle
  model = CallOfRoll
  # ref au formulaire
  form_class = CallOfRollForm
  # le nom du render
  template_name = 'lycee/callofroll/call_of_roll.html'

  def get_context_data(self, **kwargs):
        ctx = super(CallOfRollView, self).get_context_data(**kwargs)
        cursus_id = self.kwargs['cursus_id']
        ctx['cursus'] = Cursus.objects.filter(id=cursus_id)[0]
        return ctx
  
  def get_form_kwargs(self):
        kwargs = super( CallOfRollView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)  # self.kwargs contains all url conf params
        return kwargs
        
  # Called page if creation success
  def get_success_url(self):
    return reverse ("index", args=(self.object.pk,))

  # When the form is submit, save it or redirect
  def form_valid(self, form):
      cursus_id = self.kwargs['cursus_id']
      dayhalf = self.request.POST.get("dayhalf")
      todaydate = dateformat.format(timezone.now(), 'Y-m-d')
      todayCOR = CallOfRoll.objects.filter(cursus=cursus_id, dayhalf=dayhalf, date=todaydate)
      
      if not todayCOR:
        students = Student.objects.filter(cursus=cursus_id)
        date = self.request.POST.get("date")
        cursus = Cursus.objects.filter(id=cursus_id)[0]
        count = 0
        for student in students:
          missing = self.request.POST.get(str(student.id), "off")
          call = CallOfRoll()
          call.date = date
          call.dayhalf = dayhalf
          call.student = student
          call.cursus = cursus
          if missing == "on" :
            call.isPresent = True
            count += 1
          else:
            call.isPresent = False
          call.save()
        context = {'count': count, 'total':len(students), 'cursus_name': Cursus.objects.filter(id=cursus_id)[0].name}
        return render (self.request, 'lycee/callofroll/call_of_rollOK.html', context)
      else:
        context = {'dayhalf': dayhalf ,'cursus_name': Cursus.objects.filter(id=cursus_id)[0].name}
        return render (self.request, 'lycee/callofroll/call_of_rollKO.html', context)

        

class ParticularCallOfRollCreateView(CreateView):
  # ref au modEle
  model = Presence
  # ref au formulaire
  form_class = PresenceForm
  # le nom du render
  template_name = "lycee/callofroll/particular_call_of_roll.html"

  # page appelee si creation ok
  def get_success_url(self):
    return reverse ("index", args=(self.object.pk,))

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

def checkUserAuth(request):
  if not request.user.is_authenticated:
    return HttpResponseForbidden()



  
    
