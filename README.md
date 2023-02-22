# NKU-COSC0013-数据库系统
数据库大作业各项要求及加分项均实现，如果需要保姆式手把手解析欢迎邮件联系我

### 基于服务器部署和权限约束的图书管理系统



#### 一. 说明

+ 该数据库已经实现部署到服务器上
+ 该数据库各种功能设计考虑了管理员权限，通过登录获取管理员信息及根据该管理员所管权限下执行更新、删除等操作
+ 实验报告中一开始没有考虑到部署服务器这个功能，因此其中四-八部分是按照未部署服务器写的代码与程序演示，后来根据助教发的实验考核标准，我又增加了部署服务器功能，但是因为部署服务器未改变功能实现部分功能及程序演示，因此四-八部分未作调整 ，部署服务器后将有关服务器连接等服务器端、客户端代码单独在模块九详细写出

#### 二. 系统主要功能简介

1. **功能1**：注册管理员信息

   注册需要填写管理员ID、姓名和设置登录密码（输入密码可设置可见或隐藏），注册信息会保存到数据库administrate表中

2. **功能2**：登录验证

   登录需要ID和密码（ID和密码需要已经保存在数据库administrate表中）且不能为空

3. **功能3**：按图书号查询图书信息

   输入书号，按照书号索引数据库中该图书全部信息

4. **功能4**：按书架查询图书信息

   输入书架号，可以查询该书架上所有图书的全部信息

5. **功能5**：查询借还信息

   输入书号，可以索引该书全部借还信息（借阅人学号、书号借阅时间及归还时间）

6. **功能6**：查询读者信息

   输入读者学号，可以查询该读者全部信息（学号、姓名、性别）

7. **功能7**：更新管理员所属权限图书信息

   更新的图书范围仅限该管理员权限内，可以修改图书书名、作者、价格等信息，当更新图书价格小于0时不予更新修改

8. **功能8**：添加借还记录

   读者借书时为其添加借还记录，同时更改该reader表该读者可借图书以及在借图书，book表所借图书在馆数量

9. **功能9**：删除管理所属图书信息

   删除该管理员权限下所管理的指定（书号）图书或全部图书信息
