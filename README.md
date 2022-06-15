# Book-Management-System-Based-on-Permission-Constraint-and-Server-Deploymen
## <center>数据库大作业报告

​												       		姓名： 聂志强   学号：2012307  班级：信息安全

### 实验要求

1. 完成一个小型的数据库信息管理系统（或部分功能），并填写工程作业报告；程序和报告请在规定时间之内上传。
2. 开发模式（B/S或C/S）、开发高级语言任选，后台数据库使用大型数据库管理系统（SQL Server、Oracle、MySQL等），不要使用桌面数据库。
3. 报告中所列举的四种操作，每种操作举一个例子即可。
4. 作业成绩按照报告中的标准评分，程序只实现报告中涉及的部分即可。
5. 作业完成后，请将工程作业报告和程序打包提交给助教老师，并联系助教老师进行系统说明和演示，回答相关问题。

### 一. 项目信息（10分）

  1. #### **项目名称**：==基于权限约束和服务器部署的图书管理系统==

  2. #### **必备环境**：

     python 3.8.5   MySQL

  3. #### **系统主要功能简介**（4分）

     + ==说明==

       + ==**该数据库已经实现部署到服务器上**==

       + 该数据库各种功能设计考虑了管理员权限，通过登录获取管理员信息及根据**该管理员所管权限下**执行更新、删除等操作

       + 写实验报告的时候一开始没有考虑到部署服务器这个功能，因此下述四-八部分是按照未部署服务器写的代码与程序演示，后来根据助教发的实验考核标准，我又增加了部署服务器功能，但是因为部署服务器未改变功能实现部分功能及程序演示，因此四-八部分未作调整 ，部署服务器后将有关服务器连接等服务器端、客户端代码单独在模块九详细写出

       + 为了便于您浏览批阅，以下所有展示代码的部分：**核心代码**以文本代码方式给出便于浏览，**全部代码**以截图方式给出减小空冗余

         

     + ##### 功能1：注册管理员信息

       注册需要填写管理员ID、姓名和设置登录密码（输入密码可设置可见或隐藏），注册信息会保存到数据库administrate表中

       

     + ##### 功能2：登录验证

       登录需要ID和密码（ID和密码需要已经保存在数据库administrate表中）且不能为空

       

     + ##### 功能3：按图书号查询图书信息

       输入书号，按照书号索引数据库中该图书全部信息

       

     + ##### 功能4：按书架查询图书信息

       输入书架号，可以查询该书架上所有图书的全部信息

       

     + ##### 功能5：查询借还信息

       输入书号，可以索引该书全部借还信息（借阅人学号、书号借阅时间及归还时间）

       

     + ##### 功能6：查询读者信息

       输入读者学号，可以查询该读者全部信息（学号、姓名、性别）

       

     + ##### 功能7：更新管理员所属权限图书信息

       更新的图书范围仅限该管理员权限内，可以修改图书书名、作者、价格等信息，当更新图书价格小于0时不予更新修改

       

     + ##### 功能8：添加借还记录

       读者借书时为其添加借还记录，同时更改该reader表该读者可借图书以及在借图书，book表所借图书在馆数量

       

     + ##### 功能9：删除管理所属图书信息

       删除该管理员权限下所管理的**指定**（书号）图书或**全部**图书信息

     

  4. #### **系统主要页面截图**（6分）

     + ##### 登录及注册页面

       登录需要ID和密码（ID和密码需要已经保存在数据库administrate表中）且不能为空，注册需要填写管理员ID、姓名和设置登录密码（输入密码可设置可见或隐藏），注册信息会保存到数据库administrate表中

       <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\登录.jpg" style="zoom: 25%;" />   <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\注册页面.jpg" style="zoom:25%;" />

       

     + #####  图书管理系统主页

       可以前往查询中心，更新图书信息，添加借还记录，删除图书信息等页面

       <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\主页.jpg" style="zoom: 50%;" />

       

     + ##### 查询中心

       可以分别查询图书、借还信息、读者信息和书架图书信息

       <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\查询中心.jpg" style="zoom:50%;" />

       

     + #####  查询读者信息页面（设有滚轮）

       可以查询全部或指定学号读者信息，添加读者信息等

       <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\查询读者信息.jpg" style="zoom:50%;" />

     


### 二. 系统配置（10分）

1. 说明

   + （2分）请说明系统配置情况（后台数据库，高级语言）；

   + （8分）请使用连接串连接高级语言和数据库，并分析字符串的各个部分。

     

1. 配置步骤（2分）

   + DBMS

     + 后端使用数据库MySQL
     + 端口：3306，用户名：root

   + 高级语言

     + Python 3.8，使用PyCharm
     + 前端界面主要使用Tkinter类库完成可视化
     + Pymysql类库连接数据库

   + 连接串分析

     | 序号 |    名称    |     功能说明     |     取值      |
     | :--: | :--------: | :--------------: | :-----------: |
     |  1   |    host    | 数据库连接的主机 | 114.116.89.58 |
     |  2   |    user    |   Mysql用户名    |     root      |
     |  3   |  password  |  Mysql登录密码   |  SS111827jj   |
     |  4   |  database  |   使用的数据库   |    library    |
     |  5   |    port    |     连接端口     |     3306      |
     |  6   | autocommit | 打开自动提交功能 |     True      |

   + 连接串代码（截屏）

     ![](服务器.jpg)



