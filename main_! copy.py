from module.FileIOmanager import FileManager
from module.user_manager import UserManager



class Main:
    #메인 메소드
    def menu(self,list):
        print("\n1)유저 추가")
        print("2)유저 삭제")
        print("3)유저 보기")
        print("4)종료")

        while True:
            try:
                user_select = int(input("번호를 입력 해주세요:"))
                break
            except:
                print("숫자로 번호를 다시 입력 해주세요\n")

        if user_select == Menu.ADD_USER.value:
            self.select_shape(list)

        elif user_select == Menu.DELETE_USER.value:
            list.show_list()
            list.delete_shape(self.input_delete_shape())

        elif user_select == Menu.PRINT_SHAPE.value:
            list.show_list()

        elif user_select == Menu.EXIT.value:
            save = FileManager()
            save.save_shape(list.set_up_list)
            quit()
    #원 정보 입력
    def input_circle(self):
        self.x = int(input("중심좌표를 x를 입력하세요:"))
        self.y = int(input("중심좌표를 y를 입력하세요:"))
        self.r = int(input("반지름을 입력하세요:"))
        print("도형이 추가되었습니다")
    #나머지 도형 정보 입력
    def input_height_width(self):
        self.width = int(input("가로 길이를 입력하세요:"))
        self.height = int(input("세로 길이를 입력하세요:"))
        print("도형이 추가되었습니다")
    #도형 삭제 입력
    def input_delete_shape(self):
        self.delete_shape_id = int(input("삭제하고 싶은 도형의 ID를 입력해주세요:"))
        return self.delete_shape_id
    #도형 선택함수
    def select_shape(self,list):
        print("1.원형", "\n2.삼각형", "\n3.사각형")
        user_select_shpae = int(input(("어떤 도형을 추가 하시겠습니까:\n")))

        if user_select_shpae == ShapeType.CIRCLE.value:
            self.input_circle()
            list.add_shape(shape.Circle(self.x, self.y, self.r))

        elif user_select_shpae == ShapeType.TRIANGLE.value:
            self.input_height_width()
            list.add_shape(shape.Triangle(self.width,self.height))

        elif user_select_shpae == ShapeType.RECTANGLE.value:
            self.input_height_width()
            list.add_shape(shape.Rectangle(self.width,self.height))

if __name__ == '__main__':
    FIOM = FileManager()
    UM = UserManager()

    user_list = FIOM.loadlist()
    UM.user_manager(user_list)

    # while True:
    #     main.main_menu(list)