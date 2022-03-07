# XGBoost_ASFE
[[Project Page]](https://www.sciencedirect.com/science/article/abs/pii/S0263224122001798) || [[arXiv]](https://arxiv.org/abs/2202.13226)

A novel acoustic signal cavitation detection framework–based on XGBoost with adaptive selection feature engineering–is proposed. Firstly, a data augmentation method with non-overlapping sliding window (NOSW) is developed to solve few-shot learning problem involved in this study. Then, the each segmented piece of time-domain acoustic signal is transformed by fast fourier transform (FFT) and its statistical features are extracted to be the input to the adaptive selection feature engineering (ASFE) procedure, where the adaptive feature aggregation and feature crosses are performed. Finally, with the selected features the XGBoost algorithm is trained for cavitation detection and tested on valve acoustic signal data provided by Samson AG (Frankfurt). Our method has achieved state-of-the-art results. The prediction performance on the binary classification (cavitation and no-cavitation) and the four-class classification (cavitation choked flow, constant cavitation, incipient cavitation and no-cavitation) are satisfactory and outperform the traditional XGBoost by 4.67% and 11.11% increase of the accuracy.
<br>
![image](https://github.com/CavitationDetection/XGBoost_ASFE/blob/main/FeatureAggregation.png)
Figure 1: The diagram of the adaptive feature aggregation.
<br>
![image](https://github.com/CavitationDetection/XGBoost_ASFE/blob/main/FeatureCrosses.png)
Figure 2: The diagram of the adaptive feature crosses.

Requirements
------------
Python3.6.13<br>
Numpy1.17.0<br>
Pandas1.1.5<br>
xgboost1.4.2<br>


## Updates

[7.2.2022] For the time being, All codes are uploaded.

[7.3.2022] Adding a citation for a preprinted version. Our paper has been accepted by Measurement Journal.

[8.3.2022] Adding Add a link to our paper (Measurement Journal and arXiv).


For any queries, please feel free to contact YuSha et al. through yusha20211001@gmail.com

## Citation
If you find our work useful in your research, please consider citing:
```
@article{sha2022acoustic,
  title={An acoustic signal cavitation detection framework based on XGBoost with adaptive selection feature engineering},
  author={Sha, Yu and Faber, Johannes and Gou, Shuiping and Liu, Bo and Li, Wei and Shramm, Stefan and Stoecker, Horst and Steckenreiter, Thomas and Vnucec, Domagoj and Wetzstein, Nadine and Widl Andreas and Zhou Kai},
  journal={Measurement},
  pages={110897},
  year={2022},
  publisher={Elsevier}
}
```