### 三. 数据库设计（14分）

1. 说明：

   （10分）按照数据表的创建顺序，依次给出所涉及数据表的信息，其中参照字段以“（字段1，字段2，……，字段n）”的形式给出，被参照字段以“表名（字段1，字段2，……，字段n）”的形式给出；

   （4分）一般DBMS都可以为数据库生成关系图，请将该图片截屏并粘贴到表格中。

   

2. 数据表（10）

   <table  width="200" height="300" border="1" >
       <td style="text-align:center ">  <b>数据表名称</b></td> 
       <td style="text-align:center "><b>主键</b></td>
       <td style="text-align:center " ><b>参照属性</b></td>
       <td style="text-align:center "><b>被参照属性</b></td>
   <tr>
       <td style="text-align:center " >book</td>
   	<td style="text-align:center ">book_number</td>
       <td style="text-align:center " >No_bookshelf</td>
   	<td style="text-align:center ">bookshelf(No_bookshelf)</td>
   <tr>
   <tr>
        <td style="text-align:center " >bookshelf</td>    
        <td style="text-align:center ">No_bookshelf</td>    
        <td style="text-align:center " >NULL</td>    
        <td style="text-align:center ">NULL</td>  
   <tr/>
   <tr>    
        <td style="text-align:center " >bookshelf</td>    
        <td style="text-align:center ">No_bookshelf,     location</td>    
        <td style="text-align:center " >ID</td>    
        <td style="text-align:center ">administrator(ID)</td>
   <tr>
   <tr>
        <td style="text-align:center " >administrator</td>    
        <td style="text-align:center ">ID</td>    
        <td style="text-align:center " >NULL</td>    
        <td style="text-align:center ">NULL</td>  
   <tr/>
   <tr>
       <td rowspan="2" style="text-align:center " >borrow_or_return</td>
       <td rowspan="2" style="text-align:center " >student_number  ， book_number</td>
       <td style="text-align:center " >student_number</td>
       <td style="text-align:center " >reader(student_number)</td>
   </tr>
   	<tr>
   		<td style="text-align:center " >book_number</td>
           <td style="text-align:center " >book(book_number)</td>
   	</tr>
   <tr>
       <td rowspan="2" style="text-align:center " >comment_section</td>
       <td rowspan="2" style="text-align:center " >Time , Comment_content</td>
       <td style="text-align:center " >student_number</td>
       <td style="text-align:center " >reader(student_number)</td>
   </tr>
   	<tr>
   		<td style="text-align:center " >administrator</td>
           <td style="text-align:center " >administrator(ID)</td>
   	</tr>
   </table>

   

3. 关系图（4）

   <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\navicate关系图.jpg" style="zoom:80%;" />

   ​         



### 四. 含有事务应用的删除操作（13分）

1. #### 说明 

   + （1分）简要说明该操作所要完成的功能；

   + （2分）该操作会涉及的表（必须含有两张或两张以上的关系表，同时以“表名”的形式给出）

   + （1分）表连接涉及字段描述（描述方式为“表1.属性=表2.属性”）

   + （1分）删除条件涉及的字段描述(以“表名.属性=？”形式给出)  

   + （4分）实现该操作的关键代码（高级语言、SQL），截图即可；（其中如果删除语句中不包含任何形式的事务应用将扣除3分）

   + （4分）如何执行该操作，按所述方法能够正常演示程序则给分。

     

2. #### 功能描述（1分）

   删除该**管理员权限**下所管理的**指定**（书号）图书或**全部**图书信息

   

3. #### 涉及的表（2分）

   book, bookshelf

   

4. ####  表连接涉及字段（1分）

   book.No_bookshelf = bookshelf.No_bookshelf

   

5. ####  删除条件字段描述（1分）

   通过管理员ID和书号book_number确定删除图书信息

