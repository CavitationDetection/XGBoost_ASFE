import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score,accuracy_score,recall_score,f1_score
from sklearn.metrics import auc
from sklearn.utils import shuffle

train_data = pd.read_csv("/home/yusha/yusha/cavitation2017/code/feature_classify/splitdata/Four/Features/Split20/train_split_feature10_transform.csv")
test_data = pd.read_csv("/home/yusha/yusha/cavitation2017/code/feature_classify/splitdata/Four/Features/Split20/test_split_feature10_transform.csv")

train_data = shuffle(train_data)
x_train = train_data.iloc[:,0:4961]  
y_train = train_data.iloc[:,-1]


x_test = test_data.iloc[:,0:4961]
y_test = test_data.iloc[:,-1]

train = [x_train,y_train]
test = [x_test,y_test]

model = xgb.XGBClassifier(learning_rate=0.01,n_estimators=134,max_depth=3,objective='multi:softmax',num_class=4)
model1 = model.fit(x_train,y_train,eval_set=[train,test],eval_metric=['mlogloss','merror']) 

model_pred = model.predict(x_test)
model_prob = model.predict_proba(x_test)
precision_macro = precision_score(y_test,model_pred)
accuracy = accuracy_score(y_test,model_pred)
recall_macro = recall_score(y_test,model_pred)
auc = metrics.roc_auc_score(y_test,model_prob)
report_classification = classification_report(y_test,model_pred,target_names=['Cavitation-Chocked Flow','Constant Cavitation','Incipient Cavitation','No Cavitation'])


print('predit label:{}\n'.format(model_pred))
print('true label:{}\n'.format(y_test))
print("Accuracy:{}".format(accuracy))
print("Preciaion:{}".format(precision_macro)) 
print("Recall:{}".format(recall_macro))
print("f1:{}".format(f1_score(y_test,model_pred)))
print("AUC:{}".format(auc))
print(report_classification)


