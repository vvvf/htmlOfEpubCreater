text = '''
<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<html xml:lang="zh-CN" xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>1</title>
    <link href="css/style.css" rel="stylesheet" type="text/css"/>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
</head>
  <body>
    <div>
      <img src="xxxxx"/>
    </div>
  </body>

</html>

'''

import os
import os.path

rootdir = 'C:\\Users\\lin\\Desktop\\xxxx'
filelist = []

for parent, dirnames, filenames in os.walk(rootdir):
   # print(parent, dirnames, filenames)
    
   if len(filenames) != 0 : #filenames不为空，表示存在文件
       for filename in filenames:
            path = parent + '\\' + filename
            filelist.append(path[len(rootdir)+1:]) #只保留相对路径







for file in filelist:
    f= open(rootdir + "\\" + file.split('\\')[-1].split('.')[0] + ".html", "w+")
    new_text = text.replace("xxxxx", file) # html文件内容
    f.write(new_text)
    f.close()

