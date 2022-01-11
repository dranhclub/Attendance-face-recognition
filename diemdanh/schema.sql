DROP TABLE IF EXISTS student;

CREATE TABLE student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name NVARCHAR(50),
    img BLOB,
    encoding_face BLOB
);
