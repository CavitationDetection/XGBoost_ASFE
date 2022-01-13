# XGBoost_ASFE
A novel acoustic signal cavitation detection framework–based on XGBoost with adaptive selection feature engineering–is proposed. Firstly, a data augmentation method with non-overlapping sliding window (NOSW) is developed to solve few-shot learning problem involved in this study. Then, the each segmented piece of time-domain acoustic signal is transformed by fast fourier transform (FFT) and its statistical features are extracted to be the input to the adaptive selection feature engineering (ASFE) procedure, where the adaptive feature aggregation and feature crosses are performed. Finally, with the selected features the XGBoost algorithm is trained for cavitation detection and tested on valve acoustic signal data provided by Samson AG (Frankfurt). Our method has achieved state-of-the-art results. The prediction performance on the binary classification (cavitation and no-cavitation) and the four-class classification (cavitation choked flow, constant cavitation, incipient cavitation and no-cavitation) are satisfactory and outperform the traditional XGBoost by 4.67% and 11.11% increase of the accuracy.
<br>
The diagram of the adaptive feature aggregation.The adaptive feature aggregation include the adaptive selection module and the feature aggregation module.
![image](https://github.com/CavitationDetection/XGBoost_ASFE/blob/main/FeatureAggregation.png)
<br>
The diagram of the adaptive feature crosses.
![image](https://github.com/CavitationDetection/XGBoost_ASFE/blob/main/FeatureCrosses.png)


Requirements
------------
Python3.6.13<br>
Numpy1.17.0<br>
Pandas1.1.5<br>
xgboost1.4.2<br>