6. ####  代码（4分）

   核心代码：

   ```python
   def delete(old_otherFrame, id):
       old_otherFrame.withdraw()
       otherFrame = Toplevel()
       otherFrame.geometry("800x600")
       otherFrame.title("删除书籍")
   
       sql = "delete from book " \
             "where No_bookshelf in (select No_bookshelf from bookshelf where ID= '"+id+"');"
       tree = ttk.Treeview(otherFrame)
       ls = ["管理员ID", "书号", "书架号"]
       tree["columns"] = ("管理员ID", "书号", "书架号")
       for i in ls:
           tree.column(i, anchor="center")
           tree.heading(i, text=i)
       temp = "SELECT ID, book_number, No_bookshelf from book natural join bookshelf where ID= "+id+" ;"
       cursor.execute(temp)
       result = cursor.fetchall()
       for i in range(len(result)):
           tree.insert("", i, values=result[i])
       tree['show'] = 'headings'
       tree.place(relx=0.15, rely=0.05, relheight=0.3)
       # 滚动条控件
       VScroll1 = Scrollbar(tree, orient='vertical', command=tree.yview)
       VScroll1.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)
       # 给treeview添加配置
       tree.configure(yscrollcommand=VScroll1.set)
       if len(result) == 0:
           messagebox.showinfo(message='当前管理员权限下无图书')
           quiteInfo()
       else:
           Label(otherFrame, text='请输入书号', font=('Arial', 18)).place(relx=0.37, rely=0.5, width=200)
           e1 = StringVar()
           Entry(otherFrame, show='', textvariable=e1, font=('Arial', 14)).place(relx=0.37, rely=0.6, width=200)
   
           click = lambda: f4(otherFrame, e1, id)
           Button(otherFrame, text='删除所选书号', command=click).place(relx=0.37, rely=0.7, width=200)
           click = lambda: f6(otherFrame, sql)
           Button(otherFrame, text='删除全部图书信息', command=click).place(relx=0.37, rely=0.8, width=200)
           Button(otherFrame, text="返回上一页", command=quiteInfo).place(relx=0.37, rely=0.9, width=200)
           Button(otherFrame, text='退出', command=handler).place(relx=0.9, rely=0.95, relwidth=0.1)
   
   
   def f4(otherFrame,e1,id):
       e1 = e1.get()
       try:
           cursor.execute("START TRANSACTION")
           sql = "delete from book  " \
                 "where  book_number='"+e1+"' and No_bookshelf " \
                 "in (select No_bookshelf from bookshelf where ID='"+id+"');"
           # sql2 = "INSERT INTO book VALUES('831','1','python','陈晨',65.6,3,3);"
           cursor.execute(sql)
           # cursor.execute(sql2)
           messagebox.showinfo(message='删除成功！')
           db.commit()
       except Exception as m:
           messagebox.showerror('警告', m.args)
           db.rollback()
   
   def f6(otherFrame, sql):
       cursor.execute("START TRANSACTION")
       cursor.execute(sql)
       cursor.execute("COMMIT")
       messagebox.showinfo(message='已删除')
   ```

   

7. #### 程序演示(含事务操作)（4分）

   + 删除管理员（ID：101）权限下所管理的书号为732的图书信息，未发生异常，执行`commit()`并成功删除

     ```python
     def f4(otherFrame,e1,id):
         e1 = e1.get()
         try:
             cursor.execute("START TRANSACTION")
             sql = "delete from book  " \
                   "where  book_number='"+e1+"' and No_bookshelf " \
                   "in (select No_bookshelf from bookshelf where ID='"+id+"');"
             cursor.execute(sql)
             messagebox.showinfo(message='删除成功！')
             db.commit()
         except Exception as m:
             messagebox.showerror('警告', m.args)
             db.rollback()
     ```

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\删除事务.jpg" style="zoom:50%;" />

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\删除事务2.jpg" style="zoom: 50%;" />

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\删除事务3.jpg" style="zoom:50%;" />

     

     

   + 特意添加sql2指令来违背主键约束**引发异常**，导致发生`rollback()`**回滚**，查看数据库发现并没有删除书号为825的图书信息

     ```python
     def f4(otherFrame,e1,id):
         e1 = e1.get()
         try:
             cursor.execute("START TRANSACTION")
             sql = "delete from book  " \
                   "where  book_number='"+e1+"' and No_bookshelf " \
                   "in (select No_bookshelf from bookshelf where ID='"+id+"');"
             sql2 = "INSERT INTO book VALUES('831','1','python','陈晨',65.6,3,3);"
             cursor.execute(sql)
             cursor.execute(sql2)
             messagebox.showinfo(message='删除成功！')
             db.commit()
         except Exception as m:
             messagebox.showerror('警告', m.args)
             db.rollback()
     ```

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\异常事务4.jpg" style="zoom:50%;" />

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\删除事务3.jpg" style="zoom:50%;" />

     ​        

      

      

       

        

     

### 五. 触发器控制下的添加操作（20分）

1. #### 说明

   + （1分）简要说明该操作所要完成的功能；

   + （2分）简要说明该触发器所要完成的功能

   + （1分）该操作会涉及的表（以“表名”的形式给出）。

   + （2分）该操作输入数据以及输入数据应该满足的条件，如：数值范围、是否为空；

   + （6分）实现该操作的关键代码（高级语言、SQL），截图即可；

   + （8分）如何执行该操作，按所述方法能够正常演示程序则给分。

     

2. #### 功能描述（1分）

   读者借书时为其添加借还记录，同时更改该reader表该读者可借图书以及在借图书，book表所借图书在馆数量

   

3. #### 触发器描述（2分）

   + 如果该读者可借图书数量为0（已达借书数量上限），则该读者不可借书

   + 如果所借图书在馆数量为0（已经被全部借出），则该图书不可借

   + 如果所输入学号不存在，则不可添加借还记录，需要先将读者信息插入reader表

   + 如果所借图书书号不存在，则不可添加借还记录，需要先将该书信息插入book表

     

4. #### 涉及的表（1分）

   borrow_or_return，reader,  book

   

5. #### 输入数据（2分）

   <table  width="200" height="200" border="1" >
       <td style="text-align:center ">  <b>更改字段</b></td> 
       <td style="text-align:center "><b>规则</b></td>
   <tr>
       <td style="text-align:center " >student_number(学号)</td>
   	<td style="text-align:center ">student_number需已经在reader表存在（即读者信息已经录入）且该读者可借数量大于0</td>
   <tr>
   <tr>
        <td style="text-align:center " >book_number(书号)</td>    
        <td style="text-align:center ">book_number需已经在book表存在（即该图书信息已经录入）且该书在馆数量大于0</td>     
   <tr/>
   <tr>    
        <td style="text-align:center " >borrowing(借书时间)</td>    
        <td style="text-align:center ">无</td>    
   <tr>
   <tr>
        <td style="text-align:center " >Return_time(换书时间)</td>    
        <td style="text-align:center ">无</td>    
   <tr/>
   </table>

   ​         

   ​                     

   ​                 

   ​                    

