import itchat
from pandas import DataFrame

itchat.auto_login()

friends = itchat.get_friends(update=True)[0:]

for friend in friends:
    print(friend)


def get_var(var):
    v = []
    for f in friends:
        value = f[var]
        v.append(value)
    return v


nickname = get_var('NickName')
sex = get_var('Sex')
province = get_var('Province')
city = get_var('City')
signature = get_var('Signature')

data = {'NickName': nickname, 'Sex': sex, 'Province': province, 'City': city, 'Signature': signature}
frame = DataFrame()
frame.to_csv('data.csv', index=True)

print('finish save')
