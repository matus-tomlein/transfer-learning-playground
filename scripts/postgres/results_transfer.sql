CREATE TABLE
results_transfer
(source_device integer, target_device integer,
source_dataset integer, target_dataset integer,
activities integer,
feature integer, clf integer,
feature_selection boolean,
scaled_independently boolean default FALSE,
source_training_data numeric default 0.6,
target_training_data numeric default 0.0,
easy_domain_adaptation boolean default FALSE,
accuracy numeric,
precision_recall_fscore_support text,
confusion_matrix text
)
