use consulta_app_alpha

drop table if exists agendamentos

create table agendamentos (

	id int identity,
	status bit not null, -- verdadeiro sempre
    cpf_paciente varchar(50) not null,
	paciente varchar(50) not null,
	data_consulta date not null,
    hora_consulta time not null,
    consultorio varchar(50) not null,
    medico varchar(50) not null,
    --cpf_medico varchar(50)
    especialidade varchar(50) not null,
    confirma bit null, 
    chave varchar(50) 
	
        )
