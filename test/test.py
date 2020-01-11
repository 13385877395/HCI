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


def getprint3(modelFeatureList):
    prints = ''
    i = 0
    while i < len( modelFeatureList ):
        prints +=  str( modelFeatureList[i][0] ) + " " + str( modelFeatureList[i][1] ) +" "+ str( modelFeatureList[i][2] )+"\n"
        i += 1
    return prints
#陈述知识类传参
def getprint4(stateCalssFeatureList):
    prints = ''
    for feature in stateCalssFeatureList:
        str = '(chunk - type'
        for i in feature:
            str +=' '+ i
        str+=')'
        prints+=str+'\n'
    return prints
#陈述知识传参
def getprint5(stateFeatureList):
    prints = '(add-dm\n'
    for feature in stateFeatureList:
        str = ' ('
        str +=feature[0]+' ISA'
        for i in feature[1:]:
            str +=' '+ i
        str+=')'
        prints+=str+'\n'
    prints +=')'
    return prints



def create_file1(file_path,msg):
    f=open(file_path,"w")
    f.write(msg)
    f.close
def create_file2(file_path,msg):
    f=open(file_path,"a")
    f.write(msg)
    f.close