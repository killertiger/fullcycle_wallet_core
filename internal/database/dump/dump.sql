USE wallet;

CREATE TABLE clients (id varchar(255), name varchar(255), email varchar(255), created_at date);
CREATE TABLE accounts (id varchar(255), client_id varchar(255), balance int, created_at date);
CREATE TABLE transactions (id varchar(255), account_id_from varchar(255), account_id_to varchar(255), amount int, created_at date);

INSERT INTO clients VALUES('ee21871d-e49c-442b-90f5-0d4b0599c5c1', 'John Doe', 'john@doe.com', '2021-01-01');
INSERT INTO clients VALUES('e9ce715a-49f1-499d-a44c-c17e3bee8d1a', 'Jane Doe', 'jane@doe.com', '2021-01-05');

INSERT INTO accounts VALUES('31168c15-b24c-409b-b9fa-693db404a9db', 'ee21871d-e49c-442b-90f5-0d4b0599c5c1', 1000, '2021-01-01');
INSERT INTO accounts VALUES('24b1b373-c52a-4687-9a71-10f60b61b4a4', 'e9ce715a-49f1-499d-a44c-c17e3bee8d1a', 1000, '2021-01-05');

CREATE DATABASE wallet_consumer;