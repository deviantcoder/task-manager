Given tables:
- tasks (id, name, status, project_id) 
- projects (id, name)

Write the queries for:
1. get all statuses, not repeating, alphabetically ordered
```
SELECT DISTINCT status FROM tasks ORDER BY status ASC;
```

2. get the count of all tasks in each project, order by tasks count descending
```
SELECT p.name AS project_name, COUNT(t.id) AS task_count FROM projects p
LEFT JOIN tasks t ON t.project_id = p.id
GROUP BY p.id, p.name
ORDER BY task_count DESC;
```

3. get the count of all tasks in each project, order by projects names
```
SELECT p.name AS project_name, COUNT(t.id) AS task_count FROM projects p
LEFT JOIN tasks t ON t.project_id = p.id
GROUP BY p.id, p.name
ORDER BY p.name ASC;
```

4. get the tasks for all projects having the name beginning with "N" letter
```
SELECT t.*, p.name as project_name FROM tasks t
JOIN projects p ON t.project_id = p.id WHERE p.name LIKE 'N%';
```

5. get the list of al projects containing the 'a' letter in the middle of the name, and show the tasks count near each project. Mention that there can exist projects without tasks and tasks with project_id= NULL

```
SELECT p.name AS project_name, COUNT(t.id) AS task_count FROM projects p
LEFT JOIN tasks t ON t.project_id = p.id
WHERE p.name LIKE '%a%'
AND p.name NOT LIKE 'a%'
AND p.name NOT LIKE '%a'
GROUP BY p.id, p.name;
```

6. get the list of tasks with duplicate names. Order alphabetically

```1
SELECT name, COUNT(*) AS cnt FROM tasks
GROUP BY name HAVING COUNT(*) > 1
ORDER BY name ASC;
```

7. get the list of tasks having several exact matches of both name and status, from the project 'Delivery’. Order by matches count
```
SELECT t.name, t.status, COUNT(*) AS matches_count FROM tasks t
JOIN projects p ON t.project_id = p.id WHERE p.name = 'Delivery'
GROUP BY t.name, t.status HAVING COUNT(*) > 1
ORDER BY matches_count DESC;
```


8. get the list of project names having more than 10 tasks in status 'completed'. Order by project_id
```
SELECT p.name AS project_name FROM projects p
JOIN tasks t ON t.project_id = p.id WHERE t.status = 'completed'
GROUP BY p.id, p.name HAVING COUNT(t.id) > 10
ORDER BY p.id ASC;
```