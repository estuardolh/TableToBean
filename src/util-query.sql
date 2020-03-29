-- Query on oracle for CSV file required
SELECT ''''||table_name||''','''||column_name||''','''||data_type||''','''||data_length||''','''||comments||''''
FROM all_tab_columns NATURAL JOIN all_col_comments
ORDER BY table_name, column_id;
