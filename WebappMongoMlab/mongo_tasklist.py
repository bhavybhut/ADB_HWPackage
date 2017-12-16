from pymongo import MongoClient

MONGO_HOST = "ds135876.mlab.com"
MONGO_PORT = 35876
MONGO_DB = "todo"
MONGO_USER = "bhavy"
MONGO_PASS = "bhavy"

class TaskList():

    db = None

    def __init__(self):
        self.client = MongoClient()
        connection = MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = connection[MONGO_DB]
        self.db.authenticate(MONGO_USER, MONGO_PASS)
        # self.db.todo.delete_many({})
        # for i in range(0,8):
        #     self.db.todo.insert_one(
        #         { 
        #             "id":i,
        #             "task":"Do something", 
        #             "status":i%2
        #         }
        #     )

    def get_task_list(self, status=None):
        if status==None:
            where = {}
        else:
            where = {"status":status}
        items = self.db.todo.find(where,{
                            "_id":False,
                            "id":True,
                            "task":True,
                            "status":True,
                            })
        items = list(items)
        return items

    def search_task(self, task=None, status=None):
        if task==None:
            where = {}
        elif status==None:
            where = {}
        else:
            where = {"task":task ,"status":status}
        items = self.db.todo.find(where,{
                            "_id":False,
                            "id":True,
                            "task":True,
                            "status":True,
                            })
        items = list(items)
        return items

    def get_task(self, id):
        items = self.db.todo.find({"id" : id}, {
                            "_id":False,
                            "id":True,
                            "task":True,
                            "status":True,
                            })
        items = list(items)
        if len(items) == 0:
            return None
        return items[0]
    
    def new_task(self, task, status):
        id = -1
        items = self.db.todo.find({},{
                            "_id":False,
                            "id":True,
                            })
        for item in items:
            if item["id"] > id:
                id = item["id"]
        self.db.todo.insert_one(
               { 
                    "id":id+1,
                    "task":task, 
                    "status":status
                })

    def update_task(self, id, task, status):
        self.db.todo.update_one({"id":id},{"$set":{"task":task, "status":status}})

    def delete_task(self, id):
        self.db.todo.delete_one({"id":id})