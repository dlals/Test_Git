# 간단한 클래스 정의하기
class Member:
    username = None
    email = None

    def __init__(self, username, email):
        print("------- 생성자가 실행되었습니다. --------")
        self.username = username
        self.email = email

    def view_info(self):
        tpl = "이름: {0} / 이메일: {1}"
        print( tpl.format(self.username, self.email) )


