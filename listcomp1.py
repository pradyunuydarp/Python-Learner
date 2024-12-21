st = input()
lst = st.split()
st2 = input()
lst2 = st2.split()
# lst3 = list(map(int,lst2))
mp = zip(lst,lst2)
print(set(mp))
lstl = [x for x in lst2 if x not in lst] 
print(lstl)