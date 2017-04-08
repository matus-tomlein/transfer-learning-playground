CREATE MATERIALIZED VIEW v_results_transfer_aggr AS

SELECT
source_dataset, target_dataset,
source_device, target_device,
source_location, target_location,
features, feature_selection,
AVG(accuracy) as avg_accuracy
FROM v_results_transfer
GROUP BY source_dataset, target_dataset,
source_device, target_device,
source_location, target_location,
features, feature_selection
ORDER BY avg_accuracy DESC
