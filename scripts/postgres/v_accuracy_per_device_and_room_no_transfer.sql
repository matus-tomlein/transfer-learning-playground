CREATE OR REPLACE VIEW v_accuracy_per_device_and_room_no_transfer AS

SELECT AVG(avg_accuracy) as avg_accuracy, room, device_type, features FROM v_results_no_transfer_aggr
WHERE NOT feature_selection
GROUP BY room, device_type, features
ORDER BY avg_accuracy DESC
