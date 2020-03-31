## Chpt. 1 Intro to RD
- The Relational Model
    - developed by EF Codd
    - separates retieval of info from its storage method
- RDBMS (Relational Database Management System)
    - eg. MySQL, postgresQL
## Chpt. 2 Entity Relationship Diagrams
- developing a database model
    - identify the data that need to be stored
    - think about what you want to get out of the database
        - what kinds of analysis and reports would you like to be able to review
    
    - https://app.quickdatabasediagrams.com/ is good tool to quickly create diagrams with datatypes and etc.

- object name conventions
    - capitalization: most RDBMSs are case insensitive, but if you use capitalization it must be consistent
    - spacing: add complexity to scripts being written, must wrap in quotes that add complexity
        - instead should use camelcase, hyphens, or underscoring
    - reserved words: avoid using internal function names in table names
    - plural vs. singular: pick a convention and stick with it
    - avoid acronyms: use full, legible words

## Chpt. 3 Data Integrity and Validation
- establishing tables indexes
    - can be added to any column frequently used in search and table joins
    - adding too many will slow down searching
    - CREATE INDEX [INDEX_NAME] ON [TABLE] [TABLE_COLUMN]
- adding check constraints
    - can add numerical checks such as "must be greater/less than value"
    - character check constraints: limit acceptible values to an approved list
        - CONSTRAINT [CONST_NAME] CHECK ([SOME_COL] = 'VALUE' OR [SOME_COL] = 'DIFF_VALUE')
## Chpt. 4 Relationships
- Cardinality and Optionality
    - Cardinality: Maximum number of associated records between two tables (usually 1 or many, ie. 1-1, 1-N, N-N)
        - eg. product has one supplier, cardinality = 1
- Relationships
    - 1-N: one to many
    - 1-1: one to one
    - N-N: many to many
        - students to classes (students enrolled in many classes, classes have many students)
        - typically implemented with linking table.
            - e.g. student, classes, and student_classes table, where the latter is studentID, CourseID, and grade, with PK concatenation of student and course IDs
- self-joins
    - columns in same table relation
    - model hierarchies within the same class 
        - eg. employees table, where each row records an employee and their supervisor id, but the table also has a row for the supervisor, so its id field is referenced by other rows in the same table (as supervisor id )
- cascading updates and deletes
    - updates related keys when changed across tables, or deletes records when that associated key is deleted
    - both enabling and disabling cascading can, in different circumstances, promote data integrity
    - SQL: ON DELETE CASCADE / ON UPDATE CASCADE 


## Chpt. 5 Normalization
- first form: columns only store a single piece of data
    - eg. avoiding a comma separated list of people in a picture, by breaking out another table where the picture to person relationship is described.
- second form: all fields in the primary key are required to determine the other, non-key fields.
     - eg. if you have a table with composite PK of pictureID and firstname, and then add the last name as a column, this is violated because the pictureID is irrelevant to the persons last name.  Solve by: again break into two tables, one for picture person relationship, where person is an FK that is PK to a person table
- third form: all non-key fields are independent of all other non-key fields
    - usually occure when two fields state the same info in a different way, eg. having full state name and state abbreviation in a table 
- when to *not normalize

## Chpt. 6 SQL