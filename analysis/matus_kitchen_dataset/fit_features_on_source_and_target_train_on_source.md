Fit features on both source and target domain, train on source
==============================================================

1. fit features on both source and target domains
2. train on source domain
3. test on target domain

## Transfer from edge to microwave sensortag

```
             precision    recall  f1-score   support

        0.0       0.96      0.98      0.97       111
        1.0       0.34      0.89      0.49        37
        2.0       1.00      0.42      0.59       110
        3.0       0.98      1.00      0.99        48

avg / total       0.90      0.77      0.78       306
```

## Transfer from sink to edge sensortag

```
             precision    recall  f1-score   support

        0.0       1.00      0.21      0.34       111
        1.0       0.23      1.00      0.37        37
        2.0       0.99      0.65      0.79       110
        3.0       1.00      1.00      1.00        48

avg / total       0.90      0.59      0.61       306
```

## Transfer from iphone to microwave sensortag

```
             precision    recall  f1-score   support

        0.0       0.52      1.00      0.68       111
        1.0       0.44      0.30      0.35        37
        2.0       0.94      0.14      0.24       110
        3.0       0.96      1.00      0.98        48

avg / total       0.73      0.60      0.53       306
```
