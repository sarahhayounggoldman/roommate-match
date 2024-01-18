use je100_db; 

-- Cascade or set null
-- event time-date, start time and end time

CREATE TABLE roommate (
    pid int PRIMARY KEY AUTO_INCREMENT,
    username varchar(40) not null,
    descrip varchar(500),
    contact varchar(40), 
    classyear varchar(4),
    bedtime time,
    waketime time,
    cleanliness int,
    activity int,
    dorm enum('east', 'tower', 'quint', 'no pref')
)
