def registration(student_details):
    print('---- REGISTRATION ----')
    name=input('enter name ')
    id=int(input('enter id '))
    course=input('enter course ')
    password=input('enter password ')
    for i in student_details:
        if(id==i.get('id')):
            return 'duplicate'
    deatils=[{
        'name':name,
        'id':id,
        'course':course,
        'password':password
        }]
    student_details += deatils
    return 'registered'

def login(student_details):
    print('---- LOGIN ----')
    name=input('enter name ')
    password=input('enter password ')
    for i in student_details:
        if i.get('name')==name:
            if i.get('password')==password:
                return ['logged in',i.get('id')]
            else:
                return ['incorrect password',None]
    return ['error',None]

def marks_details(marks,id):
    print('--- enter your marks ---')
    maths=float(input('maths: '))
    chemistry=float(input('chemistry: '))
    physics=float(input('physics: '))
    avg=(maths+physics+chemistry)/3
    status=''
    if(avg>90):
        status='first class'
    elif(avg<90 and avg>75):
        status='second class'
    elif(avg<75 and avg>50):
        status='average'
    else:
        status='fail'
    data=[{
        'id':id,
        'maths':maths,
        'physics':physics,
        'chemistry':chemistry,
        'avg':avg,
        'status':status}]
    marks +=data
    return 'inserted'

def results(marks,stu,id):
    for i in stu:
        if(i.get('id')==id):
            for j in marks:
                if(j.get('id')==id):
                    print('     --- Results ---')
                    print(f'Name:{i.get('name')}\nId:{i.get('id')}\nCourse:{i.get('course')}\n     --- Marks ---    ')
                    print(f'Maths:{j.get('maths')}\nChemistry:{j.get('chemistry')}\nPhysics:{j.get('physics')}\nGrand Total:{j.get('maths')+j.get('physics')+j.get('chemistry')}\nAverage:{j.get('avg')}\nStatus:{j.get('status')}')
                    return '     ----- **** ------ '
            return 'login and enter marks'
    return 'not yet registered'

def start():
    stu=[]
    marks=[]
    print('Student Page')
    print('1. Register --> (register)\n2. Login and enter marks --> (login)\n3. Get all student details --> (all)\n4. Get result --> (result)')
    while True:
        x=input('enter choice ')
        if x=='exit':
            print('-------')
            break
        elif x=='register':
            result=registration(stu)
            if result == 'duplicate':
                print('student already exists')
                print('-------')
                continue
            print(result)
            print('-------')
            continue
        elif x=='login':
            res,id=login(stu)
            if(res=='error'):
                print('user doesnt exist,register to continue')
                print('-------')
                continue
            elif(res=='incorrect password'):
                print(res)
                print('-------')
                continue
            else:
                print(res)
                print(marks_details(marks,id))
                print('-------')
                continue
        elif x=='result':
            id=int(input('enter your id to know results '))
            x=results(marks,stu,id)
            print(x)
            continue
        elif x=='all':
            if len(stu)==0:
                print('Empty register to continue')
                print('-------')
                continue
            for i in stu:
                for j in marks:
                    if(i.get('id')==j.get('id')):
                        print('-------')
                        print(f'Name:{i.get('name')}\nId:{i.get('id')}\nCourse:{i.get('course')}')
                        print('-------')
        else:
            print('enter valid choice')
start()