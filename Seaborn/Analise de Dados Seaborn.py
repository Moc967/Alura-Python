#!/usr/bin/env python
# coding: utf-8

# # Importando base de dados

# In[1]:


import pandas as pd


# In[2]:


pd.read_csv('data/tips.csv')


# In[3]:


dados = pd.read_csv('data/tips.csv')


# In[4]:


dados.head()


# # Tradução

# In[5]:


dados.columns


# In[6]:


renomear = {
    'total_bill' : 'valor_da_conta', 
    'tip': 'gorjeta', 
    'dessert': 'sobremesa', 
    'day' : 'dia_da_semana', 
    'time' : 'hora_do_dia', 
    'size' : 'total_de_pessoas'   
}


# In[7]:


type(dados)


# In[8]:


gorjetas = dados.rename(columns = renomear)


# In[9]:


gorjetas.head(1)


# In[10]:


gorjetas.sobremesa.unique()


# In[11]:


sim_nao = {
    'No' : 'Não', 
    'Yes' : 'Sim'
}


# In[12]:


gorjetas.sobremesa.map(sim_nao)


# In[13]:


gorjetas.head(1)


# In[14]:


gorjetas.sobremesa = gorjetas.sobremesa.map(sim_nao)


# In[15]:


gorjetas.head(1)


# In[16]:


gorjetas.dia_da_semana.unique()


# In[17]:


dias = {
    'Sun' : 'Domingo',
    'Sat': 'Sábado',
    'Thur': 'Quinta', 
    'Fri' : 'Sexta'
}


# In[18]:


gorjetas.dia_da_semana = gorjetas.dia_da_semana.map(dias)


# In[19]:


gorjetas.head(1)


# In[20]:


gorjetas.hora_do_dia.unique()


# In[21]:


hora = {
    'Dinner' : 'Jantar',
    'Lunch' : 'Almoço'
}


# In[22]:


gorjetas.hora_do_dia = gorjetas.hora_do_dia.map(hora)


# In[23]:


gorjetas.head(1)


# # Importando o Seaborn

# In[24]:


get_ipython().system('pip install seaborn')


# In[25]:


import seaborn as sns


# In[26]:


get_ipython().system('pip show seaborn')


# # Análise 1 - Valor da conta e gorjeta

# In[27]:


gorjetas.columns


# In[28]:


valor_gorjeta = sns.scatterplot(x='valor_da_conta', y='gorjeta', data=gorjetas)


# **Visualmente, o valor da gorjeta aumenta conforme aumenta o valor da conta**

# In[29]:


print('A base de dados contém {} registros \n'.format(gorjetas.shape[0]))
print('Registros não nulos')
gorjetas.count()


# ## Criando o campo porcentagem

# In[30]:


gorjetas.head(1)


# In[31]:


gorjetas['porcentagem'] = gorjetas['gorjeta'] / gorjetas['valor_da_conta']


# In[32]:


gorjetas.head()


# In[33]:


gorjetas.porcentagem = gorjetas.porcentagem.round(2)


# In[34]:


gorjetas.head(3)


# In[35]:


porcentagem_conta = sns.scatterplot(x='valor_da_conta', y='porcentagem', data=gorjetas )


# **Visualmente, o valor da conta não é proporcional ao valor da gorjeta**

# In[36]:


porcentagem_conta_linha = sns.relplot(x='valor_da_conta', y='porcentagem', kind='line', data=gorjetas)


# In[37]:


sns.lmplot(x='valor_da_conta', y='porcentagem', data=gorjetas)


# In[38]:


gorjetas.head()


# In[39]:


gorjetas[gorjetas.sobremesa=='Sim'].describe()


# In[40]:


gorjetas[gorjetas.sobremesa=='Não'].describe()


# In[41]:


sns.relplot(x='valor_da_conta', y='gorjeta', hue='sobremesa', data=gorjetas)


# In[42]:


sns.catplot(x='sobremesa', y='gorjeta', data=gorjetas)


# **Visualmente, parece que temos poucas diferenças de quem pediu a sobremesa e de quem não pediu a sobremesa**

# In[43]:


sns.relplot(x='valor_da_conta', y='gorjeta', col='sobremesa', data=gorjetas)


# In[44]:


sns.lmplot(x='valor_da_conta', y='gorjeta', col='sobremesa', data=gorjetas)


# **Visualmente, a distribuição apresenta poucas diferenças**

# # Análise 2 - Sobremesa

# In[45]:


gorjetas.head()


# In[46]:


gorjetas[gorjetas.sobremesa =='Sim'].describe()


# In[47]:


gorjetas[gorjetas.sobremesa =='Não'].describe()


# In[48]:


sns.catplot(x='sobremesa', y='gorjeta',data=gorjetas)


# In[49]:


sns.relplot(x='valor_da_conta', y='gorjeta', hue='sobremesa', data=gorjetas)


# In[50]:


sns.relplot(x='valor_da_conta', y='gorjeta', hue='sobremesa', col='sobremesa', data=gorjetas)


# In[51]:


sns.relplot(x='valor_da_conta', y='gorjeta',col='sobremesa', data=gorjetas)


# In[52]:


sns.lmplot(x='valor_da_conta', y='gorjeta', col='sobremesa', hue='sobremesa', data=gorjetas)


# In[53]:


sns.lmplot(x='valor_da_conta', y='porcentagem', col='sobremesa', hue='sobremesa', data=gorjetas)


# In[ ]:





# In[54]:


sns.relplot(x='valor_da_conta', y='porcentagem',col='sobremesa',hue='sobremesa', kind='line', data=gorjetas)


# **Visualmente, existe uma diferença no valor da gorjeta daqueles que pediram sobremesa e não pediram sobremesa**

