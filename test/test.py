#返回陈述知识字符串
#knowname知识名，knowclass知识类，knowslot知识槽
#列表元素为字符串型
def getprint2(knowname,knowclass,knowslot):
    prints2 = ''
    prints2 += '(chunk-type count-order first second)\n'
    prints2 += '(chunk-type count-from first second)\n'
    prints2 += '(add-dm\n'
    i=0
    while i<len(knowname):
        prints2 += ' ('+str(knowname[i])+' ISA '+str(knowclass[i])+' '+str(knowslot[i])+')\n'
        i+=1
    prints2 += ')'
    return prints2

#test
kon=['b','c','d','e','f','first-goal']
knc=['count-order','count-order','count-order','count-order','count-order','count-from']
kns=['first 1 second 2','first 2 second 3','first 3 second 4','first 4 second 5','first 5 second 6','start 2 end 4']
print(getprint2(kon,knc,kns))


#返回系统参数字符串
#pa参数名，pavalue参数值
#列表元素为字符串型
def getprint1(pa,pavalue):
        prints =''
        prints +='(sgp'
        i=0
        while i<len(pa):
            prints +=' '+':'+str(pa[i])+" "+str(pavalue[i])
            i+=1
        prints +=')'
        return prints

#test
a=['esc','If','trace-detail']
b=['t','.05','high']
print(getprint1(a,b))