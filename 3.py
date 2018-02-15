 # List my public Google+ activities.
result = service.activities().list(userId='me', collection='public').execute()
tasks = result.get('items', [])
for task in tasks:
    print task['title']
