#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import gizmo_analysis as gizmo
import utilities as ut
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
get_ipython().run_line_magic('matplotlib', 'notebook')


# In[ ]:


simname = 'm12i_res7100_mhdcv'
simdir = '/scratch/projects/xsede/GalaxiesOnFIRE/mhdcv/m12i_res7100_mhdcv/1Myr/'
snapnumber = 696


# In[ ]:


part = gizmo.io.Read.read_snapshots(['star'],'snapshot_index', snapnumber, simulation_name=simname, simulation_directory=simdir, assign_hosts=True, assign_hosts_rotation=True)


# In[ ]:


part['star'].keys()


# In[ ]:


# 3-D position of star particle (particle number x dimension number) [kpc comoving]

starposition=part['star']['position'] # starposition is the array of position of all stars
ageall=part['star'].prop('age') #stored all ages in a
 
xall = part['star'].prop('host.distance.principal')[:,0] #x component of the position of all stars 
yall = part['star'].prop('host.distance.principal')[:,1] #y component of the position of all stars
zall = part['star'].prop('host.distance.principal')[:,2] #z component of the position of all stars
nall=len(xall) # counting the total no. of star particles

n=nall # This is the no. of stars we are going to use. n=nall means choose all, n=100 means choose 100
                
smallpart=starposition[0:n] # This is selecting a small part from the collection of all star positions

x=xall[0:n] # select x components from 0 to n
y=yall[0:n] # select y components from 0 to n
z=zall[0:n] # select z components from 0 to n
age=ageall[0:n]*1e9 #age converted to years Note: NOT IN GYR ANYMORE !!!!!!!!!!!

R=np.sqrt(np.square(x)+np.square(y)) #calculate the radius in the xy plane
r=np.sqrt(x**2+y**2+z**2) #calculate the spherical radius in the xyz plane


# In[ ]:





# In[ ]:




