#!/usr/bin/env python
# coding: utf-8

# In[72]:


# сумма всех часов в строке
pack = '1h 45m, 360s, 25m, 30m 120s, 2h 60s'
split_pack = [i.replace(',', '') for i in pack.split()]
hours = []

def parse_value(time_string):
    for i in time_string:
        if i.endswith('h'):
            hours.append(int(i.replace('h', '')))
        elif i.endswith('m'):
            hours.append(int(i.replace('m', '')) / 60)
        else:
            hours.append(int(i.replace('s', '')) / 360)
    return round(sum(hours), 1)


# In[73]:


print(parse_value(split_pack))

