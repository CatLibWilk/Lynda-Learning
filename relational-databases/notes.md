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