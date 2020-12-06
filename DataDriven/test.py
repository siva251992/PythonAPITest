import os

l=os.listdir('C:\\Users\\esivxxx\\Desktop\\test')

if len(l)==0:
    print('There are no files to delete')
else:
    for i in l:
        os.remove('C:\\Users\\esivxxx\\Desktop\\test\\' + i)

    print('Files removed')






