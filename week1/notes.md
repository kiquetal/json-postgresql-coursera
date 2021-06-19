#### Notes

 - https://www.pg4e.com/lectures/05-FullText
    
        We can go to block not row.
        8K block size by default postgres

#### Indexes

    Logical Keys: 

    B-Tree -- The default for many applications [constant depth for be efficient]

    BRIN -- Block Range Index-Smaller/ faster data is mostly sorted

    Hash -- Quick lookup of long key strings

    GIN --  Generalized Search Tree

    SP-GiST-- Space Partitioned Generalized Search Tree.

    Forward indexes -> logical key, primary keys
    
    Inverse Indexes(GIN,GIST) index a string

#### USING ONLY SQL

   string_to_array('Hello world',' ')
   
   SELECT string_to_array('Hello World','');
   SELECT unnest(string_to_array('Hello world',''));
   
   CREATE TABLE docs(id SERIAL, doc TEXT, primary key(id))
   INSERT INTO docs(doc) VALUES
   ('THis is sql and python and other fun teching suff'),
   ('More people should learn SQL from USMSI'),
   ('UMSI also teaches python and also sql')
   
   SELECT id, s.keyword as keyword FROM docs as D, unnest(string_to_array(D.doc,' ')) s(keyword)
   ORDER by id;
   
   SELECT DISTINCT id, s.keyword as keyword
   FROM docs AS D, unnest(string_to_array(D.doc,'')) s(keyword)
   ORDER BY ID;

   INSERT INTO docs_gin(doc_id,keyword)
   SELECT DISTINCT id, s.keyword as keyword
   FROM docs as D, unnest(string_to_array(D.doc,' ')) s(keyword)
   ORDER BY id;

