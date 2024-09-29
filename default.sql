create table drug_type(
    id integer primary key autoincrement,
    name text not null
);
create table pharmacies(
    id integer primary key autoincrement,
    name text not null,
    address text not null
);
create table inventory(
    drug_id integer primary key autoincrement,
    drug_type_id integer,
    pharmacy_id integer,
    foreign key (drug_type_id) references drug_type(id),
    foreign key (pharmacy_id) references pharmacies(id)
);

insert into drug_type (name) values
    ('Oxycodone'),
    ('Fentanyl'),
    ('Cocaine'),
    ('Methamphetamine'),
    ('Benzodiazepines');

insert into pharmacies (name, address) values
    ('CVS', '12701 SW 42nd St, Miami, FL 33175'),
    ('CVS', '9031 SW 107th Ave, Miami, FL 33176'),
    ('CVS', '10660 SW 40th St, Miami, FL 33165');