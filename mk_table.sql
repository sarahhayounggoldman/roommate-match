use je100_db; 

-- Cascade or set null
-- event time-date, start time and end time
drop table if exists roommate;

CREATE TABLE roommate (
    pid int PRIMARY KEY AUTO_INCREMENT,
    username varchar(40) not null,
    descrip varchar(500),
    contact varchar(40), 
    classyear varchar(4),
    bedtime int,
    waketime int,
    cleanliness int,
    activity int,
    dorm enum('east', 'tower', 'quint', 'no pref')
)
