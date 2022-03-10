import psycopg2

conn = psycopg2.connect("postgresql://movie_rental:2h6WBFyGVUv88qgJ@localhost/movies")
cur = conn.cursor()

print("Please enter employee ID name")
employeeName = string(input())

empoyeeNum = cur.execute("""
	SELECT employeeID FROM employee WHERE name ==
	VALUES (%s) RETURNING serial; """, ( ));

addAnotherSale = true;

while (addAnotherSale):
	print("Please enter amount of sale: ")
	amount = int(input())
	cur.execute(
		"""
		INSERT INTO Sales
		(COLUMN Total, soldBy)
		VALUES ( %s, %s)
		""", 
		(amount, employeeID));
	rental_id = cur.fetchone()[0]
	conn.commit()
	print(“Do you wish to enter another sale?”)
	print(“(1) Yes”)
	print(“(2) No.”)
	addAnotherSale = int(input())
	if (addAnotherSale == 2)
		addAnotherSale = false
cur.close()
conn.close()
    
