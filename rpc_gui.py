from tkinter import *
from xmlrpc.client import ServerProxy
from datetime import datetime
import os
import json


class Rpc_Gui(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("odoo RPC")
        self.host_input = Entry(self.root,width=30)
        self.user_input = Entry(self.root,width=30)
        self.passwd_input = Entry(self.root,width=30)
        self.db_input = Entry(self.root,width=30)
        self.model_name_input = Entry(self.root,width=30)
        self.fields_input = Entry(self.root,width=30)
        self.display_info = Listbox(self.root,width=50)
        self.count_info = Text(self.root,height=2,width=10)
        self.result_button = Button(self.root,command=self.connect_search,text="search_read")
        self.clear_button = Button(self.root,command=self.list_box_clear,text="clear")
        self.save_button = Button(self.root,command=self.write_to_file,text="save_to_file")


    def gui_arrang(self):
        L1=Label(self.root,text="地址")
        L2=Label(self.root,text="用户名")
        L3=Label(self.root,text="密码")
        L4=Label(self.root,text="数据库名称")
        L1.pack()
        self.host_input.pack()
        L2.pack()
        self.user_input.pack()
        L3.pack()
        self.passwd_input.pack()
        L4.pack()
        self.db_input.pack()
        Label(self.root,text="模型名称").pack()
        self.model_name_input.pack()
        Label(self.root,text="字段名称").pack()
        self.fields_input.pack()
        Label(self.root,text="数量总计").pack()
        self.count_info.pack()
        Label(self.root,text="回显信息").pack()
        self.display_info.pack()
        self.result_button.pack()
        self.clear_button.pack()
        self.save_button.pack()

    def connect(self):
        HOST = self.host_input.get()
        USER = self.user_input.get()
        PASSWD = self.passwd_input.get()
        DB = self.db_input.get()
        SERVER = ServerProxy('{}/xmlrpc/2/common'.format(HOST))
        UID = SERVER.login(DB,USER,PASSWD)
        MODELS = ServerProxy('{}/xmlrpc/2/object'.format(HOST))
        return MODELS,DB,UID,PASSWD


    def connect_search(self):
        MODELS,DB,UID,PASSWD = self.connect()
        MODEL_NAME = self.model_name_input.get()
        FIELDS = self.fields_input.get()
        f_list = FIELDS.strip().split(',')
        result = MODELS.execute_kw(DB,UID,PASSWD,MODEL_NAME,'search_read',[],{'fields':f_list})
        count = len(result)
        self.count_info.insert(1.0,count)
        for item in result:
            self.display_info.insert(0,item)

    def write_to_file(self):
        MODELS,DB,UID,PASSWD = self.connect()
        MODEL_NAME = self.model_name_input.get()
        FIELDS = self.fields_input.get()
        f_list = FIELDS.strip().split(',')
        result = MODELS.execute_kw(DB,UID,PASSWD,MODEL_NAME,'search_read',[],{'fields':f_list})
        filename = datetime.now().strftime('%m-%d(%H:%M:%S)')+'-'+DB+'-'+MODEL_NAME.replace('.','_')
        with open(filename,'w') as f:
            f.writelines(json.dumps(result))
            print('save done')

    def list_box_clear(self):
        self.display_info.delete(0,END)
        self.count_info.delete(1.0,END)

def main():
    rpc = Rpc_Gui()
    rpc.gui_arrang()
    mainloop()
    pass

if __name__ == "__main__":
    main()
        
