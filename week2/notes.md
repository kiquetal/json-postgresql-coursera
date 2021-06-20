#### Inverted index on Postgres


    Generalized INverse Index

    Efficient: lookup/search. Disadvantages: can be costly when inserting or update data.
    


    Generalized Search Tree

    Hashing is used to reduce the size of and cost to update Gist

    select id, doc FROM docs where '{where}' <@ string_to_array(doc,' ');


    CREATE TABLE docs(id SERIAL, doc TEXT, primary key(id));
    CREATE INDEX gin1 ON docs USING gin(string_to_array(doc,' ') _ext_ops);
    
    ON PG9
    CREATE INDEX gin1 ON docs USING gin(string_to_array(doc,' ') _text_ops);
    ON PG11
    CREATE INDEX gin1 ON docs USING gin(string_to_array(doc,' ') array_ops);


    music=# CREATE TABLE docs(id SERIAL, doc TEXT, primary key(id));
    CREATE TABLE
    music=# CREATE INDEX gin1 ON docs USING gin(to_tsvector('english',doc));
    CREATE INDEX
    music=# INSERT INTO docs (doc) VALUES ('This is SQL and PYTHON and other fun teaching stuff'), ('More people should learn SQL from USMI'),('UMSI also teach python and sql');
    INSERT 0 3
    music=# select id, doc from docs WHERE to_tsquery('english','learn') @@ to_tsvector('english',doc);


    Exercises

    CREATE INDEX array03 ON docs03 USING gin(string_to_array(lower(doc),' ') array_ops);

    Goal

    SELECT id, doc FROM docs03 WHERE '{understanding}' <@ string_to_array(lower(doc), ' ');
    EXPLAIN SELECT id, doc FROM docs03 WHERE '{understanding}' <@ string_to_array(lower(doc), ' ');

    SHOULD NOT REUTN seq scan
    EXPLAIN SELECT id, doc FROM docs03 WHERE '{understanding}' <@ string_to_array(lower(doc), ' ');
    

    Exercises 2
    
    GOAL
    SELECT id, doc FROM docs03 WHERE to_tsquery('english', 'understanding') @@ to_tsvector('english', doc);
    EXPLAIN SELECT id, doc FROM docs03 WHERE to_tsquery('english', 'understanding') @@ to_tsvector('english', doc);
    
    Solution

    CREATE INDEX fulltext03 on docs03 USING gin(to_tsvector('english',doc));
