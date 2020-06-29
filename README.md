
#Project Motive

###Our project's motive is to make our data easy to analyze. For that we can use normalization and denormalization in our process. 
Sparkify is a tool for big data analysis where it is distributed framework to smooth our analysis part even when we are dealing with a large set of data. 

#Database schema & ELT justification

###Database schema is a way to get a data from the data frame or view features by assigning schema value. Firstly, we will create a database that will allow us to record the data. Then we will assign the primary key (https://www.techopedia.com/definition/5547/primary-key) into our different dataset which can not be null automatically. Nowadays, data is analyzed in a raw form instead of that preloaded OLAP form. Thats why its became necessary to create a lightweight system for analysis. Thats called ETL process. 
1. Extract 
2. Load 
3. Transform 


/Users/parthpatel/Desktop/All in 1/Data Engineering/image1.png



where load and transform is a part of analytics transformation part. After combining both process we will reach to the final part of our data, which is called analysis. 

##Here, we are using some files as listed below.

1. sql_queries.py (To write our sql queries such as creating tables, inserting values)
https://www.postgresql.org/docs/9.4/ddl-constraints.html 

2. etl.py (which will extract the data and help us to transform in a form/tables which we have assigned in our sql_queries)
3. etl.ipynb (In case if we require a change into our dataset then we can modify it using etl.ipynb)
4. test.ipynb(To check whether our modifications are right and useful)

##Python script:

 1. insert the features into various fastest, dimensional set one by one. 
 https://www.postgresql.org/docs/9.5/sql-insert.html

 2. Print df.head() to check
3. Modify some values in it
4. Shut down the test.ipynb terminal 
5. Run the both files(create_tables.py, etl.py) into the main terminal 
6. See the changes occurred using test.ipynb

Repeat it after each table set to check if all are working properly.

##Reference: https://stackoverflow.com/questions/24308239/postgresql-integer-out-of-range
##https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.values.html
##Mentor help from Udacity.