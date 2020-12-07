from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView , UpdateView, DeleteView
from main import models
# Django has 5 generic views.
# Django’s generic views really shine when it comes to presenting views of your database content.
# Because it’s such a common task, Django comes with a handful of built-in generic views to help
# generate list and detail views of objects.

# Django has code for mostly used views for database content so we don't have to write code for it.

# DetailView gives us detials of single instances of the model
# ListView - list all instances of models . example - list all college, students etc.
# create view - handles get and post requests of models
# update view - handles post request of updating
# Delete View

class index(View):
    #over writing get and post requests
    def get(self,request):
        return HttpResponse('<h1>ITS A GET REQUEST</h1>')

    def post(self,request):
        return HttpResponse('<h1>ITS A POST REQUEST</h1>')

class collegdetails(DetailView):
    # If we were to write the code ourselves then we would have to first get
    # college detials from the database using Query Manager and then
    # pass it using context .
    # but using detailView we just need to specify the model name
    # and it will be automatically passed to the template.
    model=models.college
    template_name='college_detailview.html'
    # Note that when we created detail view ourselves in blog porject we used pk attribute
    # as parameter but here it is not required . They are handled automatically.

class collegelist(ListView):
    model = models.college
    template_name = 'college_list.html'
    # Default name for context_object_name is objects in list view but we can overwrite it.
    context_object_name = 'colleges'

class CollegeCreate(CreateView): #creates a model form for us with 'form' context_object_name
    model = models.college
    template_name = 'college_create.html'
    fields = '__all__'
    success_url = '/college'

class CollegeUpdate(UpdateView):
    model = models.college
    template_name = 'college_create.html' #update is very good. It gives prefilled form,
    fields = '__all__'                    #prefilled with previous values.
    success_url = '/college'

class StudentCreate(CreateView):
    model = models.student
    template_name = 'student_create.html'
    fields = '__all__'
    success_url = '/'

class StudentDelete(DeleteView):
    model = models.student
    template_name = 'confirm.html'
    success_url = '/'
