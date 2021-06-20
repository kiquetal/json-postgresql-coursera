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

"
      select string_to_array('hola,que tal,aaa',',');

Exercise week1

INSERT INTO docs01 (doc) VALUES
('natural That leads to some confusion as we visit and revisit topics to'),
('try to get you to see the big picture while we are defining the tiny'),
('fragments that make up that big picture While the book is written'),
('linearly and if you are taking a course it will progress in a linear'),
('fashion dont hesitate to be very nonlinear in how you approach the'),
('material Look forwards and backwards and read with a light touch By'),
('skimming more advanced material without fully understanding the details'),
('you can get a better understanding of the why of programming By'),
('reviewing previous material and even redoing earlier exercises you will'),
('realize that you actually learned a lot of material even if the material');

CREATE TABLE docs01 (id SERIAL, doc TEXT, PRIMARY KEY(id));

CREATE TABLE invert01 (
keyword TEXT,
doc_id INTEGER REFERENCES docs01(id) ON DELETE CASCADE
);
insert into invert01(doc_id,keyword) select distinct id, lower(s.keyword) from docs01 d, unnest(string_to_array(d.doc,' ')) s(keyword) order by id;

exercise 2
CREATE TABLE docs02 (id SERIAL, doc TEXT, PRIMARY KEY(id));

CREATE TABLE invert02 (
keyword TEXT,
doc_id INTEGER REFERENCES docs02(id) ON DELETE CASCADE
);
INSERT INTO docs02 (doc) VALUES
('natural That leads to some confusion as we visit and revisit topics to'),
('try to get you to see the big picture while we are defining the tiny'),
('fragments that make up that big picture While the book is written'),
('linearly and if you are taking a course it will progress in a linear'),
('fashion dont hesitate to be very nonlinear in how you approach the'),
('material Look forwards and backwards and read with a light touch By'),
('skimming more advanced material without fully understanding the details'),
('you can get a better understanding of the why of programming By'),
('reviewing previous material and even redoing earlier exercises you will'),
('realize that you actually learned a lot of material even if the material');


INSERT INTO invert02(doc_id,keyword) select T.id, t.keyword from (select distinct id, lower(s.keyword) as keyword from docs01 d, unnest(string_to_array(d.doc,' ')) s(keyword) order by id) as T  where T.keyword NOT IN (select word from stop_words);
