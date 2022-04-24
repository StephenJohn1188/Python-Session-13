#!/usr/bin/env python
# coding: utf-8

# # Create Database

# In[ ]:


import sqlite3


# Working with DB using SQL
# 
# 1. create a connection object
# 2. from the connection object, crate a cursor object
# 3. Using the cursor object, call the execute method with create table query as the parameter
# 

# In[4]:


db=sqlite3.connect('student_database.db')


# Cursor
# A cursor is a temporary work area created in system memory when a sql is execute

# In[5]:


cur=db.cursor()


# In[27]:


cur.execute("create table student(id int primary key,name text,marks int )")


# In[28]:


cur.execute("insert into student(id,name,marks) values(1,'John',90)")
db.commit()


# In[30]:


print(cur.rowcount,"Record(s) inserted")


# In[34]:


cur.execute("insert into student(id,name,marks) values(2,'Jaon',85)")
db.commit()


# In[35]:


results=cur.execute("select * from student")

for row in results:
    print(row)


# In[36]:


cur.execute("insert into student(id,name,marks) values(3,'Sam',85)")
db.commit()


# In[37]:


print(cur.rowcount,"Record(s) inserted")


# In[38]:


results=cur.execute("select * from student")

for row in results:
    print(row)


# In[44]:


results=cur.execute("select id,marks from student")

for row in results:
    print(row)
                    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




