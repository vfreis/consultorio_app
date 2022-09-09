use consulta_app_alpha

create table agendamentos (

	id int primary key identity,
	status bit not null, -- verdadeiro sempre
    cpf_pacientes varchar(50) not null,
	paciente varchar(50) not null,
	data_consulta date not null,
    hora_consulta time not null,
    consultorio varchar(50) not null,
    medico varchar(50) not null,
    --cpf_medico varchar(50)
    especilidade varchar(50) not null,
    confirma bit null
	
        )
