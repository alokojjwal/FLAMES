def remove_match(m1,m2):
    for i in range(len(m1)):
        for j in range(len(m2)):
            if m1[i]==m2[j]:
                c=m1[i]
                m1.remove(c)
                m2.remove(c)
                m=m1+['*']+m2
                return [m,True]
    m=m1+['*']+m2
    return [m,False]
    
name1=input("Enter the name of the first person: ")
name2=input("Enter the name of the person to be matched: ")
name1=name1.lower()
name2=name2.lower()
name1=name1.replace(" ","")
name2=name2.replace(" ","")

l1=list(name1)
l2=list(name2)

proceed = True
while proceed:
    ret_list=remove_match(l1,l2)
    con_list=ret_list[0]
    proceed=ret_list[1]
    star_index=con_list.index('*')
    l1=con_list[:star_index]
    l2=con_list[star_index+1:]
    
count=len(l1)+len(l2)
result=['Friends','Love','Affection','Marriage','Enemy','Siblings']

while len(result)>1:
    split_index=(count%(len(result)))-1
    if split_index>=0:
        right=result[split_index+1:]
        left=result[:split_index]
        result=left+right
    else:
        result=result[:len(result)-1]
        
print(result[0])