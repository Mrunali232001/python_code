#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install virtualenv


# In[2]:


pip install Flask


# In[3]:


# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, redirect, url_for, request
 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
 
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name
 
 
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))
     
    
    
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'mrunali'
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()


# In[5]:


from flask import Flask
app = Flask(__name__)
 
@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name
 
if __name__ == '__main__':
   app.run()


# In[ ]:


from flask import Flask, redirect, url_for, request
app = Flask(__name__)
 
 
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name
 
 
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))
 
 
if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




