from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

import pickle
import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd




