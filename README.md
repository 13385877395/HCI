# 认知建模
## 项目简介
```
认知能力评价是医学工程和工业工程中普遍存在的问题。然而，实验数据的获取是耗时的，有时甚至因为伦理原因或人文关怀而无法进行。
另一方面，使用传统的量表和生理测量方法来评价认知表现的结果可能存在主观倾向，难以量化。
随着计算机技术、信息技术和人工智能技术的飞速发展，建模与仿真方法使认知能力评价变得简单、直观、有效。
本项目通过建模和仿真技术，构造认知绩效评估的综合应用平台。

```
## 开发指南
### 目录介绍
```

-HCI  //项目根结点
    -ACT    //ACT-R python依赖包
    -config //配置文件夹
    -model  //模型文件(ACT-R->python)
    -SUBCMS //程序入口ui文件夹
    -test   //测试文件
    -ui     //子页面ui文件夹
    -view   //子页面交互文件夹
```
### 快速上手

添加依赖
```
//添加pyqt5依赖
pip install sip
pip install PyQt5

参考文章
https://blog.csdn.net/stormdony/article/details/80400032
```
git管理
```
参考文章
https://www.liaoxuefeng.com/wiki/896043488029600

git clone <path>                //下载项目包
git branch -a                   //查看所有分支
git checkout <branch_name>      //切换分支(TIP:所有项目功能都在feat分支上开发)
git checkout -b <branch_name>   //创建并且切换分支

上传项目前检测
git status                      //查看项目修改状态 modeifed 更改 delete 删除 ..
git diff                        //查看项目修改详情 
git add .                       //将文件提交到缓冲区
git commit                      //将文件提交到本地
git pull                        //在将代码提交到远端前，请求pull远端代码，防止代码冲突
git push                        //将代码提交到远端
```