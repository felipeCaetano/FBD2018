
create schema FJMCosturaFeliz;
use FJMCosturaFeliz;

-- Criando as tabelas 

create table funcionario(
matricula integer,
nome varchar (100)
);

create table costureira(

valor_minimo double,
matricula_func integer
);

create table supervisora(
matricula_func integer
);

create table peca(
modelo varchar(20),
descricao varchar (100),
matricula_costureira integer
);

create table tipo_costura (
descricao varchar(100)
);

create table habilitacao(

matricula_costureira integer,
descricao varchar(100)
);


create table maquina(

codigo integer,
localizacao varchar(40),
fabricante varchar (40)
);

create table capacitacao(

codigo_maquina integer,
descricao varchar (100)
);

create table manutencao(

data_inicio date,
data_termino date,
codigo_maquina integer,
matricula_func integer
);

-- Povoando as tabelas

insert into funcionario(matricula,nome) values
(111, 'cleta da abaporojucaiba'),
(222, 'felipa da silva'),
(333, 'marcona da silva'),
(444,'josefa da silva'),
(555,'rodriga de abaporojucaiba');

insert into costureira(valor_minimo,matricula_func) values
(1000.00,222),
(2000.00,333),
(3000.00,444);

insert into supervisora (matricula_func) values
(111),
(555);

insert into peca (modelo,descricao,matricula_costureira) values
('calca','calca saruel muito bonita e legal', 222),
('camisa','camisa da caveira da cobra da lagoa azul', 222),
('sapato','sapato invisivel cor de rosa', 333),
('oculos','oculos de pano em algodao de primeira qualidade tirado de cangurus', 444);

insert into tipo_costura(descricao) values
('costura 1'),
('costura 2'),
('costura 3'),
('costura 4'),
('costura 5'),
('costura 6'),
('costura 7'),
('costura 8');


insert into habilitacao(matricula_costureira,descricao) values
(222,'costura 2'),
(333,'costura 2'),
(444,'costura 1'),
(444,'costura 8');


insert into maquina(codigo


-- Chaves primárias

alter table funcionario add constraint pk_funcionario primary key (matricula);
alter table costureira add constraint pk_costureira primary key (matricula_func);
alter table supervisora add constraint pk_supervisora primary key (matricula_func);
alter table peca add constraint pk_peca primary key (modelo);
alter table tipo_costura add constraint pk_tipo_costura primary key (descricao);
alter table habilitacao add constraint pk_habilitacao primary key (matricula_func,descricao);
alter table maquina add constraint pk_maquiha primary key (codigo);
alter table capacitacao add constraint pk_capacitacao primary key (codigo_maquina,descricao);
alter table manutencao add constraint pk_manutencao primary key (data_inicio,data_termino,codigo_maquina,matricula_func );

-- Chaves estrangeiras

alter table costureira add constraint fk_funcionario_costureira foreign key (matricula_func) references funcionario(matricula);
alter table supervisora add constraint fk_funcionario_supervisora foreign key (matricula_func) references funcionario(matricula);
alter table peca add constraint fk_costureira_peca foreign key (matricula_func) references costureira(matricula_func);
alter table habilitacao add constraint fk_costureira_habilitacao foreign key (matricula_func) references costureira(matricula_func);
alter table habilitacao add constraint fk_costureira_habilitacao foreign key (matricula_func) references costureira(matricula_func);
alter table capacitacao add constraint fk_codigomaquina_capacitacao foreign key (codigo_maquina) references maquina(codigo);
alter table capacitacao add constraint fk_tipocostura_capacitacao foreign key (descricao) references tipo_costura(descricao);
alter table manutencao add constraint fk_matricula_func_manutencao foreign key (matricula_func) references supervisora(matricula_func);
alter table manutencao add constraint fk_codigomaquina_manutencao foreign key (codigo_maquina) references maquina(codigo);









