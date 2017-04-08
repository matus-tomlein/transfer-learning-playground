CREATE OR REPLACE VIEW v_results_transfer AS

SELECT source_devices.name AS source_device,
target_devices.name AS target_device,
features.name AS features,
source_datasets.name AS source_dataset,
target_datasets.name AS target_dataset,
source_locations.name AS source_location,
target_locations.name AS target_location,
accuracy,
feature_selection

FROM results_transfer
JOIN devices AS source_devices ON source_devices.id = results_transfer.source_device
JOIN devices AS target_devices ON target_devices.id = results_transfer.target_device
JOIN features ON features.id = results_transfer.feature
JOIN datasets AS source_datasets ON source_datasets.id = results_transfer.source_dataset
JOIN datasets AS target_datasets ON target_datasets.id = results_transfer.target_dataset
JOIN device_locations AS source_locations ON source_locations.device_id = results_transfer.source_device AND source_locations.dataset_id = results_transfer.source_dataset
JOIN device_locations AS target_locations ON target_locations.device_id = results_transfer.target_device AND target_locations.dataset_id = results_transfer.target_dataset