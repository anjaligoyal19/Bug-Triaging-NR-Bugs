# Calculating top-20 accuracy
import weka.core.jvm as jvm
from weka.classifiers import Classifier
from weka.core.converters import Loader
from weka.classifiers import Evaluation
from weka.core.dataset import Instances
from weka.core.dataset import Attribute
from weka.core.classes import Random
import numpy as np
import csv
jvm.start()

loader = Loader(classname="weka.core.converters.ArffLoader")
data_train =loader.load_file("R.arff")
data_train.class_index = data_train.num_attributes - 1

nb_classifier = Classifier(classname="weka.classifiers.bayes.NaiveBayes")
nb_classifier.build_classifier(data_train)

data_test =loader.load_file("NRF.arff")
data_test.class_is_last()

developerorderinarff=[]
with open('assignee_arff_order.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        developerorderinarff.append(str(row[0]))

def bubbleSort(arr1,arr2):
    n=len(arr1)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr1[j]<arr1[j+1]:
                temp1=arr1[j]
                arr1[j]=arr1[j+1]
                arr1[j+1]=temp1
                temp2=arr2[j]
                arr2[j]=arr2[j+1]
                arr2[j+1]=temp2
    return arr2

c=[]
for index, inst in enumerate(data_test):
    predictionDistribution = nb_classifier.distribution_for_instance(inst)
    developerorderinarffnew=[]
    for index1 in range(0,len(developerorderinarff)):
        pass
        developerorderinarffnew.append(developerorderinarff[index1])
    a=bubbleSort(predictionDistribution,developerorderinarffnew)
    counter=False
    for i in range(0,20):
        pass
        if (a[i]==inst.get_string_value(inst.class_index)):
            counter=True
    if counter==False:
        c.append("0")
    else:
        c.append("1")
print len(c)
counter1=0
for index in range(0,len(c)):
    pass
    if c[index]=="1":
        pass
        counter1=counter1+1

print("Accuracy is:", (counter1*100/len(c)))
jvm.stop()
