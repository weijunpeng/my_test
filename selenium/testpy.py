import os
import re

title_name= 'xxxxx'



path = r"C:\Users\v_weijpeng.TENCENT\Downloads\成为一名合格律师"
if not os.path.exists(path):
    os.mkdir(path)

ls_file=os.listdir(r'C:\Users\v_weijpeng.TENCENT\Downloads')
listdir = [file for file in ls_file if re.match('\d{4}_\d{2}_\d{2} \d{2}_\d{2}.*',file)]
print(listdir)
listdir.sort()
os.rename((r'C:\Users\v_weijpeng.TENCENT\Downloads'+'\\'+listdir[-1]), path+'\\'+listdir[-1]) #移动
os.rename((path+'\\'+listdir[-1]), path+'\\'+title_name+'.mp4') #重命名

