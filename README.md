### 系统环境
- 操作系统：Windows 10
- 数据库系统：SQL Server 2017

### 基本功能
- 读者管理

    读者管理即借书证管理，包括的业务（即用例）有：办理借书证、借书证变更、借书证挂失、解除挂失、补办借书证、注销借书证等。

    借书证（读者）可分为2种类别：教师、学生。

    借书证（教师）=借书证号、姓名、性别、所在单位、办证日期、照片等。

    借书证（学生）=借书证号、学号、姓名、性别、专业、班级、办证日期、有效期、照片等。其中，有效期由学生类别决定，本科生4年、专科生3年、硕士生3年等。

    相关业务规则：(1)读者凭借书证借书；(2)教师最多借书12本，借书期限最长为60天，可续借2次；学生最多借书8本，借书期限最长为30天，可续借1次；(3)处于挂失、注销状态的读者不能借书；(4)未归还图书者不能注销其借书证。

- 图书管理

    包括业务（用例）：图书编目、新书入库、图书信息维护、图书变卖与销毁处理等。

    图书信息=书号、书名、作者、出版社、出版日期、ISBN、分类号、语言、页数、单价、内容简介、图书封面、图书状态等；（图书状态包括：在馆、借出、遗失、变卖、销毁）

- 借阅管理

    包括业务用例：借书、续借、还书等。还书过程涉及超期罚款、遗失图书罚款等业务规则。

    罚款规则：（1）超期罚款规则 应罚款金额=超期天数*罚款率，罚款率=0.05元/天，罚款率可能随时间或读者类别而变化；实际罚款金额<=应罚款金额，根据实际情况可以进行减免。（2）遗失罚款规则 遗失图书应罚款金额=3*图书单价；实际罚款金额在（1*图书单价，3*图书单价）之间。（3）遗失罚款规则优先于超期罚款规则。

    借书记录=借书证号、书号、借书操作员、借书日期、应还日期

    续借记录=借书证号、书号、续借操作员、续借日期、应还日期，续借次数

    还书记录=借书证号、书号、还书操作员、还书日期、应还日期，超期天数、应罚款金额，实际罚款金额

    借阅信息=借书顺序号、借书证号、书号、借书操作员、借书日期、应还日期，续借次数、还书操作员、还书日期，超期天数、应罚款金额，实际罚款金额

- 用户登陆与用户管理

    包括用例：用户登录、密码修改、用户管理*，为本系统的基础和主要功能。

    用户包括2类：读者、管理员。其中，管理员用户权限是4种角色的组合：借书证管理、图书管理、借阅管理、系统管理；系统管理员负责所有管理员用户及其权限的管理，借书证管理员负责读者管理（即借书证管理）。

    管理员是读者，但读者不一定是管理员；读者与管理员间存在(1对0..1)联系。
    读者信息+=密码。

    管理员信息=用户号、用户名、密码、管理角色

    管理角色设计：可采用4位二进制，借书证管理(0001)2=1、图书管理(0010)2=2、借阅管理(0100)2=4、系统管理(1000)2=8。如表示图书管理和借阅管理权限：2+4=6；判断7是否具备图书管理权限：7位与2，即(0111)2位与(0010)2=(0010)2，表示有此权限。

- 读者查询

    读者（非管理员用户）的功能需求，包括用例：未归还图书查询与续借（含超期、即将到期查询操作）、在馆图书查询操作等。


### 数据库设置
- 内容：

    1. 创建数据库：Library；
    2. 创建登录名：LibAdmin，密码：123；并设置为数据库Library的dbo；
    3. 创建上述4张数据表及约束；
    4. 创建借书还书存储过程；

