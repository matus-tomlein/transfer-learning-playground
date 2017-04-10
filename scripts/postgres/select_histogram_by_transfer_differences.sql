SELECT
accuracy,
MAX("Same sensor type in same place") AS "Same sensor type in same place",
MAX("Same sensor in different place in same room") AS "Same sensor in different place in same room",
MAX("Same sensor type in different place in same room") AS "Same sensor type in different place in same room",
MAX("Different sensor type in same place") AS "Different sensor type in same place",
MAX("Different sensor type in same room") AS "Different sensor type in same room",
MAX("Same sensor in different room") AS "Same sensor in different room",
MAX("Different sensor type in different room") AS "Different sensor type in different room"

FROM
(
  SELECT
  accuracy,
  CASE WHEN type_of_transfer = 'Same sensor type in same place' THEN count ELSE 0 END AS "Same sensor type in same place",
  CASE WHEN type_of_transfer = 'Same sensor in different place in same room' THEN count ELSE 0 END AS "Same sensor in different place in same room",
  CASE WHEN type_of_transfer = 'Same sensor type in different place in same room' THEN count ELSE 0 END AS "Same sensor type in different place in same room",
  CASE WHEN type_of_transfer = 'Different sensor type in same place' THEN count ELSE 0 END AS "Different sensor type in same place",
  CASE WHEN type_of_transfer = 'Different sensor type in same room' THEN count ELSE 0 END AS "Different sensor type in same room",
  CASE WHEN type_of_transfer = 'Same sensor in different room' THEN count ELSE 0 END AS "Same sensor in different room",
  CASE WHEN type_of_transfer = 'Different sensor type in different room' THEN count ELSE 0 END AS "Different sensor type in different room"

  FROM
  (
    SELECT
    type_of_transfer, accuracy, COUNT(*) as count

    FROM (
      SELECT

      CASE
      WHEN source_room = target_room AND source_device_type = target_device_type AND source_location = target_location
      THEN 'Same sensor type in same place'
      WHEN source_room = target_room AND source_device = target_device AND source_location <> target_location
      THEN 'Same sensor in different place in same room'
      WHEN source_room = target_room AND source_device_type = target_device_type AND source_location <> target_location
      THEN 'Same sensor type in different place in same room'
      WHEN source_room = target_room AND source_device_type <> target_device_type AND source_location = target_location
      THEN 'Different sensor type in same place'
      WHEN source_room = target_room AND source_device_type <> target_device_type AND source_location <> target_location
      THEN 'Different sensor type in same room'
      WHEN source_room <> target_room AND source_device = target_device
      THEN 'Same sensor in different room'
      WHEN source_room <> target_room AND source_device_type = target_device_type
      THEN 'Same sensor type in different room'
      WHEN source_room <> target_room AND source_device_type <> target_device_type
      THEN 'Different sensor type in different room'
      ELSE 'Other' END AS type_of_transfer,

      ROUND(accuracy_with_fs, 1) as accuracy

      FROM v_results_transfer_aggr_fs

      WHERE
      activities = '11 activities' AND
      source_device_type = 'SensorTag' AND
      features = 'Accel & magnet'

      ORDER BY type_of_transfer
    ) t

    GROUP BY type_of_transfer, accuracy
  ) tt

) ttt

GROUP BY accuracy
