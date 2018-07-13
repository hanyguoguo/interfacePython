# coding:utf-8
import requests
import json


class RunMethod:
    def post_main(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res.json()

    def get_main(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, data=data, verify=False)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'Post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return json.dumps(res)

    # return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)

if __name__=="__main__":
    # url='http://clinicpe.zhiyiyunzhenshi.com/zyPublic/patientInfo/allPatient'
    # data={"sysUserId":"ff808081648d0d0301648d1729180012"}
    url="http://bt-clinicpe.yunzhenshi.com/zyPublic/patientInfo/allTag"
    runner=RunMethod()
    res=runner.run_main('Post',url)
    # print type(json.dumps(data))
    print res