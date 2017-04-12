CREATE TABLE
results_transfer
(source_device integer, target_device integer,
source_dataset integer, target_dataset integer,
activities integer,
feature integer, clf integer,
feature_selection boolean,
accuracy numeric,
precision_recall_f_score_support text,
confusion_matrix text
)