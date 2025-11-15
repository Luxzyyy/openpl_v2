select distinct on (Name)
    Name,
    Sex,
    Age,
    AgeClass,
    BirthYearClass,
    Country,
    State
from {{ ref('stg__openpl_raw') }}