6. #### 插入操作源码（3分）

   ##### 关键代码：

   ```mysql
   def f3(otherFrame, e1, e2, e3, e4):
       student_number = e1.get()
       book_number = e2.get()
       b_time = e3.get()
       r_time = e4.get()
       sql = "INSERT INTO borrow_or_return" \
             " values('" + student_number + "', '" + book_number + "', '" + b_time + "', '" + r_time + "');"
       sql2 = "update reader " \
              "set Number_of_books_available =Number_of_books_available-1 " \
              "where student_number ='"+student_number+"';"
       sql3 = "update reader " \
              "set Number_of_borrowed_books =Number_of_borrowed_books+1 " \
              "where student_number ='"+student_number+"';"
       sql4 = "update book " \
              "set Number_of_books_in_the_library =Number_of_books_in_the_library - 1 " \
              "where student_number ='"+student_number+"';"
       try:
           cursor.execute("START TRANSACTION")
           cursor.execute(sql)
           cursor.execute(sql2)
           cursor.execute(sql3)
           cursor.execute(sql4)
           messagebox.showinfo(message='添加借还记录成功！')
           db.commit()
       except Exception as m:
           messagebox.showerror('警告', m.args)
           db.rollback()
   ```

   

   ##### 全部代码：

   ![](D:\聂志强\大学\大二下\数据库系统\数据库大作业\触发器添加1.jpg)

   ![](D:\聂志强\大学\大二下\数据库系统\数据库大作业\触发器添加2.jpg)

   ![](D:\聂志强\大学\大二下\数据库系统\数据库大作业\触发器3.jpg)

    

   

7. #### 触发器源码（3分）

   ```mysql
   drop trigger if exists add_record;
   delimiter //
   CREATE trigger add_record
   BEFORE INSERT ON borrow_or_return FOR EACH ROW
   BEGIN
   	declare num1 smallint(4);
   	declare num2 smallint(4);
   	set num1=(select Number_of_books_available 
                from reader 
                where student_number=new.student_number );
       set num2=(select Number_of_books_in_the_library 
                from book 
                where book_number=new.book_number );
                
       IF num1<1 THEN
   		SIGNAL SQLSTATE '22003' SET MESSAGE_TEXT = '当前可借数量为0';
   	END IF;
   	
       IF num2<1 THEN
   		SIGNAL SQLSTATE '22002' SET MESSAGE_TEXT = '该书在馆数量为0';
   	END IF;
   	
   	IF new.student_number not in (select student_number from reader) 
   	THEN
   		SIGNAL SQLSTATE '22004' SET MESSAGE_TEXT = '该读者信息不存在';
   	END IF;
   	
       IF new.book_number not in (select book_number from book) 
   	THEN
   		SIGNAL SQLSTATE '22005' SET MESSAGE_TEXT = '该图书信息不存在';
   	END IF;
   	
   END;//
   DELIMITER;
   ```

   

   触发器设置执行成功截图

   <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\触发器截图.jpg" style="zoom:50%;" />

   ​    

   ​            

   ​                   

   

   ​                 

   

8. #### 程序演示（4分）

   说明：不违背触发器能够执行插入操作。

   + 插入学号为“2011212”，书号为“825”，借书时间为“2022-01-10”，换书时间为“2022-03-11”的借还信息
   + 观察reader表：插入后该读者可借数目由5变为4，在借数目由0变为1
   + 观察book表：插入后书号为825的图书在馆数量由1变为0

   ​          插入前：

   <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\111111.jpg" style="zoom:50%;" />

   

   <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\22222222222222.jpg" style="zoom:50%;" />

   

   <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\触发器下添加操作（成功）.jpg" style="zoom:50%;" />

   ​               

   ​                     

   

   ​                 

   ​                插入后：

   <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\1111111111.jpg" style="zoom:50%;" />

   

   <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\222222.jpg" style="zoom:50%;" />

   ​     

   

9. #### 程序演示（4分）

   说明：违背触发器要求，不能够执行插入操作，系统报错。

   + **该读者借阅数量已达上限**：加学号为2011708读者的借书记录，该读者当前图书可借数量（Number_of_books_available）为0，当前不可借书，因此添加借还记录时违背触发器要求而不能够执行插入操作

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\添加违背触发器222.jpg" style="zoom:50%;" />

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\违背触发器借书.jpg" style="zoom:50%;" />

     ​                   

     ​                       

     

   + **所借图书在馆数量为0**：书号为831的图书在馆数量为0，违背触发器要求而不能够执行插入操作

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\在馆为0.jpg" style="zoom:50%;" />

     

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\触发器存储违背（在馆为0）.jpg" style="zoom:50%;" />

     ​     

   + **读者信息不存在**：学号“111111”并不在reader表中，所以违背触发器要求而不能够执行插入操作

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\没有1111.jpg" style="zoom:50%;" />

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\触发器添加（读者信息不存在）.jpg" style="zoom:50%;" />

     

   + **图书信息不存在**：书号“111111”的图书信息不在book表中，所以违背触发器要求而不能够执行插入操作

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\触发器添加违背（图书信息不存在）.jpg" style="zoom:50%;" />

   

