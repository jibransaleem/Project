import re
import datetime as dt
import phonenumbers
import requests
#from dotenv import load_dotenv   
import bcrypt
import os
import json
import random
class Auth:
    def __init__(self):
        try:
            # self.Name()
            # self.last()
            # self.dof()
            # self.ContactNumber()
            # self.Email()
            self.Password()
            # self.fetch_all()
        except Exception as e:
            print(e)
    def Name(self):
        self.name : str = input('Enter your name : ').strip().lower()
        check = '^[^123456789!@#$%^&*()].*'
        if re.search(check,self.name).group()!=None:
            pass
        else:
            while(re.search(check,self.name).group()==None):
                self.name : str = input('Enter your name again : ').strip().lower()
                
    def last(self):
        self.father : str = input('Enter you last name : ').strip().lower()
        check = '^[^123456789!@#$%^&*()].*'
        if re.search(check,self.father).group()!=None:
            pass
        else:
            while(re.search(check,self.father).group()==None):
                self.father: str = input('Enter your father again : ').strip().lower()
    def dof(self):
        self.dof : str = input('Enter your Date of Birth [year - month -date : ]').strip()
        checker= r'^\d{4}.+\d{1,12}.+\d{1,30}$'
        if re.match(checker , self.dof).group()!=None:
            pass
        else:
            while(re.search(checker,self.dof).group()==None):
                self.dof : str = input('Enter your Date of Birth [year - month -date : ]').strip()
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
    def Password(self):
        choise : str = input('Enter Y to create your own password else hit any button ! ').strip().lower()
        if choise!='y':
            a_z = [chr(i) for i in range(97,123)]
            A_Z = [chr(i) for i in range(65,91)]
            spec =list("!#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
            key = []
            for i in range(1,3):
                index = random.randint(0,25)
                key+=(a_z[index])
            random.shuffle(key)
            for i in range(1,2):
                index = random.randint(0,25)
                key+=(A_Z[index])
            random.shuffle(key)
            for i in range(1,3):
                index = random.randint(0,len(spec))
                key+=(spec[index])
            random.shuffle(key)
            for i in range(random.randint(1,3)):
                key+=(str(random.randint(0,9)))
            random.shuffle(key)
            if len(key)<7:
                for i in range(7-len(key)):
                    index = random.randint(0,25)
                    key+=(A_Z[index])
            random.shuffle(key)
            key = "".join(key)
        else:
            key = input('Enter password (length should be greater than 6 ) :').strip()
            while(len(key)<6):
                key = input('Please enter password according to rule (length should be greater than 6 ) :').strip()
           
            self.__hashed = bcrypt.hashpw(key.encode('utf-8') , bcrypt.gensalt())
            #if bcrypt.checkpw(vld.encode('utf-8'),self.ContactNumber__hashed):
    def fetch_all(self):
            dicts = {
                'name'  : self.name,
                'father' : self.father,
                'Birthday' : self.dof,
                'email' : self.email,
                'Contact' : self.ContactNumber,
                'Password' : self.__hashed           
            }
            try:
            # Load the existing data from the file
                with open('data.json', 'r+') as file:
                    try:
                        existing_data = json.load(file)
                    except json.JSONDecodeError:
                        existing_data = []

                # Check if the email already exists in the data
                for entry in existing_data:
                    if entry['email'] == self.email:
                        return

                # Append the new data if email is not already present
                existing_data.append(dicts)

                # Move the cursor to the beginning of the file and overwrite
                file.seek(0)
                json.dump(existing_data, file, indent=4)

            except FileNotFoundError:
            # If the file does not exist, create it and write the data
                with open('data.json', 'w') as file:
                    json.dump([dicts], file, indent=4)
                      
        
        

a =Auth()
