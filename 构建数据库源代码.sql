/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2022-05-01 15:13:06                          */
/*==============================================================*/

create database library;
use library;
drop table if exists Borrow_or_return;

drop table if exists Comment_section;

drop table if exists administrator;

drop table if exists book;

drop table if exists bookshelf;

drop table if exists reader;

/*==============================================================*/
/* Table: reader                                                */
/*==============================================================*/
create table reader
(
   student_number       char(20) not null,
   name                 char(20),
   gender               char(2),
   password             char(20),
   owe_money            float,
   Number_of_books_available int,
   Number_of_borrowed_books int,
   primary key (student_number)
);




/*==============================================================*/
/* Table: administrator                                         */
/*==============================================================*/
create table administrator
(
   name                 char(20),
   ID                   char(20) not null,
   password             char(20),
   primary key (ID)
);




/*==============================================================*/
/* Table: bookshelf                                             */
/*==============================================================*/
create table bookshelf
(
   location             char(30) not null,
   No_bookshelf         char(30) ,
   ID                   char(20) not null,
   primary key (location),
   constraint FK_manage foreign key (ID)
      references administrator (ID) on update cascade on delete cascade
);





/*==============================================================*/
/* Table: book                                                  */
/*==============================================================*/
create table book
(
   book_number          char(20) not null,
   location         char(10),
   title                char(40),
   author               char(20),
   price                float,
   Number_of_books_in_the_library int,
   Number_of_collections int,
   primary key (book_number),
   constraint FK_deposit foreign key (location)
      references bookshelf (location) on update cascade on delete cascade
);


/*==============================================================*/
/* Table: Borrow_or_return                                      */
/*==============================================================*/
drop table if exists Borrow_or_return;
create table Borrow_or_return
(
   student_number       char(20) not null,
   book_number          char(20) not null,
   borrowing            date not null,
   primary key (student_number, book_number, borrowing),
   constraint FK_Borrow_or_return foreign key (student_number)
      references reader (student_number) on update cascade on delete cascade,
   constraint FK_Borrow_or_return2 foreign key (book_number)
      references book (book_number) on update cascade on delete cascade
);



/*==============================================================*/
/* Table: Comment_section                                       */
/*==============================================================*/
create table Comment_section
(
   Time                 datetime not null,
   Comment_content      char(50) not null,
   student_number       char(20) not null,
   ID                   char(20) not null,
   Reply_content        char(50),
   primary key (Comment_content, Time),
   constraint FK_add foreign key (student_number)
      references reader (student_number) on update cascade on delete cascade,
   constraint FK_reply foreign key (ID)
      references administrator (ID) on update cascade on delete cascade
);


DROP  VIEW  IF  EXISTS  b_r;
CREATE VIEW b_r AS
SELECT student_number,name, book_number,borrowing
from Borrow_or_return natural join reader;


drop trigger if exists add_record;
CREATE trigger add_record
BEFORE INSERT ON borrow_or_return FOR EACH ROW
BEGIN
	IF new.student_number not in (select student_number from reader)
	THEN
		SIGNAL SQLSTATE '22004' SET MESSAGE_TEXT = '该读者信息不存在';
	END IF;

    	IF new.book_number not in (select book_number from book)
	THEN
		SIGNAL SQLSTATE '22005' SET MESSAGE_TEXT = '该图书信息不存在';
	END IF;
END;


drop PROCEDURE if exists update_price;
CREATE PROCEDURE update_price(in new_price float, in old_price float)
BEGIN
IF new_price < 0
then
SIGNAL SQLSTATE 'HY000' SET MESSAGE_TEXT = '更新价格不合法（小于0) ';
else
UPDATE book SET price = new_price where price = old_price;
end if;
end;


DROP  VIEW  IF  EXISTS  b_r;
CREATE VIEW b_r AS
SELECT student_number,name, book_number,borrowing
from Borrow_or_return natural join reader;


delete from reader;
INSERT INTO reader VALUES('2012307', '张三',  '男' , '111111', 3.5, 8, 4) ;
INSERT INTO reader VALUES('2012112', '李四', '女' ,  '123456', 0, 10, 2);
INSERT INTO reader VALUES('2011708', '王五', '男' ,  '234512', 12, 0, 0);
INSERT INTO reader VALUES('2012207', '张观博',  '男' , '456543', 3.5, 8, 4) ;
INSERT INTO reader VALUES('2011212', '张欣竹', '女' ,  '876567', 0, 10, 2);
INSERT INTO reader VALUES('2015608', '梁浩轩', '男' ,  '098789', 12, 0, 0);


delete from administrator;
INSERT INTO administrator VALUES('曾华','101','95033');
INSERT INTO administrator VALUES('匡明','102','94037');
INSERT INTO administrator VALUES('王丽','103','98435');
INSERT INTO administrator VALUES('李军','104','12883');

delete from bookshelf;
INSERT INTO bookshelf VALUES('A01',  '1' ,  '101');
INSERT INTO bookshelf VALUES('A02',  '1' ,  '101');
INSERT INTO bookshelf VALUES('A03',  '1' ,  '101');
INSERT INTO bookshelf VALUES('A04',  '1' ,  '101');
INSERT INTO bookshelf VALUES('A05',  '1' ,  '101');
INSERT INTO bookshelf VALUES('A06',  '1' ,  '101');
INSERT INTO bookshelf VALUES('B01',  '1' ,  '101');
INSERT INTO bookshelf VALUES('B02',  '1' ,  '101');
INSERT INTO bookshelf VALUES('B03',  '1' ,  '101');
INSERT INTO bookshelf VALUES('B04',  '1' ,  '101');
INSERT INTO bookshelf VALUES('B05',  '1' ,  '101');
INSERT INTO bookshelf VALUES('B06',  '1' ,  '101');
INSERT INTO bookshelf VALUES('D02',  '2' ,  '101');
INSERT INTO bookshelf VALUES('F01',  '1' ,  '101');
INSERT INTO bookshelf VALUES('F02',  '4' ,  '104');

delete from book;
INSERT INTO book VALUES('732','A01','python','陈晨',65.6,2,5);
INSERT INTO book VALUES('856','A02','数据库','龙老师',23.5,1,4);
INSERT INTO book VALUES('825','B02','软件安全','刘哲理',78,0,3);
INSERT INTO book VALUES('633','D02','JAVA','刘嘉欣',88,5,5);
INSERT INTO book VALUES('831','A03','算法导论','苏明',34.6,0,2);
INSERT INTO book VALUES('153','B01','汇编程序设计','王志',65.6,2,5);
INSERT INTO book VALUES('632','A04','密码学','汪定',65.6,2,5);
INSERT INTO book VALUES('921','F02','文字之美','徐帆',34.6,1,5);

delete from Borrow_or_return;
INSERT INTO Borrow_or_return VALUES('2012307',  '856' ,  '2021.12.03');
INSERT INTO Borrow_or_return VALUES('2012307',  '732' ,  '2022.02.03');
INSERT INTO Borrow_or_return VALUES('2012307',  '856' ,  '2022.04.05');




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

