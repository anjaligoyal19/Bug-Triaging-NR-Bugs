# Calculating top-1 accuracy
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

c=[]
for index, inst in enumerate(data_test):
    nb_predicted = nb_classifier.classify_instance(inst)

    print ("actual=", inst.get_string_value(inst.class_index))
    print ("1st predicted=",inst.class_attribute.value(int(nb_predicted)))
    if inst.get_string_value(inst.class_index)==inst.class_attribute.value(int(nb_predicted)):
        pass
        c.append("1")
    else:
        c.append("0")

counter=0
for index in range(0,len(c)):
    pass
    if c[index]=="1":
        pass
        counter=counter+1
print len(c)
print("Accuracy is:", (counter*100/len(c)))
jvm.stop()
