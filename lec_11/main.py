import json
import requests


# GET
response = requests.get('https://jsonplaceholder.typicode.com/posts')
if response.status_code == 200:
    posts = response.json()
    print('all posts')
    print(json.dumps(posts, indent=2))

    title_filtered_posts = [post for post in posts if len(post['title'].split()) <= 6]
    print('Posts filtered by title')
    print(json.dumps(title_filtered_posts, indent=2))

    body_filtered_posts = [post for post in posts if len(post['body'].split('\n')) <= 3]
    print('Posts filtered by body')
    print(json.dumps(body_filtered_posts, indent=2))


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
        'title': 'new post',
        'body': 'post body.',
        'userId': 1
    }
)
if response.status_code == 201:
    new_post = response.json()
    print('ADDED POST')
    print(json.dumps(new_post, indent=2))

# PUT
response = requests.put(
    'https://jsonplaceholder.typicode.com/posts/1',
    json={
        'title': 'Updated title',
        'body': 'Updated body of the post.',
        'userId': 1
    }
)
if response.status_code == 200:
    updated_post = response.json()
    print('UPDATED POST 1')
    print(json.dumps(updated_post, indent=2))


# PATCH
response = requests.patch(
    'https://jsonplaceholder.typicode.com/posts/1',
    json={
        "title": "Partially Updated Title"
    }
)
if response.status_code == 200:
    partially_updated_post = response.json()
    print('PARTIALLY UPDATED POST 1')
    print(json.dumps(partially_updated_post, indent=2))


# DELETE
response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
if response.status_code == 200:
    print('POST 1 DELETED')