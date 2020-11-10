CREATE USER postgres WITH PASSWORD 'password';
CREATE SCHEMA IF NOT EXISTS together AUTHORIZATION postgres;
ALTER ROLE postgres SET search_path TO together;