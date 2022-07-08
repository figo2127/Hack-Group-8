#!/usr/bin/env python
# coding: utf-8

# In[160]:


get_ipython().run_cell_magic('gremlin', '', 'g.V().drop()')


# In[162]:


get_ipython().run_cell_magic('gremlin', '', "\n//populate the graph database with data\ng.\n// qn: How to link a SPR with a DID?\naddV('Tag').property('name', 'SPR to DID').\naddV('Tag').property('name', 'a SPR a DID').\naddV('Tag').property('name', 'SPR').\n\n// qn: new joiner\naddV('Tag').property('name', 'SDLC New Hire').\n\n// qn: How to create a Procmon script?\naddV('Tag').property('name', 'a Procmon script').\n\naddV('URL').property('name', 'http://confluence.com/sdlc/new-hires').\naddV('URL').property('name', 'http://gitlab.com/gs/new-joiners').\naddV('URL').property('name', 'http://confluence.com/procmon/creation').\n\n// found in\nV().hasLabel('URL').has('name','http://confluence.com/sdlc/new-hires').as('a').V().hasLabel('Tag').has('name','a SPR a DID').addE('found in').to('a').property('confidence', 0.9).\nV().hasLabel('URL').has('name','http://gitlab.com/gs/new-joiners').as('a').V().hasLabel('Tag').has('name','a SPR a DID').addE('found in').to('a').property('confidence', 0.95).\nV().hasLabel('URL').has('name','http://confluence.com/procmon/creation').as('a').V().hasLabel('Tag').has('name','a SPR a DID').addE('found in').to('a').property('confidence', 0.67).\nV().hasLabel('URL').has('name','http://gitlab.com/gs/new-joiners').as('a').V().hasLabel('Tag').has('name','SDLC New Hire').addE('found in').to('a').property('confidence', 0.7).\nV().hasLabel('URL').has('name','http://confluence.com/procmon/creation').as('a').V().hasLabel('Tag').has('name','a Procmon script').addE('found in').to('a').property('confidence', 0.7).\n\n// links to \nV().hasLabel('URL').has('name','http://confluence.com/procmon/creation').as('a').V().hasLabel('URL').has('name','http://gitlab.com/gs/new-joiners').addE('links to').to('a').property('confidence', 0.7).\nV().hasLabel('URL').has('name','http://gitlab.com/gs/new-joiners').as('a').V().hasLabel('URL').has('name','http://confluence.com/sdlc/new-hires').addE('links to').to('a').property('confidence', 0.73)\n\n")


# In[137]:


get_ipython().run_cell_magic('gremlin', '', '\n//list all the entries in the Neptune cluster\ng.V().valueMap()')


# In[138]:


get_ipython().run_cell_magic('gremlin', '', "\ng.V().hasLabel('Tag').has('name', 'SPR to DID').valueMap()")


# In[164]:


get_ipython().run_cell_magic('gremlin', '-p v,oute,inv', '\ng.V().outE().inV().path()')


# In[158]:


get_ipython().run_cell_magic('gremlin', '', '\ng.V().hasLabel("Tag").has("name", "a SPR a DID").outE("found in").values("confidence").toList()')


# In[159]:


get_ipython().run_cell_magic('gremlin', '', '\ng.V().hasLabel("Tag").has("name", "a SPR a DID").out("found in").values("name").toList()')


# In[ ]:




