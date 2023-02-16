#!/usr/bin/env python
# coding: utf-8

# In[6]:


from tabulate import tabulate 


# In[7]:


import SISTEM as sis


# In[8]:


transaksi = sis.Transaction()


# In[9]:


transaksi.show_order()


# #### Test 1

# Customer ingin menambahkan dua item baru menggunakan method add_item(). Item  yang ditambahkan adalah sebagai berikut : 
# 
#     - Nama item : Ayam Goreng, Qty:2, Harga : 20000
#     - Nama Item : Pasta Gigi, Qty:3, Harga : 15000

# In[11]:


transaksi.add_item("ayam goreng", 2, 20000)
transaksi.add_item("Pasta Gigi", 3, 15000)
transaksi.show_order()


# #### Test 2

# Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan 
# maka customer menggunakan method delete_item() untuk menghapus item. item yang 
# ingin dihapuskan adalah pasta gigi. 
# 

# In[14]:


transaksi.delete_item("Pasta Gigi")
transaksi.show_order()


# #### Test 3 

# Ternyata setelah dipikir - pikir customer salah memasukan item yang ingin dibelanjakan!
# daripada menghapusnya satu - satu, maka customer cukup menggunakan method 
# reset_transaction(). untuk menghapus semu item yang sudah ditambahkan. 

# In[15]:


transaksi.reset_transaction()
transaksi.show_order()


# #### Test 4

# Setelah customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan
# menggunakan method total_price(). Sebelum mengeluarkan output totla belanja akan 
# menampilkan item - item yang dibeli 

# In[16]:


transaksi.add_item("Sabun",5,10000)
transaksi.add_item("Handuk",2,7000)
transaksi.add_item("Minyak Goreng",5,20000)
transaksi.add_item("Kecap Manis",4,10000)
transaksi.show_order()


# In[ ]:





# In[ ]:





# In[ ]:




