use consulta_app_alpha

drop table if exists medicos

create table medicos (

	id int identity,
	status bit not null, -- verdadeiro sempre
	nome varchar(50) not null,
	dt_nasc date not null,
	email varchar(50) unique not null,
	celular varchar(50) not null,
	telefone varchar(50),
	sexo varchar(50) not null,
	cpf varchar(50) primary key not null,
    crm varchar(50) unique not null,
	senha varchar(50) not null,
	data_criacao date,

)