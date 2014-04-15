import pymongo
con = pymongo.Connection('127.0.0.1',27017)
db = con.mydb

db.add_user('root','root')
db.authenticate('root','root')

user = db.user
user.drop()
user.save({'id':1,'name':'pymongo'})
user.save({'id':2,'name':'python'})

datas = user.find()
for data in datas:
    print data

data = user.find_one()