# ## Teste de hipótese

# **H<sup>null</sup>**
# 
# > **A distribuição da taxa da gorjeta é a mesma nos dois grupos**
# 
# **H<sup>alt</sup>**
# 
# > **A distribuição da taxa da gorjeta não é a mesma nos dois grupos**

# In[55]:


from scipy.stats import ranksums


# In[56]:


sobremesa = gorjetas.query("sobremesa == 'Sim'").porcentagem


# In[57]:


sem_sobremesa = gorjetas.query("sobremesa == 'Não'").porcentagem


# In[58]:


r = ranksums(sobremesa, sem_sobremesa)


# In[59]:


print('O valor do p-value é {}'.format(r.pvalue))


# **H<sup>null</sup>**
# 
# > **A distribuição da taxa da gorjeta é a mesma nos dois grupos**

# # Análise 3 - Dia da semana

# In[60]:


gorjetas.head()


# In[61]:


gorjetas.dia_da_semana.unique()


# In[62]:


sns.catplot(x='dia_da_semana',y='valor_da_conta', data=gorjetas)


# In[63]:


sns.relplot(x='valor_da_conta', y='gorjeta', hue='dia_da_semana', data=gorjetas)


# In[64]:


sns.relplot(x='valor_da_conta', y='porcentagem', hue='dia_da_semana', data=gorjetas)


# In[65]:


sns.relplot(x='valor_da_conta', y='gorjeta', hue='dia_da_semana', col='dia_da_semana', data=gorjetas)


# In[66]:


sns.relplot(x='valor_da_conta', y='porcentagem', hue='dia_da_semana', col='dia_da_semana', data=gorjetas)


# In[67]:


sns.lmplot(x='valor_da_conta', y='porcentagem', hue='dia_da_semana', col='dia_da_semana', data=gorjetas)


# In[68]:


media_geral_gorjetas = gorjetas.gorjeta.mean()


# In[69]:


print('A média geral das gorjetas é de {}'.format(media_geral_gorjetas))


# In[94]:


gorjetas.groupby(['dia_da_semana']).mean()


# In[70]:


gorjetas.groupby(['dia_da_semana']).mean()[['valor_da_conta', 'gorjeta', 'porcentagem']]


# In[71]:


print('Frequência dos dias')
gorjetas.dia_da_semana.value_counts()


# ## Teste de hipótese

# **H<sup>null</sup>**
# 
# > **A distribuição do valor da conta é igual no sábado e no domingo**
# 
# **H<sup>alt</sup>**
# 
# > **A distribuição do valor da conta não é igual no sábado e no domingo**

# In[72]:


valor_conta_domingo = gorjetas.query("dia_da_semana == 'Domingo'").valor_da_conta


# In[73]:


valor_conta_sabado = gorjetas.query("dia_da_semana == 'Sábado'").valor_da_conta


# In[74]:


r2 = ranksums(valor_conta_domingo, valor_conta_sabado)
print('O valor do p-value é {}'.format(r2.pvalue))


# **H<sup>null</sup>**
# 
# > **A distribuição do valor da conta é igual no sábado e no domingo**

# # Análise 4 - Hora do dia

# In[75]:


gorjetas.head()


# In[76]:


gorjetas.hora_do_dia.unique()


# In[77]:


sns.catplot(x='hora_do_dia', y='valor_da_conta', data=gorjetas)


# In[78]:


sns.catplot(x='hora_do_dia', y='valor_da_conta', kind='swarm',data=gorjetas)


# In[79]:


sns.violinplot(x='hora_do_dia', y='valor_da_conta', data=gorjetas)


# In[80]:


sns.boxplot(x='hora_do_dia', y='valor_da_conta', data=gorjetas)


# In[81]:


almoco = gorjetas.query("hora_do_dia == 'Almoço'").valor_da_conta


# In[82]:


sns.distplot(almoco)


# In[83]:


sns.distplot(almoco, kde=False)


# In[84]:


jantar = gorjetas.query("hora_do_dia == 'Jantar'").valor_da_conta


# In[85]:


sns.distplot(jantar)


# In[86]:


sns.distplot(jantar, kde=False)


# In[87]:


gorjetas.groupby(['hora_do_dia']).mean()[['valor_da_conta', 'gorjeta', 'porcentagem']]


# ## Teste de hipótese

# **H<sup>null</sup>**
# 
# > **A distribuição do valor da conta é igual no jantar e no almoço**
# 
# **H<sup>alt</sup>**
# 
# > **A distribuição do valor da conta não é igual no jantar e no almoço**

# In[88]:


r2 = ranksums(jantar, almoco)


# In[89]:


print('O valor do p-value é de {}'.format(r2.pvalue))


# **H<sup>alt</sup>**
# 
# > **A distribuição do valor da conta não é igual no jantar e no almoço**

# ## Teste de hipótese 2

# **H<sup>null</sup>**
# 
# > **A distribuição da taxa da gorjeta é igual no jantar e no almoço**
# 
# **H<sup>alt</sup>**
# 
# > **A distribuição da taxa da gorjeta não é igual no jantar e no almoço**

# In[95]:


porcentagem_almoco = gorjetas.query("hora_do_dia == 'Almoço'").porcentagem
porcentagem_almoco


# In[96]:


porcentagem_jantar = gorjetas.query("hora_do_dia == 'Jantar'").porcentagem
porcentagem_jantar


# In[92]:


r3 = ranksums(porcentagem_almoco, porcentagem_jantar)


# In[93]:


print('O valor do p-value é de {}'.format(r3.pvalue))


# **H<sup>null</sup>**
# 
# > **A distribuição da taxa da gorjeta é igual no jantar e no almoço**
