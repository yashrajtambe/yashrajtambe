import mysql.connector as mysql
import datetime
from BG_sound import *
host = "localhost"
user = "ak"
password = "Algo123#"

db = mysql.connect(host=host, user=user,password=password, database="health_management")

c_h = db.cursor(buffered=True)

def get_date():
    return datetime.datetime.now().date()

def get_time():
    return datetime.datetime.now().time()

def client_session(user_input_id):

    print(" ")
    inp = input(
        "Enter 1 :to record diet \nEnter 2 :to record exercise "
        "\nEnter 3 :to view records \nEnter 4 :to download records\nEnter 5 :to Log_out")

    if inp == "1":

        client_inp = input("You have selected: Record diet.\nPlease enter what did you eat today...\n")
        query = (str(get_date()),str(get_time()), client_inp, user_input_id)
        c_h.execute("insert into diet(date, time, diet,id) values (%s, %s, %s, %s )",query)
        db.commit()
        print("Diet has been recorded")

        client_session(user_input_id)
    elif inp == "2":

        client_inp = input("You have selected: Record exercise.\nPlease enter what have you done today...?\n")
        query = (str(get_date()), str(get_time()), client_inp, user_input_id)
        c_h.execute("insert into exercise(date, time, exercise ,id) values (%s, %s, %s, %s )", query)
        db.commit()
        print("Exercise has been recorded")
        client_session(user_input_id)

    elif inp == "3":
        print('-'*20,'diet','-'*20)
        c_h.execute(" select diet.diet,diet.date,diet.time from diet where diet.id = '"+ user_input_id +"'")
        for record in c_h.fetchall():
            print(record)
        print("")
        print('-'*20,'exercise','-'*20)
        c_h.execute("select exercise.exercise,exercise.date, time from exercise where exercise.id = '"+ user_input_id +"'")
        for record in c_h.fetchall():
            print(record)

        client_session(user_input_id)

    elif inp == "4":

        print("downloading records....")
        f= open(f"register_{user_input_id}.txt", "a+")

        f.write('-' * 20+'diet'+'-' * 20+'\n')
        c_h.execute("select diet.diet,diet.date,diet.time from diet where diet.id = '" + user_input_id + "'")
        for record in c_h.fetchall():
            f.write(str(record)+'\n')
        f.write('\n')

        f.write('-' * 20+'exercise'+'-' * 20+'\n')
        c_h.execute("select exercise.exercise,exercise.date, time from exercise where exercise.id = '" + user_input_id + "'")
        for record in c_h.fetchall():
            f.write(str(record)+'\n')
        f.write('\n')
        f.close()
        print("all records saved")
        client_session(user_input_id)

    elif inp == "5":
        c_h.execute("select name from data where id = '"+ user_input_id +"'")
        y = c_h.fetchall()
        for x in y:
            x = str(x).replace("(", "")
            x = str(x).replace(")", "")
            x = str(x).replace("[", "")
            x = str(x).replace("]", "")
            x = str(x).replace(",", "")
            print(f"Have a nice day...{x}")
        end()
        main()

    else:
        print("invalid input")
        client_session(user_input_id)

def login():
    user_input_id = input("enter client id : ")
    user_input_password = input("enter password : ")

    query_vals = (user_input_id, user_input_password)
    c_h.execute("select id, password from data where id = %s and password = %s ", query_vals)

    if c_h.rowcount <= 0:
        print("invalid password")
    else:
        client_session(user_input_id)

def main():
    print("")
    while 1:
        user_input = input("Are you a new user(y/n)")
        if user_input == "y":
            inp1 = input("do you want to continue y/n")
            if inp1 == "y":
                name = str(input("name : "))
                password = str(input("password : "))

                query_vals = (name, password)
                c_h.execute("insert into data(name, password) values (%s,%s)", query_vals)
                db.commit()
                print(name + " has been registered in system")
            else:
                main()
        elif user_input == "n":

            c_h.execute("")
            c_h.execute("select id, name from data")
            lst = c_h.fetchall()
            for j in lst:
                j = str(j).replace("'", " ")
                j = str(j).replace(",", ".")
                j = str(j).replace("(", " ")
                j = str(j).replace(")", " ")
                print(j)

            inp = input("do you want to continue(y/n)")
            if inp == "y":
                login()
            elif inp == "n":
                main()
            else:
                print("please enter valid input")

        else:
            print("Please enter valid input..")
            main()


print("\nWelcome to Health Management System........!")
intro()
main()
