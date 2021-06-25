### Connection python and postgresql

- Donwload  wget http://www.gutenberg.org/cache/epub/19337/pg19337.txt

- Download wget https://www.pg4e.com/code/loadbook.py

- Download wget https://www.pg4e.com/code/myutils.py

- Download wget https://www.pg4e.com/code/hidden-dist.py

- python3 loadbook.py
- pg19337.txt

#### Codes utilized

    CREATE INDEX pg19337_gin ON pg19337 USING gin(to_tsvector('english',body));

    SELECT body FROM pg19337 WHERE to_tsquery('english','goose') @@ to_tsvector('english',body) LIMIT 5;

    SELECT count(body) FROM pg19337 WHER to_tsquery('english','tiny <-> tim') @@ to_tsvector('english',body);

