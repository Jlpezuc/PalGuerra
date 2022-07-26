drop database if exists correo_yury;
create database correo_yury;
use correo_yury;

create table employee (
	id int primary key,
    rut char(8),
    pass varchar(255),
    first_name varchar(255),
    second_name varchar(255),
    last_name varchar(255),
    second_last_name varchar(255),
    address varchar(255),
    phone char(9),
    email varchar(255),
    rh bool
);

create table person_employee (
	id int primary key,
    id_employee int,
    first_name varchar(255),
    last_name varchar(255),
    relationship varchar(255),
    carga bool,
    rut char(8),
    male bool,
    phone char(9),
    emergency bool,
    foreign key(id_employee) references employee(id) on delete cascade
);

create table log_action(
	id integer primary key,
	str varchar(255)
);

create table log (
	id int primary key,
    fecha date,
    id_action int,
    foreign key(id_action) references log_action(id) on delete cascade
);

insert into log_action values (1, 'Create');
insert into log_action values (2, 'Delete');
insert into log_action values (3, 'Update');