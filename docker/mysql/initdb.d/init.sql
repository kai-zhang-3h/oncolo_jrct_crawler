DROP DATABASE IF EXISTS testdb;
CREATE DATABASE testdb;
DROP DATABASE IF EXISTS oncolojrctdb;
CREATE DATABASE oncolojrctdb;
USE testdb;
DROP TABLE IF EXISTS test;

CREATE TABLE test
(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name TEXT NOT NULL
)DEFAULT CHARACTER
  SET=utf8;

  INSERT INTO test
    (name)
  VALUES
    ("田中"),
    ("鈴木"),
    ("ああああああ");