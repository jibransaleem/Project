import re
import datetime as dt
import phonenumbers
import requests
from dotenv import load_dotenv   
import os
import json
class Auth:
    def __init__(self):
        pass
    def Name(self):
        self.name : str = input('Enter your name : ').strip().lower()
        check = '^[^123456789!@#$%^&*()].*'
        if re.search(check,self.name).group()!=None:
            pass
        raise Exception('Please Enter valid user name ')
    def last(self):
        self.father : str = input('Enter you last name : ').strip.lower()
        check = '^[^123456789!@#$%^&*()].*'
        if re.search(check,self.father).group()!=None:
            pass
    def dof(self):
        self.dof : str = input('Enter your Date of Birth [year - month -date : ]').strip()
        checker= r'^\d{4}.+\d{1,12}.+\d{1,30}$'
        if re.match(checker , self.dof).group()!=None:
            pass
        raise Exception('Please Enter date of birth in this order [YYY-MM-DD]')
    def ContactNumber(self):
        self.region : str  = input('Enter you region : ').strip()
        self.number : str = input('Enter your phone Number: ').strip()
        try :
            parse_ = phonenumbers.parse(self.number,self.region)
            if( phonenumbers.is_valid_number(parse_) )and ( phonenumbers.region_code_for_number(parse_) == self.region):
                pass
            else:
                raise Exception('Please Enter valid details !')
        except  phonenumbers.NumberParseException:
            print('Invalid Phone number format')

    def Email(self):
        self.email : str = input('Enter your email : ')
        #load_dotenv()
        #api_key = os.getenv('API_KEY')
        try :
            api_key = '64965a7c-f5de-46c4-8750-a8758c002308'
            url = f'https://api.mails.so/v1/validate?email={self.email}'
            header = {
            'x-mails-api-key': api_key
            }   
            resp = requests.get(url,headers=header)
            if resp.status_code == 200:
                data = resp.json()
                op = 'deliverable'
                if data['data']['result'] ==op:
                    pass
            else:
                print(resp.status_code)
                
        except requests.exceptions.RequestException as e:
            print(e)
            
