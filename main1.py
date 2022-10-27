import sqlite3

from faker import Faker

faker = Faker()

def create_person():
    con = sqlite3.connect("lc32.db")
    cur = con.cursor()
    sql = '''
    CREATE TABLE IF NOT EXISTS person(
    personid INTEGER NOT NULL PRIMARY KEY,
    first_name VARCHAR(128) NOT NULL,
    last_name VARCHAR(128) NOT NULL,
    Address VARCHAR(1024) NOT NULL,
    job VARCHAR(128) NOT NULL,
    Age INTEGER NOT NULL
    )
    '''
    cur.execute(sql)
    con.close()

def insrt_person(first_name, last_name, Address, job, Age):
    con = sqlite3.connect("lc32.db")
    cur = con.cursor()
    sql = f'''
        INSERT INTO person (first_name, last_name, Address, job, Age)
        VALUES
            ('{first_name}', '{last_name}', '{Address}', '{job}', '{Age}')
    '''
    cur.execute(sql)
    con.commit()
    con.close()

def print_person():
    con = sqlite3.connect("lc32.db")
    cur = con.cursor()
    sql = '''
        SELECT personid, first_name, last_name, Address, job, Age FROM person
        '''
    persons = cur.execute(sql)
    for n in persons:
        print(n)
    con.close()

def delete_person_by_id(personid):
    con = sqlite3.connect("lc32.db")
    cur = con.cursor()
    sql = f'''
        DELETE FROM person WHERE personid={personid}
        '''
    cur.execute(sql)
    con.commit()
    con.close()

def update_person_name(personid, name):
    con = sqlite3.connect("lc32.db")
    cur = con.cursor()
    sql = f'''
        UPDATE person 
        SET first_name='{name}'
        WHERE personid={personid}
        '''
    cur.execute(sql)
    con.commit()
    con.close()

create_person()

#for n in range(11):
#    insrt_person(faker.first_name(), faker.last_name(), faker.address(), faker.job(), faker.random_int())

#delete_person_by_id(1)
#update_person_name(1, 'Ann')

print_person()