​                         

​                              


### 六. 存储过程控制下的更新操作（18分）

1. 说明

   + （1分）简要说明该操作所要完成的功能；
   + （1分）简要说明该存储过程所要完成的功能；
   + （2分）说明该操作涉及操作的表（必须包含两张或两张以上的关系表，以“表名形式”描述）
   + （1分）表连接涉及字段描述（描述方式为“表1.属性=表2.属性”）
   + （2分）该操作会修改字段（以“表名.字段名”的形式给出），以及修改规则，如新数值的计算方法、在何种条件下予以修改等；
   + （6分）实现该操作的关键代码（高级语言、SQL），截图即可；
   + （5分）如何执行该操作，按所述方法能够正常演示程序则给分。

   

2. #### 功能描述（1分）

   更新该管理员权限下所管理图书的部分或全部信息（书名，作者， 价格）

   

3. #### 存储过程功能描述（1分）

   更新的图书范围仅限该管理员权限内，可以修改图书书名、作者、价格等信息，当更新图书价格小于0时不予更新修改

   

4. #### 涉及的关系表（2分）

   book, bookshelf

   

5. #### 表连接涉及字段（1分）

   book.No_bookshelf = bookshelf.No_bookshelf

   

6. #### 更改字段（2分）

   <table  width="200" height="120" border="1" >
       <td style="text-align:center ">  <b>更改字段</b></td> 
       <td style="text-align:center "><b>规则</b></td>
   <tr>
       <td style="text-align:center " >title(书名)</td>
   	<td style="text-align:center ">无</td>
   <tr>
   <tr>
        <td style="text-align:center " >author(作者)</td>    
        <td style="text-align:center ">无</td>     
   <tr/>
   <tr>    
        <td style="text-align:center " >price(价格)</td>    
        <td style="text-align:center ">所更新的价格需要大于0</td>    
   <tr>
   </table>

   

7. #### 更新代码（3分）

   ```mysql
   def change_all(otherFrame, new_name, old_name, new_location,old_location, new_price, old_price, num):
       new_name = new_name.get()
       new_location = new_location.get()
       new_price = new_price.get()
       try:
           cursor.execute("START TRANSACTION")
           sql1 = "update book natural join bookshelf " \
                  "set title= '" + str(new_name) + "', book.location='"+str(new_location)+"'" \
                  "where  book_number= '" + str(num) + "';"
           sql2 = "call update_price(" + str(new_price) + ", " + "" + str(old_price) + ");"
           cursor.execute(sql1)
           cursor.execute(sql2)
           messagebox.showinfo(message='更新成功！')
           db.commit()
       except Exception as m:
           messagebox.showerror('警告', m.args)
           db.rollback()
   ```

   

8. #### 创建存储过程源码（3分）

   ##### 核心代码：

   ```mysql
   drop PROCEDURE if exists update_price;
   delimiter//
   CREATE PROCEDURE update_price(in new_price float, in old_price float)
   BEGIN
   IF new_price < 0
   then
   SIGNAL SQLSTATE 'HY000' SET MESSAGE_TEXT = '更新价格不合法（小于0) ';
   else
   UPDATE book SET price = new_price where price = old_price;
   end if;
   end//
   delimiter;
   ```

   

   ##### 执行成功截图

   <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\更新图书信息触发器.jpg" style="zoom:50%;" />

   

9. #### 存储过程执行源码（1分）

   ##### 核心代码：

   ```mysql
   try:
   	cursor.execute("START TRANSACTION")
       sql1 = "update book set  title= '" + str(new_name) + "' where title = '" + str(old_name) + "';"
       sql2 = "update book set  author= '" + str(new_author) + "' where author = '" + str(old_author) + "';"
       sql3 = "call update_price(" + str(new_price) + ", " + "" + str(old_price) + ");"
       cursor.execute(sql1)
       cursor.execute(sql2)
       cursor.execute(sql3)
       messagebox.showinfo(message='更新成功！')
       db.commit()
   except Exception as m:
   	messagebox.showerror('警告', m.args)
       db.rollback()
   ```

   ##### 全部代码：

   ![](D:\聂志强\大学\大二下\数据库系统\数据库大作业\更新1.jpg)

   ![更新2](D:\聂志强\大学\大二下\数据库系统\数据库大作业\更新2.jpg)

   ![更新3](D:\聂志强\大学\大二下\数据库系统\数据库大作业\更新3.jpg)

   ![更新4](D:\聂志强\大学\大二下\数据库系统\数据库大作业\更新4.jpg)

   ![更新5](D:\聂志强\大学\大二下\数据库系统\数据库大作业\更新5.jpg)

   ![](D:\聂志强\大学\大二下\数据库系统\数据库大作业\更新6.jpg)

   ![](补充.jpg)

   ![](D:\聂志强\大学\大二下\数据库系统\数据库大作业\更新9.jpg)

   ![屏更新8](D:\聂志强\大学\大二下\数据库系统\数据库大作业\屏更新8.jpg)   

10. #### 程序演示（2分）

    + 说明：不违背存储过程，能够执行更新操作

      <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\成功更新.jpg" style="zoom:50%;" />

      <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\成功更新前.jpg" style="zoom:50%;" />

      <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\成功更新后.jpg" style="zoom:50%;" />

      

