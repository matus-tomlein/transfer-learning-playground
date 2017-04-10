CREATE MATERIALIZED VIEW v_results_transfer_aggr AS

SELECT
source_dataset, target_dataset,
source_device, target_device,
source_device_type, target_device_type,
source_location, target_location,
source_room, target_room,
features, feature_selection,
activities,
AVG(accuracy) as avg_accuracy
FROM v_results_transfer
GROUP BY source_dataset, target_dataset,
source_device, target_device,
source_device_type, target_device_type,
source_location, target_location,
source_room, target_room,
features, feature_selection,
activities
ORDER BY avg_accuracy DESC
