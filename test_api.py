from requests import get, post, delete
print(get('http://localhost:5000/api/v2/users').json())
print(get('http://localhost:5000/api/v2/users/5').json())
print(get('http://localhost:5000/api/v2/users/52').json())
print(post('http://localhost:5000/api/v2/users', json={'user_id': 3, 'name': 'Anton3', 'position': 'idk',
                                                       'surname': 'sochenko', 'age': 54, 'address': 'module_3',
                                                       'speciality': 'tester',
                                                       'hashed_password': '123456', 'email': 'antonim_s3@mail.ru'}).json())
print(post('http://localhost:5000/api/v2/users').json())
print(post('http://localhost:5000/api/v2/users', json={'name': 'a'}).json())
print(delete('http://localhost:5000/api/v2/users/999').json())
print(get('http://localhost:5000/api/v2/users').json())
print(delete('http://localhost:5000/api/v2/users/3').json())