11. #### 程序演示（2分）

    + 说明：单独更新价格且小于0，违背存储过程，系统报错；观察书号为234更新前后价格并未变化

      <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\更新失败前.jpg" style="zoom:50%;" />

      <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\更新失败.jpg" style="zoom:50%;" />

      <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\更新失败前.jpg" style="zoom:50%;" />





### 七. 含有视图的查询操作（15分）

1. #### 说明

   + （1分）简要说明该操作所要完成的功能；

   + （1分）简要说明建立的该视图的功能；

   + （2分）简要说明该操作涉及的关系数据表（以“表名”的形式给出）

   + （1分）简要说明表连接涉及的字段（以“表1.属性=表2.属性”）

   + （6分）实现该操作的关键代码（高级语言、SQL），截图即可；

   + （4分）如何执行该操作，按所述方法能够正常演示程序则给分。

      

      

      

     

2. #### 操作功能描述（1分）

   <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\查询中心.jpg" style="zoom:50%;" />

   + ##### 查询借还信息

     + 输入书号，按照书号索引数据库中该图书全部借还信息

     + 输入学号，按照学号查询该读者全部借还信息

       

    ==为了使查询功能更加完善，以下三个功能为大作业额外实现，为了不使实验报告过于冗长，以下三个功能仅做简要程序演示==

   + ##### 按图书号查询图书信息

     输入书号，按照书号索引数据库中该图书全部信息

   + ##### 按书架查询图书信息

     输入书架号，可以查询该书架上所有图书的全部信息

   + ##### 查询读者信息

     输入读者学号，可以查询该读者全部信息（学号、姓名、性别、）

   

3. #### 视图功能描述（1分）

   + 合并Borrow_or_return 和 reader 表并筛选出重要属性，去除性别、欠款等非关键属性

     

4. #### 涉及的关系表（2分）

   Borrow_or_return,   reader               

   ​    

5. #### 表连接字段（1分）

   Borrow_or_return.student_number = reader.student_number

   

6. #### 创建视图代码（3分）

   ```mysql
   DROP VIEW IF EXISTS b_r;
   CREATE VIEW b_r AS
   SELECT student_number,name, book_number,borrowing
   from Borrow_or_return natural join reader;
   ```

   执行成功截图：

   <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\视图成功.jpg" style="zoom:50%;" />

   

7. #### 查询代码（3分）

   ![](D:\聂志强\大学\大二下\数据库系统\数据库大作业\查询1.jpg)

   ![查询2](D:\聂志强\大学\大二下\数据库系统\数据库大作业\查询2.jpg)

   ![查询3](D:\聂志强\大学\大二下\数据库系统\数据库大作业\查询3.jpg)

   ![查询5](D:\聂志强\大学\大二下\数据库系统\数据库大作业\查询5.jpg)

   ![查询6](D:\聂志强\大学\大二下\数据库系统\数据库大作业\查询6.jpg)

   ![查询7](D:\聂志强\大学\大二下\数据库系统\数据库大作业\查询7.jpg)

   

8. #### 程序演示（4分）

   + 按书号查询，输入书号732，可以显示该书所有借还记录，且设置滚动条，可以拖动滚动条或者鼠标查询全部借还信息

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\按书号查询.jpg" style="zoom:50%;" />

     

   + 按学号查询，输入学号“2012307"，可以查看该读者所有借还记录，且设置滚动条，可以拖动滚动条或者鼠标查询全部借还信息

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\按学号查询.jpg" style="zoom:50%;" />

   

   


   + 点击添加借还信息，可以跳转至添加借还信息页面插入借还信息

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\添加借还.jpg" style="zoom:50%;" />

     

   + ##### ==额外功能==：

     **查询图书信息**

     输入书号，即可显示该图书全部信息（书架号/位置，书号，书名，作者，价格，在馆/馆藏数量， 管理员ID）

     点击更新图书信息即可跳转至更新页面，更新图书书名、作者、价格等信息

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\查询图书.jpg" style="zoom: 33%;" />

     

     ##### 查询读者信息

     输入学号，点击 ”查询“ 可以查询该读者全部信息（学号， 姓名， 性别， 登录密码， 欠费， 可借/在借图书数量）

     点击 ”添加读者信息“ 可以插入读者至reader表中，学号、姓名、性别、密码按照输入添加，欠费、可借/在借图书数量按照初始化默认添加

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\查询读者.jpg" style="zoom: 33%;" />

     

     ##### 查询书架图书信息

     因为每个书架均由一个管理员管理，所以设置按照书架查询图书信息具有很大作用方便管理员查询，输入书架号，点击 ”查询“ 即可查询该书架全部图书信息（书架号，书号， 书名， 作者， 价格， 在馆/馆藏数量， 位置， 管理员ID）

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\查询书架.jpg" style="zoom: 33%;" />





### 八. 附加功能：登录验证及注册

#####    为了避免实验报告冗长，该部分以代码和演示为主：