- 源码：
```
-创建数据库用户并赋予权限
CREATE LOGIN LibAdmin WITH PASSWORD = '123', DEFAULT_DATABASE = Library;

CREATE USER LibAdmin FOR LOGIN LibAdmin WITH DEFAULT_SCHEMA = dbo;

EXEC sp_addrolemember 'db_owner', 'LibAdmin';
--创建表
BEGIN TRAN;
CREATE TABLE TB_ReaderType
(
    rdType SMALLINT
        CONSTRAINT pk_ReaderType_rdType PRIMARY KEY,
    rdTypeName NVARCHAR(20) NOT NULL
        CONSTRAINT uk_rtrtn
        UNIQUE,
    CanLendQty INT,
    CanLendDay INT,
    CanContinueTimes INT,
    PunishRate FLOAT,
    DateValid SMALLINT NOT NULL
);

CREATE TABLE TB_Reader
(
    rdID INT
        CONSTRAINT pk_Reader_rdID PRIMARY KEY,
    rdName NVARCHAR(20),
    rdSex NCHAR(1),
    rdType SMALLINT NOT NULL
        CONSTRAINT fk_Reader_rdType
        FOREIGN KEY REFERENCES TB_ReaderType (rdType),
    rdDept NVARCHAR(20),
    rdPhone NVARCHAR(25),
    rdEmail NVARCHAR(25),
    rdDateReg DATETIME,
    rdPhoto IMAGE,
    rdStatus NCHAR(2),
    rdBorrowQty INT
        DEFAULT 0,
    rdPwd NVARCHAR(20)
        DEFAULT 123,
    rdAdminRoles SMALLINT
);

CREATE TABLE TB_Book
(
    bkID INT
        CONSTRAINT pk_Book_bkID PRIMARY KEY,
    bkCode NVARCHAR(20),
    bkName NVARCHAR(50),
    bkAuthor NVARCHAR(30),
    bkPress NVARCHAR(50),
    bkDatePress DATETIME,
    bkISBN NVARCHAR(15),
    bkLanguage SMALLINT,
    bkPages INT,
    bkPrice MONEY,
    bkDateLn DATETIME,
    bkBrief TEXT,
    bkCover IMAGE,
    bkStatus NCHAR(2)
);

CREATE TABLE TB_Borrow
(
    BorrowID NUMERIC(12, 0)
        CONSTRAINT pk_Borrow_BorrowID PRIMARY KEY,
    rdID INT
        CONSTRAINT fk_Borrow_rdID
        FOREIGN KEY REFERENCES TB_Reader (rdID),
    bkID INT
        CONSTRAINT fk_Borrow_bkID
        FOREIGN KEY REFERENCES TB_Book (bkID),
    ldContinueTimes INT,
    ldDateOut DATETIME,
    ldDateRetPlan DATETIME,
    ldDateRetAct DATETIME,
    ldOverDay INT,
    ldOverMoney MONEY,
    ldPunishMoney MONEY,
    lsHasReturn BIT
        DEFAULT 0,
    OperatorLend NVARCHAR(20),
    OperatorRet NVARCHAR(20)
);

IF @@ERROR = 0
BEGIN
    PRINT 'Success';
    COMMIT;
END;
ELSE
BEGIN
    PRINT 'Fail';
    ROLLBACK;
END;

--

--借书
GO
CREATE PROCEDURE BorrowBook
    @BorrowID NUMERIC(12, 0),
    @rdID CHAR(9),
    @bkID CHAR(9),
    @OperatorLend NVARCHAR(20)
AS
--声明（判断Book表中有没有这本书）的变量
DECLARE @bkStatus NCHAR(2);
SELECT @bkStatus = bkStatus
FROM TB_Book
WHERE bkID = @bkID;
--声明关于（判断可借书数量是否超出）的变量
DECLARE @rdBorrowQty INT,
        @canLendQty INT;
SELECT @rdBorrowQty = rdBorrowQty
FROM TB_Reader
WHERE rdID = @rdID;
SELECT @canLendQty = CanLendQty
FROM TB_ReaderType
WHERE rdType IN
      (
          SELECT rdType FROM TB_Reader WHERE rdID = @rdID
      );
--声明（提示有书未归还）的变量
DECLARE @lsHasReturn DATETIME;
SELECT @lsHasReturn = lsHasReturn
FROM TB_Borrow
WHERE @rdID = rdID
      AND @lsHasReturn = 0;

--------------------开始事务执行----------------------
BEGIN TRAN;
BEGIN TRY
    -----------------------------------------------------------------------
    IF NOT EXISTS (SELECT * FROM TB_Book WHERE @bkID = bkID)
    BEGIN
        RAISERROR('没有这本书', 16, 1);
    END;
    ELSE IF NOT EXISTS (SELECT * FROM TB_Reader WHERE @rdID = rdID)
    BEGIN
        RAISERROR('无此用户', 16, 1);
    END;
    ELSE IF @bkStatus <> '在馆'
    BEGIN
        RAISERROR('该图书不在馆', 16, 1);
    END;
    ELSE IF @rdBorrowQty = @canLendQty
    BEGIN
        RAISERROR('超过可借书数量', 16, 1);
    END;
    ELSE IF @lsHasReturn <> 1
    BEGIN
        RAISERROR('你有未归还的图书', 16, 1);
    END;
    -------开始借书-----------------------
    --更新借书状态
    UPDATE TB_Book
    SET bkStatus = '借出'
    WHERE bkID = @bkID;

    --更新借书数量
    UPDATE TB_Reader
    SET rdBorrowQty = rdBorrowQty + 1
    WHERE rdID = @rdID;

    --向Borrow表插入数据
    DECLARE @canLendDay INT;
    SELECT @canLendDay = CanLendDay
    FROM TB_ReaderType
    WHERE rdType IN
          (
              SELECT rdType FROM TB_Reader WHERE rdID = @rdID
          );
    INSERT INTO TB_Borrow
    VALUES
    (@BorrowID, @rdID, @bkID, 0, GETDATE(), DATEADD(dd, @canLendDay, GETDATE()), NULL, 0, 0, 0, 0, @OperatorLend, NULL);
    COMMIT;
----------------------------------------------------------------------
END TRY
BEGIN CATCH
    DECLARE @error_message VARCHAR(1000);
    SET @error_message = ERROR_MESSAGE();
    RAISERROR(@error_message, 16, 1);
    ROLLBACK;
END CATCH;

--
--还书
GO

CREATE PROCEDURE ReturnBook
    @rdID CHAR(9),
    @bkID CHAR(9),
    @OperatorLend NVARCHAR(20)
    --@ECHO NVARCHAR(20) OUTPUT
AS
DECLARE @lsHasReturn BIT
SELECT @lsHasReturn = lsHasReturn
FROM TB_Borrow
WHERE rdID = @rdID AND bkID = @bkID
--DECLARE @ECHO NVARCHAR(20)
--------------------开始事务执行----------------------
BEGIN TRAN;
BEGIN TRY
    -----------------------------------------------------------------------
    IF NOT EXISTS (SELECT * FROM TB_Book WHERE @bkID = bkID)
    BEGIN
        RAISERROR('没有这本书！', 16, 1);
    END;
    ELSE IF NOT EXISTS (SELECT * FROM TB_Reader WHERE @rdID = rdID)
    BEGIN
        RAISERROR('无此用户！', 16, 1);
    END;
    ELSE IF EXISTS (SELECT * FROM TB_Borrow WHERE @rdID = rdID) AND NOT EXISTS (SELECT * FROM TB_Borrow WHERE @bkID = bkID)
    BEGIN
        RAISERROR('此用户没有借这本书！', 16, 1);
    END;
    ELSE IF NOT EXISTS (SELECT * FROM TB_Borrow WHERE @rdID = rdID) AND EXISTS (SELECT * FROM TB_Borrow WHERE @bkID = bkID)
    BEGIN
        RAISERROR('此用户没有借这本书！', 16, 1);
    END;
    ELSE IF EXISTS (SELECT * FROM TB_Borrow WHERE @rdID = rdID) AND EXISTS (SELECT * FROM TB_Borrow WHERE @bkID = bkID) AND @lsHasReturn = 1
    BEGIN
        --SELECT @ECHO = '此用户的此书已还'
        RAISERROR('此用户的这本书已经归还！', 16, 1);
    END;
    -------开始还书-----------------------
    --更新借书状态
    UPDATE TB_Book
    SET bkStatus = '在馆'
    WHERE bkID = @bkID;

    --更新借书数量
    UPDATE TB_Reader
    SET rdBorrowQty = rdBorrowQty - 1
    WHERE rdID = @rdID;

    DECLARE @ldDateRetAct DATETIME,
            @PunishRate FLOAT;
    SELECT @ldDateRetAct = ldDateRetAct
    FROM TB_Borrow
    WHERE bkID = @bkID;
    SELECT @PunishRate = PunishRate
    FROM TB_ReaderType
    WHERE rdType IN
          (
              SELECT rdType FROM TB_Reader WHERE rdID = @rdID
          );
    --更新Borrow表数据
    IF  DATEDIFF(dd, GETDATE(), @ldDateRetAct) > 0
    BEGIN
        UPDATE TB_Borrow
        SET ldDateRetAct = GETDATE(),
            lsHasReturn = 1,
            OperatorRet = @OperatorLend
        WHERE bkID = @bkID;
    END;
    ELSE
    BEGIN
        UPDATE TB_Borrow
        SET ldDateRetAct = GETDATE(),
            ldOverDay = DATEDIFF(dd, GETDATE(), @ldDateRetAct),
            ldOverMoney = DATEDIFF(dd, GETDATE(), @ldDateRetAct) * @PunishRate,
            lsHasReturn = 1,
            OperatorRet = @OperatorLend
        WHERE bkID = @bkID;
    END;
    COMMIT;
----------------------------------------------------------------------
END TRY
BEGIN CATCH
    DECLARE @error_message VARCHAR(1000);
    SET @error_message = ERROR_MESSAGE();
    RAISERROR(@error_message, 16, 1);
    ROLLBACK;
END CATCH;

GO
```

