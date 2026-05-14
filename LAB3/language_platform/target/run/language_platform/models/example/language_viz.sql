
  
    
    

    create  table
      "language_db"."main"."language_viz__dbt_tmp"
  
    as (
      

select 
    language,
    count(user_id) as total_students,
    avg(score) as average_score
from "language_db"."main"."progress"
where status = 'completed'
group by 1
    );
  
  