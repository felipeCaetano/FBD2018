import pymysql

conexao =pymysql.connect(host='localhost',user='root',password='root')

c =conexao.cursor()
criarbanco = 'create schema mjcosturafeliz;'
c.execute(criarbanco)

conexao =pymysql.connect(host='localhost',user='root',password='root',db='mjcosturafeliz')
c =conexao.cursor()
c.execute('use mjcosturafeliz;')

c.execute(''' 
create table funcionario(
matricula integer,
nome varchar (100));''')

c.execute('''
create table costureira(
valor_minimo double,
matricula_func integer
);''')

c.execute('''create table supervisora(
matricula_func integer
);''')

c.execute('''create table peca(
modelo varchar(20),
descricao varchar (100),
matricula_costureira integer
);''')

c.execute('''create table tipo_costura (
descricao varchar(100)
);''')

c.execute('''create table habilitacao(

matricula_costureira integer,
descricao varchar(100)
);''')


c.execute('''create table maquina(

codigo integer,
localizacao varchar(40),
fabricante varchar (40)
);''')

c.execute('''create table capacitacao(

codigo_maquina integer,
descricao varchar (100)
);''')

c.execute('''create table manutencao(

data_inicio date,
data_termino date,
codigo_maquina integer,
matricula_func integer
);''')


#-- Povoando as tabelas


c.execute('''insert into funcionario(matricula,nome) values
(111, 'cleta da abaporojucaiba'),
(222, 'felipa da silva'),
(333, 'marcona da silva'),
(444,'josefa da silva'),
(555,'rodriga de abaporojucaiba');''')

c.execute('''insert into costureira(valor_minimo,matricula_func) values
(1000.00,222),
(2000.00,333),
(3000.00,444);''')

c.execute('''insert into supervisora (matricula_func) values
(111),
(555);
''')

c.execute('''insert into peca (modelo,descricao,matricula_costureira) values
('calca','calca saruel muito bonita e legal', 222),
('camisa','camisa da caveira da cobra da lagoa azul', 222),
('sapato','sapato invisivel cor de rosa', 333),
('oculos','oculos de pano em algodao de primeira qualidade tirado de cangurus', 444);''')

c.execute('''insert into tipo_costura(descricao) values
('costura 1'),
('costura 2'),
('costura 3'),
('costura 4'),
('costura 5'),
('costura 6'),
('costura 7'),
('costura 8');''')

c.execute('''insert into capacitacao (codigo_maquina,descricao) values
(1,'costura 2'),
(2,'costura 8');''')


c.execute('''insert into habilitacao(matricula_costureira,descricao) values
(222,'costura 2'),
(333,'costura 2'),
(444,'costura 1'),
(444,'costura 8');''')


c.execute(''' insert into maquina(codigo, localizacao, fabricante) values
(1,'cegoe','cletoltda'),
(2,'Producao','HP'),
(3,'Costura','Ferrari'),
(4,'Corte','EA costura'),
(5,'Acabamento','RockStar Costuras');''')

c.execute(''' insert into manutencao(data_inicio,data_termino,codigo_maquina,matricula_func) values
('2018-1-25','2018-9-12',1,555),
('2018-1-12','2018-6-12',2,555),
('2018-1-14','2018-2-12',3,555),
('2018-1-30','2018-8-12',4,111),
('2018-1-1','2018-8-12',6,555);''')


#-- Chaves primárias

c.execute('''alter table funcionario add constraint pk_funcionario primary key (matricula);''')
c.execute('''alter table costureira add constraint pk_costureira primary key (matricula_func);''')
c.execute('''alter table supervisora add constraint pk_supervisora primary key (matricula_func);''')
c.execute('''alter table peca add constraint pk_peca primary key (modelo);''')
c.execute('''alter table tipo_costura add constraint pk_tipo_costura primary key (descricao);''')
c.execute('''alter table habilitacao add constraint pk_habilitacao primary key (matricula_costureira,descricao);''')
c.execute('''alter table maquina add constraint pk_maquiha primary key (codigo);''')
c.execute('''alter table capacitacao add constraint pk_capacitacao primary key (codigo_maquina,descricao);''')
c.execute('''alter table manutencao add constraint pk_manutencao primary key (data_inicio,data_termino,codigo_maquina,matricula_func );''')

#-- Chaves estrangeiras

c.execute('''alter table costureira add constraint fk_funcionario_costureira foreign key (matricula_func) references funcionario(matricula)  on delete set null ;''')
c.execute('''alter table supervisora add constraint fk_funcionario_supervisora foreign key (matricula_func) references funcionario(matricula)  on delete set null ;''')
c.execute('''alter table peca add constraint fk_costureira_peca foreign key (matricula_costureira) references costureira(matricula_func);''')
c.execute('''alter table habilitacao add constraint fk_costureira_habilitacao foreign key (matricula_costureira) references costureira(matricula_func);''')
c.execute('''alter table capacitacao add constraint fk_codigomaquina_capacitacao foreign key (codigo_maquina) references maquina(codigo) on update cascade on delete cascade ;''')
c.execute('''alter table capacitacao add constraint fk_tipocostura_capacitacao foreign key (descricao) references tipo_costura(descricao);''')
c.execute('''alter table manutencao add constraint fk_matricula_func_manutencao foreign key (matricula_func) references supervisora(matricula_func);''')
c.execute('''alter table manutencao add constraint fk_codigomaquina_manutencao foreign key (codigo_maquina) references maquina(codigo) on delete cascade;''')