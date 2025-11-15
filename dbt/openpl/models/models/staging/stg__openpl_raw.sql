{% set text_columns = ["Name", "Sex", "Event", "Equipment", "AgeClass", "BirthYearClass", "Division", "WeightClassKg", "Place", "Tested", "Country", "State", "Federation", "ParentFederation", "MeetCountry", "MeetState", "MeetName", "Sanctioned"] %}
{% set int_columns = ["Age", "BodyweightKg", "Squat1Kg", "Bench1Kg", "Deadlift1Kg", "Squat2Kg", "Bench2Kg", "Deadlift2Kg", "Squat3Kg", "Bench3Kg", "Deadlift3Kg", "Squat4Kg", "Bench4Kg", "Deadlift4Kg", "Best3SquatKg", "Best3BenchKg", "Best3DeadliftKg", "TotalKg", "Dots", "Wilks", "Glossbrenner", "Goodlift"] %}

select
    {% for text_column in text_columns %}
    cast("{{ text_column }}" as text) as {{ text_column }},
    {% endfor %}
    {% for int_column in int_columns %}
    cast("{{ int_column }}" as double precision) as {{ int_column }},
    {% endfor %}
    cast("Date" as date) as Date
from {{ source('openpl_raw', 'openpl_raw') }}