CREATE TABLE contacts ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL, 
    age INTEGER NOT NULL, 
    email TEXT NOT NULL UNIQUE
);
CREATE TABLE users ( 
    first_name TEXT NOT NULL, 
    last_name TEXT NOT NULL, 
    age INTEGER NOT NULL, 
    country TEXT NOT NULL, 
    phone TEXT NOT NULL, 
    balance INTEGER NOT NULL
);

ALTER TABLE contacts RENAME TO new_contacts;