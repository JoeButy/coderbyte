import pandas as pd
def smartAssigning(names, statuses, projects, tasks):
    
 df = pd.DataFrame({'name':names,'vac':statuses,'proj':projects,'tasks':tasks})
 df = df[df['vac'] == False]
 df = df.sort_values(by=['tasks', 'proj'], ascending=[True, True]).reset_index(drop=True)
 print df
 return df.loc[0,'name']

names = ["John", 
 "Martin"]
statuses = [True, False]
projects = [2, 1]
tasks = [16, 5]

print smartAssigning(names, statuses, projects, tasks)