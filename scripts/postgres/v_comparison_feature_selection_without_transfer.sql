CREATE OR REPLACE VIEW v_comparison_feature_selection_without_transfer

SELECT
name,
MAX(accuracy_with_feature_selection) AS accuracy_with_feature_selection,
MAX(accuracy_without_feature_selection) AS accuracy_without_feature_selection
FROM (
SELECT
(device_type || ' in ' || dataset) AS name,
CASE WHEN feature_selection THEN AVG(avg_accuracy) ELSE 0 END as accuracy_with_feature_selection,
CASE WHEN NOT feature_selection THEN AVG(avg_accuracy) ELSE 0 END as accuracy_without_feature_selection
FROM v_results_no_transfer_aggr
WHERE features = 'Accel & mic'
GROUP BY dataset, device_type, feature_selection
) t
GROUP BY name
ORDER BY name
