CREATE OR REPLACE VIEW v_results_transfer_aggr_fs AS

SELECT
source_dataset, target_dataset,
source_device, target_device,
source_device_type, target_device_type,
source_location, target_location,
source_room, target_room,
features, activities,
target_training_data,
easy_domain_adaptation,
MAX(accuracy_with_fs_with_is) AS accuracy_with_fs_with_is,
MAX(accuracy_with_fs_without_is) AS accuracy_with_fs_without_is,
MAX(accuracy_without_fs_with_is) AS accuracy_without_fs_with_is,
MAX(accuracy_without_fs_without_is) AS accuracy_without_fs_without_is

FROM

(
  SELECT
  source_dataset, target_dataset,
  source_device, target_device,
  source_device_type, target_device_type,
  source_location, target_location,
  source_room, target_room,
  features, feature_selection,
  activities, scaled_independently,
  target_training_data,
  easy_domain_adaptation,
  avg_accuracy AS accuracy_with_fs_with_is,
  -1 AS accuracy_with_fs_without_is,
  -1 AS accuracy_without_fs_with_is,
  -1 AS accuracy_without_fs_without_is
  FROM v_results_transfer_aggr
  WHERE feature_selection AND scaled_independently

  UNION

  SELECT
  source_dataset, target_dataset,
  source_device, target_device,
  source_device_type, target_device_type,
  source_location, target_location,
  source_room, target_room,
  features, feature_selection,
  activities, scaled_independently,
  target_training_data,
  easy_domain_adaptation,
  -1 AS accuracy_with_fs_with_is,
  avg_accuracy AS accuracy_with_fs_without_is,
  -1 AS accuracy_without_fs_with_is,
  -1 AS accuracy_without_fs_without_is
  FROM v_results_transfer_aggr
  WHERE feature_selection AND NOT scaled_independently

  UNION

  SELECT
  source_dataset, target_dataset,
  source_device, target_device,
  source_device_type, target_device_type,
  source_location, target_location,
  source_room, target_room,
  features, feature_selection,
  activities, scaled_independently,
  target_training_data,
  easy_domain_adaptation,
  -1 AS accuracy_with_fs_with_is,
  -1 AS accuracy_with_fs_without_is,
  avg_accuracy AS accuracy_without_fs_with_is,
  -1 AS accuracy_without_fs_without_is
  FROM v_results_transfer_aggr
  WHERE NOT feature_selection AND scaled_independently

  UNION

  SELECT
  source_dataset, target_dataset,
  source_device, target_device,
  source_device_type, target_device_type,
  source_location, target_location,
  source_room, target_room,
  features, feature_selection,
  activities, scaled_independently,
  target_training_data,
  easy_domain_adaptation,
  -1 AS accuracy_with_fs_with_is,
  -1 AS accuracy_with_fs_without_is,
  -1 AS accuracy_without_fs_with_is,
  avg_accuracy AS accuracy_without_fs_without_is
  FROM v_results_transfer_aggr
  WHERE NOT feature_selection AND NOT scaled_independently

) t

GROUP BY

source_dataset, target_dataset,
source_device, target_device,
source_device_type, target_device_type,
source_location, target_location,
source_room, target_room,
features, activities,
target_training_data,
easy_domain_adaptation
