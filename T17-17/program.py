i = get_safe('id')
username = ""
if i != 0:
    username = get('username')
    username = escape_string(username)
else:
    username = name
query = 'some query'
it = execute(query + username)