1. #### 全部代码

   ```mysql
   # 个人信息注册
   def registerInfo():
       # root.withdraw()
       top = Toplevel()
       top.title('注册页面')
       top.geometry('700x500')
   
       # 加载图片
       canvas = tkinter.Canvas(top, width=700, height=500, bg=None)
       image = canvas.create_image(0, 0, anchor='nw', image=image_file_login)
       canvas.pack()
   
       def quiteInfo():
           top.withdraw()
           root.deiconify()
   
       def register():
           if id.get() == "":
               showerror(title='提示', message='输入不能为空')
           elif name.get() == "":
               showerror(title='提示', message='输入不能为空')
           elif password.get() == "":
               showerror(title='提示', message='输入不能为空')
           elif len(password.get()) < 5 :
               showerror(title='提示', message='密码不能小于5位')
           else:
               flag = 1
               sql = "INSERT INTO administrator values('" + name.get() + "', " + id.get() + ", " + password.get() + ");"
               try:
                   cursor.execute(sql)
               except Exception as m:
                   messagebox.showerror('警告', m.args)
                   flag = 0
   
               cursor.execute("select * from administrator")
               message_list = cursor.fetchall()
               for i in range(len(message_list)):
                   if int(id.get()) == message_list[i][1]:
                       showerror(title='提示', message='该身份证已经注册过')
                       flag = 0
                       break
               if flag:
                   showinfo(title='提示', message="注册成功")
                   top.withdraw()
                   root.deiconify()
                   
       def toggle_password():
           if passwd_entry.cget('show') == '':
               passwd_entry.config(show='*')
               toggle_btn.config(text='Show Password')
           else:
               passwd_entry.config(show='')
               toggle_btn.config(text='Hide Password')
       Label(top, text="ID：", font=(20,)).place(relx=0.3, rely=0.1, relwidth=0.1, height=25)
       Entry(top, textvariable=id).place(relx=0.5, rely=0.1, relwidth=0.2, height=25)
       Label(top, text="姓名：", font=(20,)).place(relx=0.3, rely=0.2, relwidth=0.1, height=25)
       Entry(top, textvariable=name).place(relx=0.5, rely=0.2, relwidth=0.2, height=25)
       Label(top, text="密码(不少于5位)：", font=(20,)).place(relx=0.22, rely=0.3, relwidth=0.26, height=25)
       passwd_entry = Entry(top, textvariable=password, show='*')
       passwd_entry.place(relx=0.5, rely=0.3, relwidth=0.2, height=25)
       toggle_btn = ttk.Button(top, text='Show Password', command=toggle_password).place(relx=0.73, rely=0.3, relwidth=0.1, height=25)
       Button(top, text="注册", command=register, font=(20,)).place(relx=0.53, rely=0.5, width=200, height=25)
       Button(top, text="返回上一页", command=quiteInfo, font=(20,)).place(relx=0.2, rely=0.5, width=200, height=25)
   
   
   # 登录界面
   def signInfo():
       root.withdraw()
       top = Toplevel()
       top.geometry('700x500')
       top.title('登录界面')
   
       # 加载图片
       canvas = tkinter.Canvas(top, width=700, height=500, bg=None)
       image = canvas.create_image(0, 0, anchor='nw', image=image_file_login)
       canvas.pack()
   
       def quiteInfo():
           top.withdraw()
           root.deiconify()
   
       def check():
           if id.get() == "":
               showerror(title='提示', message='输入不能为空')
           elif password.get() == "":
               showerror(title='提示', message='输入不能为空')
           else:
               cursor.execute("select * from administrator")
               message_list = cursor.fetchall()
               num = id.get()
               password_user = password.get()
               flag = 0
               for i in range(len(message_list)):
                   if num == message_list[i][1] and password_user == message_list[i][2]:
                       flag = 1
                       # user = message_list[i][0]
                       break
               # if flag == 1:
               if flag:
                   showinfo(title='提示', message="登录成功")
                   top.withdraw()
                   main_choose(num)
               else:
                   showerror(title='提示', message='ID或密码有错，登录失败')
   
       Label(top, text="ID：", font=('楷体',20,)).place(relx=0.32, rely=0.2, relwidth=0.13, height=30)
       Label(top, text="密码：", font=('楷体',20)).place(relx=0.32, rely=0.3, relwidth=0.13, height=30)
       Entry(top, textvariable=id,font=('楷体',20)).place(relx=0.5, rely=0.2, relwidth=0.15, height=30)
       Entry(top, textvariable=password,font=('楷体',20)).place(relx=0.5, rely=0.3, relwidth=0.15, height=30)
       Button(top, text="登录", command=check, font=('楷体',20)).place(relx=0.35, rely=0.5, width=200, height=30)
       Button(top, text="返回上一页", command=quiteInfo, font=('楷体',20)).place(relx=0.35, rely=0.6, width=200, height=30)
   ```

   

2. #### 进入登录/注册选择页面

   <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\第一个页面.jpg" style="zoom: 33%;" />

   ​          

   

3. #### 登录功能

   + 点击 ”登录“ 摁扭，进入登录页面

   + 输入ID和密码，会自动从administrator表中匹配对应管理员信息，若该管理员信息已存在，则**登录成功**，若输入的ID或密码不匹配或不在administrator表中则会**引发异常**

   <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\登录数据库.jpg" style="zoom:67%;" />

   

   <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\登录成功.jpg" style="zoom: 33%;" />

   

   <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\登录失败.jpg" alt="登录失败" style="zoom: 33%;" />

   

