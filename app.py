#!/usr/bin/env python
# coding: utf-8

# In[4]:


from flask import Flask,render_template,request


# In[5]:


import joblib


# In[6]:


app = Flask(__name__)


# In[ ]:


@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model = joblib.load("regression")
        r = model.predict([[rates]])
        return(render_template("index.html",result=r))
    else:
        return(render_template("index.html",result="WAITTING"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




