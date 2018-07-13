requests+python 接口自动化测试框架
====
1.项目概述
-------
python2.7编写；
基于requests框架；
json管理请求数据；
excel管理接口，实现接口依赖，测试结果回写，测试结果统计，并邮件发送通知。

###
2.目录简介
-------
* 2.1 base：存放基础封装，主要是对get、post方法的封装。
* 2.2 case：存放测试用例，目前使用excel管理接口用例。
* 2.3 config：配置文件，如请求数据，cookie等，未来可存放参数化的配置信息如http信息、数据库信息、邮件信息等。
* 2.4 data：封装获取接口数据，如url、请求方法、请求数据、数据依赖等。
* 2.5 main：程序入口。
* 2.6untils： 公共的工具模块。


3.效果展示图
-------
整体结构
###
![](https://github.com/hanyguoguo/interfacePython/image/tree.png)

接口测试用例
###
![](https://github.com/hanyguoguo/interfacePython/image/case.png)

邮件效果
###
![](https://github.com/hanyguoguo/interfacePython/image/email.png)
