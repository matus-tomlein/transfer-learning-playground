Transfer using ESC-50 noise dataset as meta-classifiers
=======================================================

- ESC-50 provides samples for 50 classes of 5s sounds in 5 categories
  - https://github.com/karoldvl/ESC-50/blob/master/README.md
- idea: use the 5 categories as 5 meta-classifiers to train the virtual sensors on

1. for each category in ESC-50 build a classifier to recognize them
2. classify the recordings using each classifiers
3. train a classifier recognizing activities using the classifications from step 2 on
   source domain
4. test the classifier on the target domain

Results:

* [Classification without transfer](esc_meta_classifiers_no_transfer.md)
* [With transfer](esc_transfer.md)

Reasons for bad performance:

* the ESC-50 dataset wasn't a good fit for the problem
  * in some categories, the meta-classifier predicted the same label for all the
    recorded activities
* the same meta-classifiers were used for all inputs
  * the meta-classifiers should be adapted for each input to enable the
    end-classifiers to be the same
