

with source_data as (
    select
        u.user_name,
        u.country,
        l.lang_name as language,
        l.level as language_level,
        les.lesson_title,
        p.score,
        d.words_learned,
        ex.ex_type
    from "language_db"."main"."progress" p
    join "language_db"."main"."users" u on p.user_id = u.user_id
    join "language_db"."main"."lessons" les on p.lesson_id = les.lesson_id
    join "language_db"."main"."languages" l on les.lang_id = l.lang_id
    left join "language_db"."main"."dictionaries" d on u.user_id = d.user_id and l.lang_id = d.lang_id
    left join "language_db"."main"."exercises" ex on les.lesson_id = ex.lesson_id
)

select 
    user_name,
    country,
    language,
    language_level,
    count(distinct lesson_title) as total_lessons,
    round(avg(score), 1) as avg_score,
    sum(distinct words_learned) as total_words,
    -- Собираем типы упражнений в одну строку для наглядности
    group_concat(distinct ex_type, ', ') as exercise_types
from source_data
group by 1, 2, 3, 4