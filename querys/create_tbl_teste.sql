create table teste (

	id int primary key identity,
	status bit not null, -- verdadeiro sempre
	nome varchar(50) not null,
	data_criacao timestamp,

)