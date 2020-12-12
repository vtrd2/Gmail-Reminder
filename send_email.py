import smtplib, time

class Sending():
    '''Cuida do envio dos emails'''
    def __init__(self):
        self.email = ''
        self.senha = ''
        self.domain = 'smtp.gmail.com'
        self.get_email()
        # self.smtp_obj = self.connect()

    def get_email(self):
        while True:
            email, senha = self.receive_data_email()
            existent_email = self.testa_email(email, senha)
            if existent_email:
                print('\nConected\n')
                break
            else:
                print('''\nThis gmail doesn't exist, or you entered the wrong password''')
        self.email = email
        self.senha = senha

    @staticmethod
    def receive_data_email():
        email = input('Enter your gmail: ')
        senha = input('Enter the gmail password: ')
        return email, senha
    
    def testa_email(self, email, senha):
        smtp_obj = smtplib.SMTP(self.domain, '587')
        smtp_obj.ehlo()
        smtp_obj.starttls()
        try:
            smtp_obj.login(email, senha)
        except Exception:
            return False
        finally:
            smtp_obj.quit()
        return True

    def send_mail(self, assunto, message):
        smtp_obj = smtplib.SMTP(self.domain, '587')
        smtp_obj.ehlo()
        smtp_obj.starttls()
        smtp_obj.login(self.email, self.senha)        
        smtp_obj.sendmail(self.email, self.email, f'Subject:{assunto}\n{message}')
        smtp_obj.quit()

if __name__ == "__main__":
    sending = Sending()
    sending.send_mail('assunto', 'oi')