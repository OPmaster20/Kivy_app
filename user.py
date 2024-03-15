import pymysql
import time,re
from kivy.uix.widget import Widget
import message
import random as ran
import sqlite3

conn = sqlite3.connect('E:\\sqlite_database\music.db')
cur = conn.cursor()
user_id = 1
def search(username,password):
    str = "username:" + username + "password:" + password
    if len(username) == 0:
        message.mess1(2)
        return 1
    if len(password) == 0:
        message.mess1(3)
        return 1
    if str == "username:password:":
        message.mess1(1)
        return 1
    if see_user_infor(username,password):
        return 0
    else:
        return 1


def import_guest():
    sys_user = 'g_'
    sys_pass = ''
    for i in range(6):
        sys_pass += str(ran.randint(0,9))

    for j in range(10):
        sys_user += ran.choice("abcdefgABCDEFG")

    insert = "insert into guset(sys_user,sys_pass) values(\'" + sys_user + "\',\'" + sys_pass + "\');"
    cur.execute(insert)
    conn.commit()

    return True
def see_user_infor(username,password):
    global user_id
    from_database = ("select * from user_register join user_infor on user_register.user_id_re = user_infor.user_id "
                     "where user_name = \'" + str(username) + '\' and pass_word = \'' + str(password) + '\';')

    cur.execute(from_database)
    if len(cur.fetchall()) == 1:
        get_user_id(username,password)
        return True
    message.mess1(8)
    print(len(cur.fetchall()))
    return False

def get_user_id(username,password):
    global user_id
    user_id = "select user_id_re from user_register " + "where user_name = \'" + str(
        username) + '\' and pass_word = \'' + str(password) + '\';'
    cur.execute(user_id)
    user_id = cur.fetchall()[0][0]
    print(user_id)
def register_search(username,password,password_re,email):
    if len(username) + len(password) + len(email) == 0:
        message.mess1(1)
    elif len(username) == 0:
        message.mess1(2)
    elif len(password) == 0:
        message.mess1(3)
    elif len(email) == 0:
        message.mess1(7)
    elif password != password_re:
        message.mess2(2)

    if len(username) > 15 and len(password) > 15:
        message.mess2(3)

    if re.search(r'^[A-Za-z0-9@#$%^&+=]{3,}$',str(password)):
        if re.search(r'^.+@(qq)|(gmail)\\.com$',str(email)):
            update = "insert into user_infor(log_in_time,status,log_out_time) values(\'" + str(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())) + '\',"online","None");'
            cur.execute(update)
            conn.commit()
            load = "insert into user_register(user_name,pass_word,email) values(\'" + str(username) + '\',\'' + str(
                password) + '\',\'' + str(email) + '\');'
            cur.execute(load)
            conn.commit()
            get_user_id(username, password)
            return True
        else:
            message.mess2(4)
            return False
    else:
        message.mess2(7)
        return False



def search_for_songs(infor):
    search = "select songs_name,songs_style,singer_name,songs_published_date from user_times join songs_infor on user_times.songs_id = songs_infor.songs_id_infor where songs_name like '%" + infor + '%\' or songs_name = \'' + infor + '\';'
    print(search)
    cur.execute(search)
    if len(cur.fetchall()) == 0:
        #return False
        return "No any result"
    else:
        cur.execute(search)
        re = dict()
        du = list(cur.fetchall()[0])
        re = {"song":du[0],"style":du[1],"singer":du[2],"publish_date":str(du[3])}
        print(re)
        #return True
        return re

def update_count_songs(song_name):
    global user_id
    if user_id == 0:
        print("Not working")
    get_songs_id = "select songs_id_infor from songs_infor where songs_name = \'" + song_name + "\';"
    print(get_songs_id)
    cur.execute(get_songs_id)
    songs_id = cur.fetchall()[0][0]
    update = "update user_times set song_times = song_times + 1 where user_id_infor = " + str(user_id) + " and songs_id = " + str(songs_id) + ";"
    cur.execute(update)
    conn.commit()

def user_log_out_fun():
    global user_id
    if user_id_see():
        exit = "update user_infor set status = 'offline',log_out_time = \'" + str(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())) +"\' where user_id = " + str(user_id) + ";"
        cur.execute(exit)
        conn.commit()
        message.work1(3)

def user_id_see():
    global user_id
    if user_id == 0:
        print("Not working")
    search = "select count(*) from user_infor where user_id = " + str(user_id) + ";"
    cur.execute(search)
    if int(cur.fetchall()[0][0]) != 0:
        return True
    return False
def computer_user_loved():
    global user_id
    if user_id_see():
        cal = ("select singer_name from songs_infor join user_times on songs_infor.songs_id_infor = user_times.songs_id "
               "join user_infor on user_infor.user_id = user_times.user_id_infor where user_infor.user_id = " + str(user_id) + " group by singer_name having max(song_times)")

        cur.execute(cal)
        return cur.fetchall()[0][0]

def computer_user_loved_song():
    global user_id
    if user_id_see():
        cal = ("select songs_name,song_times from songs_infor,user_times "
               "where user_times.user_id_infor = " + str(user_id) + " and songs_infor.songs_id_infor = user_times.songs_id "
               "order by song_times DESC;")
        cur.execute(cal)
        re = cur.fetchall()[0]
        return re[0],re[1]

def get_username():
    global user_id
    if user_id_see():
        get = "select user_name from user_register where user_id_re = " + str(user_id) + ";"
        cur.execute(get)
        #print(cur.fetchall()[0][0])
        return cur.fetchall()[0][0]

def check_status_true():
    global user_id
    check = "select status from user_infor where user_infor.user_id = " + str(user_id) + ";"
    cur.execute(check)

    if str(cur.fetchall()[0][0]) == "offline":
        return False
    return True