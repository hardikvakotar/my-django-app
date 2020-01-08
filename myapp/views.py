from django.http import HttpResponse, HttpResponseNotFound  
from django.template import loader  
from django.shortcuts import render  
from myapp.form import StudentForm  
from myapp.functions.function import handle_uploaded_file
from myapp.models import Student
import csv
from reportlab.pdfgen import canvas
# Create your views here.  

def bootstrap(request):
	return render(request,"index1.html")
def show(request):  
	name={'student':'hardik','roll':'121'}
	return HttpResponse(loader.get_template('index.html').render(name))
def index(request):
	if request.method=='POST':
		student=StudentForm(request.POST,request.FILES)
		if student.is_valid():
			handle_uploaded_file(request.FILES['file'])
			return HttpResponse("File uploaded successfully")
	else:
		student=StudentForm()
		return render(request,"index.html",{'form':student})
def getfile(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="file.csv"'
	employees = Student.objects.all()
	writer = csv.writer(response)
	for students in employees:
		writer.writerow([students.id,students.firstname,students.lastname])
	return response

def getpdf(request):
	response=HttpResponse(content_type='application/pdf')
	response['Content-Disposition']='attachment; filename="file.pdf"'
	p=canvas.Canvas(response)
	p.setFont("Times-Roman",55)
	p.drawString(100,700, "Hello, Javatpoint.")
	p.showPage()
	p.save()
	return response
		
	
def add(request):
	num1=int(request.GET['name1'])
	num2=int(request.GET['name2'])
	return render(request,"result.html",{'result':num1+num2,'num1':num1,'num2':num2})