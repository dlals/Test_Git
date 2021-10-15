# -> 경로 정보를 취득하기 위한 모듈
import os.path
# -> 발송서버와 연동하기 위한 모듈
from smtplib import SMTP
# -> 본문 구성 기능
from email.mime.text import MIMEText
# -> 파일을 Multipart 형식으로 변환
from email.mime.application import MIMEApplication
# -> 파일을 본문에 추가하는 기능 제공
from email.mime.multipart import MIMEMultipart

def send_mail(from_addr, to_addr, subject, content, files=[]):
    content_type = "html"
    username = 'zmfwl123@gmail.com'
    password = 'shnucvzoelldrmev'
    smtp = 'smtp.gmail.com'
    port = 587
    
    # 메일 발송 정보를 저장하기 위한 객체
    msg = MIMEMultipart()
    msg['Subject'] = subject  # 메일 제목
    msg['From'] = from_addr   # 보내는 사람
    msg['To'] = to_addr       # 받는사람

    # 본문 설정 -> 메일의 내용과 형식 지정
    msg.attach(MIMEText(content, content_type))
    
    if files:
        for f in files:
            with open(f, 'rb') as a_file:
                basename = os.path.basename(f)
                part = MIMEApplication(a_file.read(), Name=basename)
                part['Content-Disposition'] = 'attachment; filename="%s"' % basename
                msg.attach(part)
        
    mail = SMTP(smtp)
    mail.ehlo()
    mail.starttls()
    mail.login(username, password)
    mail.sendmail(from_addr, to_addr, msg.as_string())