#返回陈述知识字符串
#knowstatement为陈述知识
#传单个列表，列表元素为三个元素的元组
def getprint2(knowstatement):
    prints2 = ''
    prints2 += '(chunk-type count-order first second)\n'
    prints2 += '(chunk-type count-from first second)\n'
    prints2 += '(add-dm\n'
    i=0
    while i<len(knowstatement):
        prints2 += ' ('+str(knowstatement[i][0])+' ISA '+str(knowstatement[i][1])+' '+str(knowstatement[i][2])+')\n'
        i+=1
    prints2 += ')'
    return prints2

#test
know=[('b','count-order','first 1 second 2'),('c','count-order','first 2 second 3'),('d','count-order','first 3 second 4')]
print(getprint2(know))


#返回系统参数字符串
#sysparameter为系统参数
#传一个列表，列表元素为两个元素的元组
def getprint1(sysparameter):
        prints =''
        prints +='(sgp'
        i=0
        while i<len(sysparameter):
            prints +=' '+':'+str(sysparameter[i][0])+" "+str(sysparameter[i][1])
            i+=1
        prints +=')'
        return prints

#test
a=[('esc',.05 ), ('if','high') ]
print(getprint1(a))


def create__file1(file_path,msg):
    f=open(file_path,"w")
    f.write(msg)
    f.close
def create__file2(file_path,msg):
    f=open(file_path,"a")
    f.write(msg)
    f.close