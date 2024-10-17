-- Set user permissions and configurations

ALTER ROLE gutenberg_user SET client_encoding TO 'utf8';
ALTER ROLE gutenberg_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE gutenberg_user SET timezone TO 'UTC';