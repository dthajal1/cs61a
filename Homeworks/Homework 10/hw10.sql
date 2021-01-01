CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT d.name, s.size FROM dogs AS d, sizes AS s WHERE d.height > s.min and d.height <= s.max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT p.child FROM parents AS p, dogs AS d WHERE p.parent = d.name ORDER BY d.height DESC;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child as child1, b.child as child2, c.size as size FROM parents AS a, parents AS b, size_of_dogs as c, size_of_dogs as d
  WHERE a.parent = b.parent and c.size = d.size and c.name < d.name and a.child = c.name and b.child = d.name ORDER BY child1;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT child1 || ' and ' || child2 || ' are ' || size || ' siblings' FROM siblings;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);
  INSERT INTO stacks_helper SELECT name, height, height FROM dogs;
  INSERT INTO stacks_helper SELECT b.dogs ||', '|| a.name, a.height + b.stack_height, a.height FROM dogs as a, stacks_helper as b WHERE b.last_height < a.height;
  INSERT INTO stacks_helper SELECT b.dogs ||', '|| a.name, a.height + b.stack_height, a.height FROM dogs as a, stacks_helper as b WHERE b.last_height < a.height;
  INSERT INTO stacks_helper SELECT b.dogs ||', '|| a.name, a.height + b.stack_height, a.height FROM dogs as a, stacks_helper as b WHERE b.last_height < a.height;

CREATE TABLE stacks AS
  SELECT dogs, stack_height from stacks_helper WHERE stack_height >= 170 ORDER BY stack_height;
