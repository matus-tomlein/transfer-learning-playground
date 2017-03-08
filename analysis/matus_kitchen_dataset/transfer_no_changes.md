Transfer without any changes
============================

1. train on source domain
2. test on target domain

## Transfer from microwave to edge sensortag

```
             precision    recall  f1-score   support

        0.0       1.00      0.20      0.33       111
        1.0       0.16      1.00      0.27        37
        2.0       0.05      0.02      0.03       110
        3.0       1.00      0.21      0.34        48

avg / total       0.56      0.23      0.22       306
```

## Transfer from edge to microwave sensortag

```
             precision    recall  f1-score   support

        0.0       0.71      0.99      0.82       111
        1.0       0.22      0.49      0.30        37
        2.0       0.29      0.18      0.22       110
        3.0       0.00      0.00      0.00        48

avg / total       0.39      0.48      0.42       306
```

## Transfer from sink to edge sensortag

```
             precision    recall  f1-score   support

        0.0       0.79      0.14      0.23       111
        1.0       0.18      0.84      0.30        37
        2.0       0.90      0.56      0.69       110
        3.0       1.00      0.98      0.99        48

avg / total       0.79      0.51      0.52       306
```

## Transfer from iphone to microwave sensortag

```
             precision    recall  f1-score   support

        0.0       0.58      1.00      0.74       111
        1.0       0.83      0.95      0.89        37
        2.0       0.96      0.22      0.36       110
        3.0       0.96      0.98      0.97        48

avg / total       0.81      0.71      0.65       306
```
