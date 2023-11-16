import requests
import json


# GET
response = requests.get('https://jsonplaceholder.typicode.com/posts')
if response.status_code == 200:
    posts = response.json()
    print('ALL POSTS')
    print(json.dumps(posts, indent=2))

    byTitle = [post for post in posts if len(post['title'].split()) <= 6]
    print('Posts filtered by title')
    print(json.dumps(byTitle, indent=2))

    byBody = [post for post in posts if len(post['body'].split('\n')) <= 3]
    print('Posts filtered by body')
    print(json.dumps(byBody, indent=2))


# GET BY ID
response = requests.get('https://jsonplaceholder.typicode.com/posts/2')
if response.status_code == 200:
    post = response.json()
    print('POST #2')
    print(json.dumps(post, indent=2))

# GET COMMENTS OF POST 2
response = requests.get('https://jsonplaceholder.typicode.com/posts/2/comments')
if response.status_code == 200:
    comments = response.json()
    print('POST #2 COMMENTS')
    print(json.dumps(comments, indent=2))


# POST
response = requests.post(
    'https://jsonplaceholder.typicode.com/posts',
    json={
        'title': 'NEW post',
        'body': 'Post body',
        'userId': 1
    }
)
if response.status_code == 201:
    newPost = response.json()
    print('POST ADDED')
    print(json.dumps(newPost, indent=2))

# PUT
response = requests.put(
    'https://jsonplaceholder.typicode.com/posts/1',
    json={
        'title': 'Change title',
        'body': 'post body.',
        'userId': 1
    }
)
if response.status_code == 200:
    updatedPost = response.json()
    print('UPDATED POST 1')
    print(json.dumps(updatedPost, indent=2))


# PATCH
response = requests.patch(
    'https://jsonplaceholder.typicode.com/posts/1',
    json={
        "title": "Updated Title"
    }
)
if response.status_code == 200:
    updatedPost = response.json()
    print('PARTIALLY UPDATED POST #1')
    print(json.dumps(updatedPost, indent=2))


# DELETE
response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
if response.status_code == 200:
    print('POST #1 DELETED')