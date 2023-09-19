from FileIOmanager import FileManager
import enum_collection
import my_user

class UserManager():
    def user_manager(self,user_list):
            while(True):
                print("\n1)유저 추가")
                print("2)유저 삭제")
                print("3)유저 보기")
                print("4)종료")

                user_selection = int(input("입력하세요:"))
                if (user_selection == enum_collection.USERMENU.ADD_USER):
                    user_name = input("이름을 입력하세요:")
                    user_list.append(my_user.User(user_name))
                    FileManager.save_userlist(user_list)

                elif(user_selection == enum_collection.USERMENU.DELETE_USER):
                    pass
                elif(user_selection == enum_collection.USERMENU.SHOW_USER):
                    pass
                else:
                    break