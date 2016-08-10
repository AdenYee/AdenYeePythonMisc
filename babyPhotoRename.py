# encoding: utf-8
import os
import shutil
import time
import datetime

photoDir = "E:\\baby"
babyBirthday = datetime.datetime(2016, 4, 29)


def parse(srcDir):
    for f in os.listdir(srcDir):
        file = os.path.join(srcDir, f)
        try:
            file = unicode(file, "gbk")
        except Exception,e:
            try:
                file = unicode(file, "utf8")
            except Exception,e:
                pass
        if os.path.isdir(file):
            parse(file)
        else:
            m_time = os.stat(file).st_mtime
            timeArray = time.localtime(m_time)
            otherStyleTime = time.strftime("%Y-%m-%d %H_%M_%S", timeArray)
            dt = datetime.datetime(timeArray[0], timeArray[1], timeArray[2])
            detaDays = (dt-babyBirthday).days + 1
            newName = str(detaDays) + u"天 (" + otherStyleTime+")";
            ext = os.path.splitext(file)[1]
            newFile = os.path.join(srcDir, newName+ext)
            if os.path.exists(newFile)==False:
                pass
            else:
                count = 1
                while os.path.exists(os.path.join(srcDir, newName+"_"+str(count)+ext)):
                    count += 1
                newFile = os.path.join(srcDir, newName+"_"+str(count)+ext)
            print u"正在重命名:"+file+"----->"+newFile
            os.rename(file, newFile)

parse(photoDir)
os.system("pause")

