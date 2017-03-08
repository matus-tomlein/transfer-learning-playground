Train on test domain and choose only source samples that were classified correctly
==================================================================================

1. train a classifier just using the target domain
2. predict labels for the source domain
3. compare with real labels and choose only the samples that were predicted
   correctly
4. use the selected samples to train a classifier on the source domain
5. test on the target domain

## Transfer from edge to microwave sensortag

```
             precision    recall  f1-score   support

        0.0       0.73      0.67      0.70       111
        1.0       0.24      0.84      0.38        37
        2.0       1.00      0.01      0.02       110
        3.0       0.63      1.00      0.77        48

avg / total       0.75      0.50      0.43       306
```

## Transfer from sink to edge sensortag

```
             precision    recall  f1-score   support

        0.0       1.00      0.15      0.27       111
        1.0       0.17      1.00      0.30        37
        2.0       0.67      0.02      0.04       110
        3.0       0.64      0.98      0.77        48

avg / total       0.72      0.34      0.27       306
```

## Transfer from iphone to microwave sensortag

Selected 0 features.
