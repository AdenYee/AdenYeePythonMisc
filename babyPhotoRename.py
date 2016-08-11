# encoding: utf-8
import os
import re
import time
import datetime

photoDir = "E:\\YiKS\\BB"
babyBirthday = datetime.datetime(2016, 4, 29)


def parse(srcDir):
    for f in os.listdir(srcDir):
        try:
            f = unicode(f, "gbk")
        except Exception,e:
            try:
                f = unicode(f, "utf8")
            except Exception,e:
                pass
        file = os.path.join(srcDir, f)
        if os.path.isdir(file):
            parse(file)
        else:
            matchObj = re.match(ur'\d+天\s\(\d{4}-\d{2}-\d{2}\s\d{2}_\d{2}_\d{2}.*', f, re.U)
            if matchObj:
                continue
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

