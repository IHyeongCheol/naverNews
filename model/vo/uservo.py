# userdb table
# id(str), pwd(str), name(str)

class UserVO:
    def __init__(self,id,pwd,name):
        self.id = id;
        self.pwd = pwd;
        self.name = name;

    def getId(self):
        return self.id;
    def getPwd(self):
        return self.pwd;
    def getName(self):
        return self.name;
    def setId(self,id):
        self.id = id;
    def setPwd(self,pwd):
        self.pwd = pwd;
    def setName(self,name):
        self.name = name;

    def __str__(self):
        return '%s %s %s' % (self.id,self.pwd,self.name);