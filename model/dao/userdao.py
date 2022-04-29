# userdb table
# data access object
from css.errorcode import ErrorCode
from model.dao.sqlitedao import SqliteDao
from model.sql.sql import Sql
from model.vo.uservo import UserVO


class UserDAO(SqliteDao):

    def __init__(self,dbNAme):
        super().__init__(dbNAme);

    def insert(self,u):
        try:
            conn = self.getConn();
            conn['cursor'].execute(Sql.insert_userdb,(u.getId(),u.getPwd(),u.getName()));
            conn['con'].commit();
        except:
            raise Exception;
        finally:
            self.close(conn);
        print('Insert Completed: %s' % u);

    def delete(self, id):
        try:
            conn = self.getConn();
            conn['cursor'].execute(Sql.delete_userdb,(id,));
            conn['con'].commit();
        except:
            raise Exception;
        finally:
            self.close(conn);
        print('%s 삭제 되었습니다.' % id);

    def update(self, u):
        try:
            conn = self.getConn();
            conn['cursor'].execute(Sql.update_userdb,(u.getPwd(),u.getName(),u.getId()));
            conn['con'].commit();
        except:
            raise Exception;
        finally:
            self.close(conn);
        print('%s 수정 되었습니다.' % u.getId());

    def select(self,id):
        print(id);
        uservo = None;
        conn = self.getConn();
        conn['cursor'].execute(Sql.select_userdb,(id,));
        rs = conn['cursor'].fetchone();
        uservo = UserVO(rs[0], rs[1], rs[2]);
        print(uservo.getId(), uservo.getPwd());
        self.close(conn);
        return uservo;

    def selectall(self):
        users = [];
        conn = self.getConn();
        conn['cursor'].execute(Sql.selectall_userdb);
        all = conn['cursor'].fetchall();
        for u in all:
            rs = UserVO(u[0],u[1],u[2]);
            users.append(rs);
        self.close(conn);
        return users;



if __name__ == '__main__':
    print('start test');

    sqlitedao = SqliteDao('shop');
    sqlitedao.makeTable();
    userdao = UserDAO('shop');

    # Insert Test
    # user1 = UserVO('id15','pwd15','정말숙');
    # try:
    #     userdao.insert(user1);
    #     print('OK');
    # except:
    #     print(ErrorCode.E0001);
    # Delete Test
    # try:
    #     userdao.delete('id13');
    #     print('OK');
    # except:
    #     print(ErrorCode.E0001);
    # Update Test
    user2 = UserVO('id19', 'pwd44', 'kim44');
    userdao.update(user2);
    #
    # # Select
    user3 = userdao.select('id99');
    print(user3);

    # Select All
    result = userdao.selectall();
    for u in result:
       print(u);


    print('end test');