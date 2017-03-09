Classification of recordings on a single domain
===============================================

1. split a single dataset to 70/30
2. train and test using random forest

## SS018 – placed on the other side, behind table

### Using accelerometer FFT + SST

```
             precision    recall  f1-score   support

        0.0       0.42      0.36      0.38        14
        1.0       0.36      0.50      0.42        10
        2.0       0.38      0.56      0.45        16
        3.0       0.38      0.18      0.24        17
        4.0       0.67      0.80      0.73         5
        5.0       0.94      0.83      0.88        18

avg / total       0.52      0.51      0.50        80
```

### Using accelerometer SST

```
             precision    recall  f1-score   support

        0.0       1.00      1.00      1.00        12
        1.0       0.94      0.85      0.89        20
        2.0       0.83      1.00      0.91        10
        3.0       0.80      0.89      0.84         9
        4.0       1.00      0.92      0.96        12
        5.0       0.94      0.94      0.94        17

avg / total       0.93      0.93      0.93        80
```

### Using microphone SST

```
             precision    recall  f1-score   support

        0.0       1.00      1.00      1.00        16
        1.0       0.88      0.94      0.91        16
        2.0       0.92      0.92      0.92        13
        3.0       1.00      1.00      1.00        16
        4.0       1.00      1.00      1.00         7
        5.0       0.91      0.83      0.87        12

avg / total       0.95      0.95      0.95        80
```

### Using magnetometer SST

```
             precision    recall  f1-score   support

        0.0       0.15      0.14      0.15        14
        1.0       0.00      0.00      0.00        11
        2.0       0.35      0.33      0.34        21
        3.0       0.25      0.18      0.21        11
        4.0       1.00      1.00      1.00         6
        5.0       0.53      0.59      0.56        17

avg / total       0.34      0.34      0.34        80
```

## SS049 – placed by sink

### Using accelerometer SST

```
             precision    recall  f1-score   support

        0.0       0.71      0.77      0.74        13
        1.0       0.67      0.53      0.59        15
        2.0       0.69      0.73      0.71        15
        3.0       0.75      0.67      0.71         9
        4.0       0.78      0.88      0.82         8
        5.0       0.71      0.75      0.73        20

avg / total       0.71      0.71      0.71        80
```

### Using microphone SST

```
             precision    recall  f1-score   support

        0.0       0.94      1.00      0.97        16
        1.0       0.91      0.91      0.91        11
        2.0       0.58      0.73      0.65        15
        3.0       0.64      0.47      0.54        15
        4.0       1.00      0.78      0.88         9
        5.0       0.87      0.93      0.90        14

avg / total       0.81      0.80      0.80        80
```

### Using magnetometer SST

```
             precision    recall  f1-score   support

        0.0       0.86      0.80      0.83        15
        1.0       0.77      0.91      0.83        11
        2.0       1.00      0.76      0.87        17
        3.0       0.71      0.86      0.77        14
        4.0       1.00      0.89      0.94         9
        5.0       0.87      0.93      0.90        14

avg / total       0.87      0.85      0.85        80
```

## SS076 – placed in the elbow of the kitchen desk

### Using magnetometer SST

```
             precision    recall  f1-score   support

        0.0       0.93      0.72      0.81        18
        1.0       0.53      0.89      0.67         9
        2.0       0.41      0.50      0.45        14
        3.0       0.43      0.25      0.32        12
        4.0       1.00      1.00      1.00        11
        5.0       1.00      1.00      1.00        16

avg / total       0.74      0.72      0.72        80
```

### Using accelerometer SST

```
             precision    recall  f1-score   support

        0.0       1.00      1.00      1.00        13
        1.0       1.00      0.76      0.86        21
        2.0       0.82      1.00      0.90         9
        3.0       0.69      0.90      0.78        10
        4.0       1.00      1.00      1.00         7
        5.0       1.00      1.00      1.00        20

avg / total       0.94      0.93      0.93        80
```

### Using microphone SST

```
             precision    recall  f1-score   support

        0.0       0.71      0.77      0.74        13
        1.0       0.55      0.67      0.60         9
        2.0       0.94      0.83      0.88        18
        3.0       0.75      0.90      0.82        10
        4.0       0.50      0.50      0.50         6
        5.0       0.76      0.67      0.71        24

avg / total       0.75      0.74      0.74        80
```

## SS008 – placed between coffee machines

### Using microphone SST

```
             precision    recall  f1-score   support

        0.0       0.79      1.00      0.88        11
        1.0       0.86      0.92      0.89        13
        2.0       0.85      0.85      0.85        13
        3.0       0.85      0.85      0.85        13
        4.0       0.89      0.80      0.84        10
        5.0       0.82      0.70      0.76        20

avg / total       0.84      0.84      0.83        80
```

### Using accelerometer SST

```
             precision    recall  f1-score   support

        0.0       0.73      0.92      0.81        12
        1.0       1.00      0.65      0.79        17
        2.0       0.94      0.94      0.94        16
        3.0       0.75      0.82      0.78        11
        4.0       0.89      1.00      0.94         8
        5.0       0.94      1.00      0.97        16

avg / total       0.89      0.88      0.87        80
```

### Using magnetometer SST

```
             precision    recall  f1-score   support

        0.0       0.53      0.50      0.51        18
        1.0       0.29      0.13      0.18        15
        2.0       0.73      0.92      0.81        12
        3.0       0.29      0.42      0.34        12
        4.0       0.62      0.83      0.71         6
        5.0       0.62      0.59      0.61        17

avg / total       0.51      0.53      0.51        80
```
