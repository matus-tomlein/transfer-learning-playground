Fit features on target domain, but train on source domain
=========================================================

1. fit features on target domain
2. train on source domain
3. test on target domain

## Transfer from edge to microwave sensortag

```
             precision    recall  f1-score   support

        0.0       0.67      0.99      0.80       111
        1.0       0.55      0.49      0.51        37
        2.0       0.78      0.43      0.55       110
        3.0       1.00      1.00      1.00        48

avg / total       0.75      0.73      0.71       306
```

## Transfer from sink to edge sensortag

```
             precision    recall  f1-score   support

        0.0       1.00      0.86      0.92       111
        1.0       0.85      0.89      0.87        37
        2.0       0.64      0.99      0.78       110
        3.0       1.00      0.02      0.04        48

avg / total       0.85      0.78      0.72       306
```

## Transfer from iphone to microwave sensortag

```
             precision    recall  f1-score   support

        0.0       0.63      0.99      0.77       111
        1.0       0.93      0.35      0.51        37
        2.0       0.90      0.56      0.69       110
        3.0       0.96      0.98      0.97        48

avg / total       0.82      0.76      0.74       306
```
