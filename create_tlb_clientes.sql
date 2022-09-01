create table clientes (

	id int primary key identity,
	status bit not null, -- verdadeiro sempre
	nome varchar(50) not null,
	dt_nasc datetime not null,
	email varchar(50) not null,
	celular varchar(50) not null,
	telefone varchar(50),
	sexo varchar(50) not null,
	cpf varchar(50) not null,
	data_criacao timestamp,

)