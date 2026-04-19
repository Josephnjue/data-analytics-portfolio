SELECT 
    worker_id,
    COUNT(task_id) AS tasks_completed,
    AVG(completion_time) AS avg_time,
    AVG(accuracy) AS avg_accuracy,
    SUM(CASE WHEN status='error' THEN 1 ELSE 0 END) AS errors
FROM dataset
GROUP BY worker_id;