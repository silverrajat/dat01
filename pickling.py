#pickling 

import pickle
name = ["rajat","himanshu","simri","sudhanshu"]
skill = ["data analyst","business man","software engineer","manager"]
pickle_file = open("emp1.dat","wb")
pickle.dump(name,pickle_file)
pickle.dump(skill,pickle_file)

pickle_file.close()


#unpickling

import pickle
pickle_file=open("emp1.dat","rb")
name_list = pickle.load(pickle_file)
skill_list = pickle.load(pickle_file)
print(name_list,"\n",skill_list )

list1=["Bat-man","Spider-man","Iron-man","Thor"]
dict1={1:"Good Morning",2:"Good Noon",3:"Good Afternoon"}

import pickle
p_file=open("myobjects.dat",'wb')
pickle.dump(list1,p_file)
pickle.dump(dict1,p_file)
p_file.close()

import pickle

p_file=open("myobjects.dat",'rb')
mylist=pickle.load(p_file)
mydict=pickle.load(p_file)
print(mylist,"\n",mydict)