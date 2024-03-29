from django.shortcuts import render
from . forms import MyForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import PredictMark
from . serializers import PredictMarkSerializer
import pickle
import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd




class PredictMarkView(viewsets.ModelViewSet):
	queryset = PredictMark.objects.all()
	serializer_class = PredictMarkSerializer
	

@api_view(["POST"])
def predictmark(request):
	try:
		#D:\school\BIAC\LinearRegression.pkl
		mdl=joblib.load("D:/school/BIAC/LinearRegression.pkl")
		#mydata=pd.read_excel('/Users/sahityasehgal/Documents/Coding/bankloan/test.xlsx')
		mydata=request.data
		print(mydata)
		unit=np.array(list(mydata.values()))
		unit=unit.reshape(1,-1)
		y_pred=mdl .predict(unit)
		saveResult(mydata,y_pred)
		return JsonResponse('Your Status is {}'.format(y_pred), safe=False)
	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
	


#output -> {'time_study': 6, 'num_course': 8089}
def saveResult(input, output) :
	pm = PredictMark()
	pm.time_study = input['time_study']
	pm.num_course = input['num_course']
	pm.final_mark = output
	pm.save()