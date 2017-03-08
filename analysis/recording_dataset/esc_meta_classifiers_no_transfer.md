Classification using the ESC dataset as a meta-classifier
=========================================================

1. train 5 classifiers based on the ESC dataset
2. split the targeted dataset into train/test 70/30
3. use the meta-classifiers to predict features for the training and testing
4. train and test classifier using the predicted meta-features

## Train and test on iPhone at home

```
             precision    recall  f1-score   support

          0       0.71      0.95      0.82        21
          1       0.62      0.83      0.71         6
          2       1.00      1.00      1.00        17
          3       1.00      0.73      0.85        15
          4       0.82      0.56      0.67        16

avg / total       0.85      0.83      0.82        75
```

## Train and test on iPad at home

```
             precision    recall  f1-score   support

          0       1.00      0.76      0.87        17
          1       0.00      0.00      0.00        10
          2       0.83      1.00      0.91        15
          3       0.83      1.00      0.91        15
          4       0.64      0.94      0.76        17

avg / total       0.71      0.80      0.74        74
```

## Train and test on MacBook at home

```
             precision    recall  f1-score   support

          0       1.00      0.60      0.75        20
          1       0.82      0.90      0.86        10
          2       0.80      1.00      0.89        20
          3       0.86      1.00      0.92        12
          4       0.85      0.85      0.85        13

avg / total       0.87      0.85      0.85        75
```

## Train and test on iPhone in NSH 2nd floor

```
             precision    recall  f1-score   support

          0       0.94      0.88      0.91        17
          1       0.69      0.87      0.77        23
          3       1.00      0.38      0.56        13
          4       0.91      1.00      0.95        10
          5       0.85      0.94      0.89        18

avg / total       0.85      0.83      0.81        81
```
