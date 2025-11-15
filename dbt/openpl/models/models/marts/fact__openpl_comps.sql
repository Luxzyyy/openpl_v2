{% set columns = ["Name", "Event", "Equipment", "Division", "WeightClassKg", "Place", "Tested", "Federation", "ParentFederation", "MeetCountry", "MeetState", "MeetName", "Sanctioned", "Age", "BodyweightKg", "Squat1Kg", "Bench1Kg", "Deadlift1Kg", "Squat2Kg", "Bench2Kg", "Deadlift2Kg", "Squat3Kg", "Bench3Kg", "Deadlift3Kg", "Squat4Kg", "Bench4Kg", "Deadlift4Kg", "Best3SquatKg", "Best3BenchKg", "Best3DeadliftKg", "TotalKg", "Dots", "Wilks", "Glossbrenner", "Goodlift"] %}



select
    {% for column in columns %}
    {{ column }}{% if not loop.last %},{% endif %}
    {% endfor %}
from {{ ref('stg__openpl_raw') }}