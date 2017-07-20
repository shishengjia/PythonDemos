from cStringIO import StringIO
from imaplib import IMAP4_SSL
from platform import python_revision
from smtplib import SMTP
from poplib import POP3_SSL

# 判断python的版本，SMTP_SSL只支持python2.6.2以上
release = python_revision()
if release > '2.6.2':
    from smtplib import SMTP_SSL # fixed in 2.6.3
else:
    SMTP_SSL = None

from Secert import *
who = '%s@gmail.com' % MAILBOX
from_ = who
# 收件人以列表进行存储
to = [who]

# 邮件头部
headers = [
    'From: %s' % from_,
    'To: %s' % ', '.join(to),
    'Subject: test SMTP send via 587/TLS'
]

# 邮件正文
body = [
    'Hello',
    'World'
]

# 组装
msg = '\r\n\r\n'.join(('\r\n'.join(headers), '\r\n'.join(body)))

# 获取邮件的Subject
def getSubject(msg, default='(no subject line)'):
    for line in msg:
        if line.startswith('Subject:'):
            return line.rstrip()
        if not line:
            return default

# 以SMTP/TLS协议进行邮件的发送
print('***Doing SMTP send via TLS')
s = SMTP('smtp.gmail.com', 587)
if release < '2.6':
    s.ehlo()
s.starttls()
if release < '2.5':
    s.ehlo()

s.login(MAILBOX, PASSSWD)
s.sendmail(from_, to, msg)
s.quit()
print('   TLS mail sent')


# 以POP协议接受邮件
print('***Doing POP recv')
s = POP3_SSL('pop.gamil.com', 995)
s.user(MAILBOX)
s.pass_(PASSSWD)
rv, msg, sz = s.retr(s.stat()[0])
s.quit()
line = getSubject(msg)
print('Received msg via POP: %r' % line)

body = body.replace('587/TLS', '465/SSL')

# 以SMTP/SSL发送邮件
if SMTP_SSL:
    print('*** Doing SMTP send via SSL...')
    s = SMTP_SSL('smtp.gmail.com', 465)
    s.login(MAILBOX, PASSSWD)
    s.sendmail(from_, to, msg)
    s.quit()
    print('   SSL mail sent')

# 以IMAP协议接受邮件
print('*** Doing IMAP recv')
s = IMAP4_SSL('imap.gmail.com', 993)
s.login(MAILBOX, PASSSWD)
rsp, msgs = s.select('INBOX', True)
rsp, data = s.fetch(msgs[0], '(RFC822)')
line = getSubject(StringIO(data[0][1]))
s.close()
s.logout()
print('Received msg via IMAP: %r' % line)
