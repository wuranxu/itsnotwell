import requests
import os
import zipfile
import subprocess
import clipboard

class Xiaomeng(object):

    URL = "http://idea.medeming.com/jets/images/jihuoma.zip"

    def download(self):
        try:
            r = requests.get(Xiaomeng.URL, timeout=10)
            return r.content
        except Exception as e:
            print("下载激活码失败. error: ", e)
        return None
    
    def fetch_zip(self):
        content = None
        for _ in range(3):
            content = self.download()
            if content is not None:
                break
        else:
            raise Exception("尝试3次均下载失败, 请检查晓梦的网站是否可用")

        if content is not None:
            try:
                with open("temp.zip", mode='wb') as f:
                    f.write(content)
            except Exception as e:
                print("写入文件出错, error: ", e)
            zp = zipfile.ZipFile("temp.zip")
            for file in zp.namelist():
                if "later" in file:
                    zp.extract(file)
                    return file

    def copy_windows(self, file):
        with open(file, mode='r',encoding='utf-8') as data:
            clipboard.copy(data.read())

    def clean(self, file):
        os.remove("temp.zip")
        os.remove(file)



if __name__ == "__main__":
    x = Xiaomeng()
    file = x.fetch_zip()
    x.copy_windows(file)
    x.clean(file)
