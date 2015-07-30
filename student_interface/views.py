# Create your views here.
from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from student_interface.models import Student,Subject,linking
import json
from django.db.models import Q


def first(request):
	return render_to_response('start.html', {})

def search(request):
	tmp=request.GET
	if(tmp):
		res1=list(Student.objects.filter(first_name = tmp["firstname"]))+list(Student.objects.filter(last_name =tmp["lastname"]))
		x={}
		for i in res1: x[i]=1
		res1=[]
		for i in x.keys(): res1.append(i)
		res=[]
		for i in res1:
			p={}
			p["firstname"]=(i.first_name)
			p["lastname"]=(i.last_name)
			p["gpa"]=(i.gpa)
			l=linking.objects.filter(student=i)
			x={}
			for j in l:
				x[j.subject.name]=j.grade
			p["marks"]=x
			res.append(p)
		return render(request,'result.html',{"res":res})
	else:	return render_to_response('search.html', {})

def result(request):
	tmp=request.GET
	res=Student.objects.filter(first_name = tmp[firstname])+Student.objects.filter(last_name =tmp[lastname])
	return render(request,'result.html',{"searchresults":res})