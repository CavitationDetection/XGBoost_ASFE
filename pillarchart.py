'''
Description: 
Author: Yu Sha
Date: 2021-08-13 15:10:24
LastEditors: Yu Sha
LastEditTime: 2021-08-13 16:41:05
'''
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import MultipleLocator
data = pd.read_csv("./data/AccuracyCavitationDetectionDataset1.csv")

resnet = data['ResNet-18']*100
xgboost = data['XGBoost(ASFE)']*100
our = data['our']*100
svm = data['svm']*100
decision_tree = data['DT']*100
cnn = data['CNN']*100


# pillar = ['233472','259413','291840','333531','389120','466944','583680','778240','1167360','2334720']

pillar = ['2334720','1167360','778240','583680','466944','389120','333531','291840','259413','233472']
print(resnet)

xticks = np.arange(len(pillar))

fig,ax = plt.subplots(figsize=(14,9))
width = 0.14

svm_list = []
decision_tree_list = []
xgboost_list = []
cnn_list = []
resnet_list = []
our_list = []

for i in range(len(pillar)):
    svm_list.append(i)
    decision_tree_list.append(i+width)
    xgboost_list.append(i+2*width)
    cnn_list.append(i+3*width)
    resnet_list.append(i+4*width)
    our_list.append(i+5*width)


bar_svm = ax.bar(svm_list,svm, width = width, edgecolor="darkorange", facecolor="white", align='edge', hatch='/////', linewidth=2, label = "SVM")
bar_decision_tree = ax.bar(decision_tree_list, decision_tree, width = width, edgecolor = "lightseagreen", facecolor="white",align='edge', hatch='+++++',  linewidth=2,label='Decision Tree')
bar_xgboost = ax.bar(xgboost_list, xgboost, width = width, edgecolor = "darkgreen", facecolor="white",align='edge', hatch='-----', linewidth=2,label="XGBoost (ASFE)")
bar_cnn = ax.bar(cnn_list, cnn, width = width, edgecolor = "deeppink", facecolor="white",align='edge', hatch="xxxxx",  linewidth=2,label="1-D CNN")
bar_resnet = ax.bar(resnet_list, resnet, width = width, edgecolor = "darkblue", facecolor="white",align='edge', hatch='\\\\\\\\\\', linewidth=2,label="1-D ResNet-18")
bar_our = ax.bar(our_list, our, width = width, edgecolor = "red", facecolor="white",align='edge', hatch='.....', linewidth=2.2,label="1-D DHRN (our method)")



svm_list = []
decision_tree_list = []
xgboost_list = []
cnn_list = []
resnet_list = []
our_list = []

for i in range(len(pillar)):
    svm_list.append(i+0.06)
    decision_tree_list.append(i+width+0.06)
    xgboost_list.append(i+2*width+0.06)
    cnn_list.append(i+3*width+0.06)
    resnet_list.append(i+4*width+0.06)
    our_list.append(i+5*width+0.06)

line_svm = ax.plot(svm_list,svm,marker='p',ms = 7,linestyle='--',linewidth=1.5,markerfacecolor='darkorange', markeredgecolor='darkorange',color='darkorange',label="SVM")
line_decision_tree = ax.plot(decision_tree_list,decision_tree,marker='h',ms = 7,linestyle='--',linewidth=1.5,markerfacecolor='lightseagreen', markeredgecolor='lightseagreen',color='lightseagreen',label="Decision Tree")

line_xgboost = ax.plot(xgboost_list,xgboost,marker='v',ms =7,linestyle='--',linewidth=1.5,markerfacecolor='darkgreen', markeredgecolor='darkgreen',color='darkgreen',label="XGBoost (ASFE)")

line_cnn = ax.plot(cnn_list,cnn,marker='*',ms =7,linestyle='--',linewidth=1.5,markerfacecolor='deeppink', markeredgecolor='deeppink',color='deeppink',label="1-D CNN")

line_resnet = ax.plot(resnet_list,resnet,marker='o',ms = 7,linestyle='--',linewidth=1.5,markerfacecolor='darkblue', markeredgecolor='darkblue',color='darkblue',label="1-D ResNet-18")
line_our = ax.plot(our_list,our,marker='d',ms = 9,linestyle='-.',linewidth=2,markerfacecolor='red', markeredgecolor='red',color='red',label="1-D DHRN (our method)")

ax.set_xticks(xticks + 2.5*width)
ax.set_xticklabels(pillar,rotation=20)
font1 = {'family' : 'DejaVu Sans','size': 14}

handles1, labels1 = ax.get_legend_handles_labels()
handles2, labels2 = handles1[6:], labels1[6:]
handles1, labels1 = handles1[0:6], labels1[0:6]
ax.legend((*handles2, *handles1), (*len(labels1)*[''], *labels2),
             loc='upper right', ncol=2, handlelength=3, edgecolor='black',
             borderpad=0.7, handletextpad=1.5, columnspacing=0,prop=font1)
plt.xlabel("The Size of Sliding Window (${W_{size}}$)",fontdict={'family' : 'DejaVu Sans','size': 15})
plt.ylabel("Cavitation Detection Accuracy ($\%$)",fontdict={'family' : 'DejaVu Sans','size': 15})
plt.tick_params(labelsize=14,direction='in',right=True,top=True)
plt.ylim(70,110)
# plt.savefig("./figs/Bar.pdf")
plt.show()


