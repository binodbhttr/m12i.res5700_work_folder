#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def cylindrical_cut(R1,R2):
    ind_cylindrical_cut=np.where((R>R1)&(R<R2))
    x_cut=x[ind_cylindrical_cut]
    y_cut=y[ind_cylindrical_cut]
    z_cut=z[ind_cylindrical_cut]
    age_cut=age[ind_cylindrical_cut]
    R_cut=R[ind_cylindrical_cut]