### 界面
- 用户登录

[![Qaq4xJ.png](https://s2.ax1x.com/2019/12/08/Qaq4xJ.png)](https://imgse.com/i/Qaq4xJ)

- 主界面

[![Qaqh24.png](https://s2.ax1x.com/2019/12/08/Qaqh24.png)](https://imgse.com/i/Qaqh24)

[![QaqfGF.png](https://s2.ax1x.com/2019/12/08/QaqfGF.png)](https://imgse.com/i/QaqfGF)

- 添加

[![QaqWPU.png](https://s2.ax1x.com/2019/12/08/QaqWPU.png)](https://imgse.com/i/QaqWPU)

- 删除

[![Qaq25T.png](https://s2.ax1x.com/2019/12/08/Qaq25T.png)](https://imgse.com/i/Qaq25T)

- 查询

[![QaqIM9.png](https://s2.ax1x.com/2019/12/08/QaqIM9.png)](https://imgse.com/i/QaqIM9)

- 借书

[![QaqorR.png](https://s2.ax1x.com/2019/12/08/QaqorR.png)](https://imgse.com/i/QaqorR)

- 还书

[![QaqHVx.png](https://s2.ax1x.com/2019/12/08/QaqHVx.png)](https://imgse.com/i/QaqHVx)

- 修改密码

[![QaqqIK.png](https://s2.ax1x.com/2019/12/08/QaqqIK.png)](https://imgse.com/i/QaqqIK)
