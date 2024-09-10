show databases;
use dbms;

show tables;
create table Hplaylist(link varchar(100), lang varchar(10));
create table Splaylist(link varchar(100), lang varchar(10));

drop table Hplaylist;

insert into Hplaylist values("https://youtube.com/playlist?list=PL9bw4S5ePsEF-J_tIORZ6xE_OXkGuKjjY","hindi");
insert into Hplaylist values("https://youtube.com/playlist?list=PLB00151086C9310A0","hindi");
insert into Hplaylist values("https://youtube.com/playlist?list=PLw8TejMbmHM6IegrJ4iECWNoFuG7RiCV_","english");
insert into Hplaylist values("https://youtube.com/playlist?list=PL64E6BD94546734D8","english");
select * from Hplaylist;

insert into Splaylist values("https://youtube.com/playlist?list=PL9khxBZiiQwoKEqdTrb4ip-S_Tov6FkBQ","hindi");
insert into Splaylist values("https://youtu.be/-F8spsC9eFw","hindi");
insert into Splaylist values("https://youtube.com/playlist?list=PL3-sRm8xAzY-w9GS19pLXMyFRTuJcuUjy","english");
insert into Splaylist values("https://youtube.com/playlist?list=PLbgl9Fi469m1GwI2YGtVPc9wSYtDSB9ao","english");

select * from Splaylist;