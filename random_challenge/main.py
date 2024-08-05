import csv
from faker import Faker
import random


def generate_person(num_of_ppl):
    fake = Faker()
    ppl = []
    for _ in range(0,int(num_of_ppl)):
        name = f"{fake.first_name()} {fake.last_name()}"
        age = random.randint(18,100)
        email = fake.ascii_safe_email()
        ppl.append({'name':name,'age':age,'email':email})
    return ppl

def create_contact_file(numOfPpl,numOfFiles):

    for f in range(0,int(numOfFiles)):
        people = generate_person(numOfPpl)
        filename = f"contact_list{f+1}.csv"
        headers = ['name','age','email']
        with open(filename,'w') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames= headers)
            writer.writeheader()
            for p in people:
                writer.writerow(p)


# fake = Faker()
# print(fake.first_name())
# print(fake.last_name())
# print(fake.ascii_safe_email())
# print(random.randint(18,100))

create_contact_file(50,100)
