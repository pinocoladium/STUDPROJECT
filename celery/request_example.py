# import time

# import requests

# resp = requests.post('http://127.0.0.1:5000/upscale', files={
#     'image_before': open('example/lama_300px.png', 'rb')
# })
# resp_data = resp.json()
# # print(resp_data)
# task_id = resp_data.get('task_id')
# # print(task_id)

# resp = requests.get(f'http://127.0.0.1:5000/upscale/{task_id}')
# print(resp.json())
# while resp.json()['status'] == 'PENDING':
#     resp = requests.get(f'http://127.0.0.1:5000/upscale/{task_id}')
#     print(resp.json())
#     time.sleep(3)

# resp = requests.get(f'http://127.0.0.1:5000/upscale/{task_id}')
# print(resp.json()