from django.http import HttpResponse
from .models import Student

def index (request):
    all_Students =Student.objects.all() #connect with database
    html=' '
    for student in all_Students: #put each row in student
        url= '/tadrebi/' + str(student.id) + '/'#get student id
        html += '<a href=" '+ url + '   ">' + student.username + '</a><br>'
        return HttpResponse (html)

        

def detail (request, student_id):
    return HttpResponse ("<h1>ID:"+ str (student_id) +"</h1>")
