Transfer without modifications
==============================

- activity Kettle is not trained in my home
- activity coffee is not trained at NSH 2

## Within my home

### From iPad to iPhone

```
             precision    recall  f1-score   support

          0       0.42      1.00      0.59        60
          1       0.53      0.23      0.32        35
          2       0.03      0.03      0.03        64
          3       0.00      0.00      0.00        46
          4       1.00      0.41      0.58        46

avg / total       0.37      0.35      0.30       251
```

### From iPhone to MacBook

```
             precision    recall  f1-score   support

          0       0.00      0.00      0.00        61
          1       0.00      0.00      0.00        35
          2       0.26      1.00      0.41        63
          3       1.00      0.02      0.04        46
          4       0.00      0.00      0.00        45

avg / total       0.25      0.26      0.11       250
```

### From MacBook to iPad

```
             precision    recall  f1-score   support

          0       0.46      0.33      0.39        57
          1       0.64      0.39      0.48        36
          2       0.00      0.00      0.00        64
          3       0.43      1.00      0.61        46
          4       0.52      0.91      0.66        45

avg / total       0.37      0.48      0.39       248
```

### From iPhone and iPad to MacBook

```
             precision    recall  f1-score   support

          0       0.69      1.00      0.81        61
          1       1.00      0.06      0.11        35
          2       0.97      1.00      0.98        63
          3       0.58      0.98      0.73        46
          4       1.00      0.38      0.55        45

avg / total       0.84      0.75      0.69       250
```

### From MacBook and iPad to iPhone

```
             precision    recall  f1-score   support

          0       1.00      1.00      1.00        60
          1       0.69      1.00      0.81        35
          2       0.98      1.00      0.99        64
          3       1.00      0.63      0.77        46
          4       1.00      1.00      1.00        46

avg / total       0.95      0.93      0.93       251
```

## From NSH 2nd floor to my home

### From iPhone to iPhone

             precision    recall  f1-score   support

          0       0.27      0.98      0.43        60
          1       0.89      0.49      0.63        35
          2       0.00      0.00      0.00        64
          3       0.67      0.04      0.08        46
          4       0.50      0.02      0.04        46
          5       0.00      0.00      0.00         0

avg / total       0.40      0.31      0.21       251

## From my home to NSH 2nd floor

### From MacBook and iPhone to iPhone

             precision    recall  f1-score   support

          0       0.81      0.91      0.86        56
          1       0.53      0.91      0.67        74
          2       0.00      0.00      0.00         0
          3       0.73      0.92      0.81        38
          4       0.87      0.73      0.79        37
          5       0.00      0.00      0.00        66

avg / total       0.53      0.66      0.58       271

### From MacBook and iPad in my home to iPhone in NSH

             precision    recall  f1-score   support

          0       0.95      0.75      0.84        56
          1       0.66      0.99      0.79        74
          2       0.00      0.00      0.00         0
          3       1.00      0.87      0.93        38
          4       0.74      0.95      0.83        37
          5       0.00      0.00      0.00        66

avg / total       0.62      0.68      0.63       271
