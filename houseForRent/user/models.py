from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from utils.functions import db

class BaseModel(object):
    # 定义基础的模型
    create_time = db.Column(db.DATETIME,default=datetime.now()) # 创建时间
    update_time = db.Column(db.DATETIME,default=datetime.now(),
                            onupdate=datetime.now())

    def add_update(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class User(BaseModel,db.Model):
    __tablename__ = "ihome_user"
    id = db.Column(db.INTEGER,primary_key=True)
    phone = db.Column(db.String(11),unique=True)
    pwd_hash = db.Column(db.String(200)) # 密码
    name = db.Column(db.String(30),unique=True)
    avatar = db.Column(db.String(100)) # 头像
    id_name = db.Column(db.String(30)) # 实名认证的姓名
    id_card = db.Column(db.String(18),unique=True)

    # houses = db.relationship('House',backref="user")
    # orders = db.relationship('Order',backref="user")

    @property
    def password(self):
        return ''

    @password.setter
    def password(self,pwd):  # 设置密码
        self.pwd_hash = generate_password_hash(pwd) # 对密码进行加密

    # 校验密码
    def check_pwd(self,pwd):
        return check_password_hash(self.pwd_hash,pwd)

    def to_basic_dict(self):  # 将当前的self对象序列化
        return {
            'id':self.id,
            'avatar':self.avatar if self.avatar else '',
            'name':self.name,
            'phone':self.phone,
        }