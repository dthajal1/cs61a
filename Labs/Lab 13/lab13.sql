.read data.sql

-- QUESTIONS --



-------------------------------------------------------------------------
------------------------ Give Interest- ---------------------------------
-------------------------------------------------------------------------

-- replace this line with your solution
UPDATE accounts SET amount = amount + 0.02 * amount;


create table give_interest_result as select * from accounts; -- just for tests

-------------------------------------------------------------------------
------------------------ Split Accounts ---------------------------------
-------------------------------------------------------------------------

-- replace this line with your solution
CREATE TABLE temporary_table as
  SELECT name ||"'s Checking account" as name, amount/2 as amount from accounts UNION
  SELECT name ||"'s Savings account", amount/2 as amount from accounts;

DELETE FROM accounts WHERE name = name;
INSERT INTO accounts(name, amount) SELECT t.name, t.amount from temporary_table as t;




create table split_account_results as select * from accounts; -- just for tests

-------------------------------------------------------------------------
-------------------------------- Whoops ---------------------------------
-------------------------------------------------------------------------

-- replace this line with your solution
DROP TABLE accounts;


CREATE TABLE average_prices AS
  SELECT category as category, avg(MSRP) as average_price from products group by category;

CREATE TABLE lowest_prices AS
  SELECT store, item, price from inventory group by item having price = min(price);

CREATE TABLE shopping_list AS
  SELECT p.name, l.store from products as p, inventory as l group by p.category having p.MSRP = l.price;

CREATE TABLE total_bandwidth AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
