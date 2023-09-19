import numpy as np

class FileManager:
    #저장 함수
    def save_userlist(self,target_list):
        np.save('userlist.npy',target_list)

    #파일 불러오기 함수
    def load_list(self):
        try:
            loeded_user_list = np.load('userlist.npy',allow_pickle=True)
        except FileNotFoundError:
            init_list = []
            self.save_userlist(init_list)
            loeded_user_list = np.load('userlist.npy',allow_pickle=True)
        return loeded_user_list