4. #### 注册功能

   + 点击 ”个人信息注册“ 摁扭

   + 输入ID，姓名，密码（**可设置外显或隐藏**） ，点击 ”注册“ 摁扭，即可成功完成注册，观察administrator表中 出现了刚才注册的管理员信息

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\注册（不展示密码）.jpg" style="zoom: 33%;" />

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\注册（展示密码）.jpg" alt="注册（展示密码）" style="zoom: 33%;" />

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\注册数据库.jpg" style="zoom:67%;" />

   + ##### 注册失败1： ID，姓名，密码任何一个信息为空均会引发异常，注册失败

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\注册失败.bmp" style="zoom: 33%;" />

     

   + ##### 注册失败2：输入密码小于5位会引发异常，注册失败

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\注册失败2.jpg" style="zoom: 33%;" />

     

   + ##### 注册失败3：注册重复的ID号，会违背主键约束引发异常，注册失败

     <img src="D:\聂志强\大学\大二下\数据库系统\数据库大作业\注册失败3.jpg" style="zoom: 33%;" />






### 九. 服务器部署

1. #### 服务器端

   ```mysql
   service = {
       'registerInfo': "1",
       'signInfo': "2",
       'search_reader': "3",
       'choose_reader': "4",
       'new_reader': "5",
       'find_book': "6",
       'find_number': "7",
       'find_name': "8",
       's_bookshelf': "9",
       'f3': "10",
       'change': "11",
       'change_choose': "12",
       'change_all': "13",
       'change_name': "14",
       'change_location': "15",
       'change_price': "16",
       'delete': "17",
       'f4': "18",
       'f6': "19",
   }
   
   def handle(client):
       # 拿2048字节
       message_recv = client.recv(2048).decode()
       lst = message_recv.split('&&&')
       dic = {}
       for item in lst:
           dic[item.split('=')[0]] = item.split('=')[1]
   
       if dic['service'] == service['registerInfo']:
           res(client, dic)
       elif dic['service'] == service['signInfo']:
           sig(client, dic)
       elif dic['service'] == service['search_reader']:
           s_r(client, dic)
       elif dic['service'] == service['choose_reader']:
           c_r(client, dic)
       elif dic['service'] == service['new_reader']:
           n_r(client, dic)
       elif dic['service'] == service['find_book']:
           f_b(client, dic)
       elif dic['service'] == service['find_number']:
           f_number(client, dic)
       elif dic['service'] == service['find_name']:
           f_name(client, dic)
       elif dic['service'] == service['s_bookshelf']:
           s_b(client, dic)
       elif dic['service'] == service['f3']:
           f3(client, dic)
       elif dic['service'] == service['change']:
           change(client, dic)
       elif dic['service'] == service['change_choose']:
           c_c(client, dic)
       elif dic['service'] == service['change_all']:
           change_all(client, dic)
       elif dic['service'] == service['change_name']:
           change_name(client, dic)
       elif dic['service'] == service['change_location']:
           change_location(client, dic)
       elif dic['service'] == service['change_price']:
           change_price(client, dic)
       elif dic['service'] == service['delete']:
           delete(client, dic)
       elif dic['service'] == service['f4']:
           f4(client, dic)
       elif dic['service'] == service['f6']:
           f6(client, dic)
   
   if __name__ == '__main__':
       serverPort = 8401
       serverSocket = socket(AF_INET, SOCK_STREAM)
       serverSocket.bind(('', serverPort))
       serverSocket.listen(1)
       print("服务器开始服务")
       while True:
           # 建立连接，监听8401端口
           client, address = serverSocket.accept()
           handle2 = lambda: handle(client)
           # 开启新线程
           threading.Thread(target=handle2).start()
   ```

   

2. #### 客户端

   ```python
   # 向服务器发送请求
   def connect(string):
       # 服务器IP
       serverName = "114.116.89.58"
       # 服务器端口
       serverPort = 8401
       client = socket(AF_INET, SOCK_STREAM)
       # 与服务器建立连接并发送数据参数
       client.connect((serverName, serverPort))
       client.send(string.encode())
       # 接受服务器回传数据
       receive = client.recv(2048).decode()
       # 断开连接
       client.close()
       return receive
   ```

    

3. ###  docerfile

   ```mysql
   # 将官方 Python 运行时用作父镜像
   FROM python:server
   # 定义变量
   ENV DIR_WEBAPP /usr/local/Server/
   # 将工作目录设置为
   WORKDIR $DIR_WEBAPP
   # 将当前目录内容复制容器中
   ADD ./server.py server.py
   #ADD ./requirements.txt requirements.txt
   # 暴露接口
   EXPOSE 8401
   # 安装 requirements.txt 中指定的任何所需软件包
   #RUN #pip install -r requirements.txt
   # 在容器启动时运行 tset.py
   CMD ["python", "./server.py"]
   ```

   

### 九. 总结

1. 非常感谢龙老师及各位助教学长学姐的指导帮助，这次实验虽然耗时一个月，但真的对数据库、前端、后端以及前后端通信有了理论及实践两方面掌握
2. ==该数据库已经部署到服务器上==
3. 前后端代码一共**1000+行，全部原创**
4. 除了实现大作业要求的4个功能外，额外又实现5个功能，已经在上述大作业报告中体现
5. 该图书管理系统一开始的设计理念是将权限与数据库应用相结合并且部署到服务器上，基于登录获取管理员信息，在**该管理员所管权限下**如上9个功能的操作。
6. 为了增加数据库安全性，所有功能实现均包含异常处理及事务操作。
