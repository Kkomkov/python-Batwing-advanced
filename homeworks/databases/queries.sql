
CREATE TABLE `level` (
	id SMALLINT UNSIGNED NOT NULL,
	student_id INT NOT NULL,
	CONSTRAINT level_student_id_FK FOREIGN KEY (student_id) REFERENCES students(id)
);

insert into level(id,student_id)
values( 10,1),
	  (10,2),
	  (11,3),
	  (11,4);
      
select s.first_name ,s.last_name ,level.id "level" ,l.name "lesson", t.name "teacher"
from  students s 
left join level on (level.student_id=s.id)
left join students_lessons sl  on (sl.student_id=s.id)
left join lessons l on (sl.lesson_id =l.id )
left join teachers t on (l.id=t.lesson_id);