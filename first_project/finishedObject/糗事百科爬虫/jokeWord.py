import win32com.client
import pickle

path = r'D:\qian_feng_education\first_project\myClass\糗事百科\jock.txt'
toPath = r'D:\qian_feng_education\first_project\myClass\糗事百科\joke.docx'

word = win32com.client.Dispatch('Word.Application')
word.Visible = True
doc = word.Documents.Add()
r = doc.Range(0, 0)

with open(path, 'rb') as f:
    jokeList = pickle.load(f)

for jokeDict in jokeList:
    for k, v in jokeDict.items():
        k = '【' + k + '】'
        v = v.replace('<br/>', '') + '\n'
        r.InsertAfter('{}\n'.format(k))
        r.InsertAfter('    {}\n'.format(v))

doc.SaveAs(toPath)
doc.Close()
word.Quit()