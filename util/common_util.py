# coding:utf-8
import json


class CommonUtil:
    def is_contain(self, str_one, str_two):
        '''
        判断一个字符串是否再另外一个字符串中
        str_one:查找的字符串
        str_two：被查找的字符串
        '''
        flag = None
        if isinstance(str_one, unicode):
            str_one = str_one.encode('unicode-escape').decode('string_escape')
        # if isinstance(str_two, unicode):
        #     str_two = str_two.encode('unicode-escape').decode('string_escape')
        # return cmp(str_one, str_two)
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

    def is_equal_dict(self, dict_one, dict_two):
        '''
        判断两个字典是否相等
        '''
        if isinstance(dict_one, str):
            dict_one = json.loads(dict_one)
        if isinstance(dict_two, str):
            dict_two = json.loads(dict_two)
        return cmp(dict_one, dict_two)

if __name__=="__main__":
    common_util=CommonUtil()
    str_one="patientId"
    ss_two={"content": [{"patientStatus": "", "weight": "", "height": "", "relation": "", "peMedical": "", "peAllergy": "", "patientBir": "2010-01-01", "familyHis": "", "patientId": "ff808081648d0d0301648d1f24e9004a", "medicalHis": "", "type": 1, "patientName": "果果", "allergyTag": "", "address": "", "familyHisTag": "", "patientPhone": "13051852468", "medicalHisTag": "", "medicalTag": "", "age": "2010-01-01", "patientSex": 0, "marriage": "", "fertility": ""}, {"patientStatus": "", "weight": "", "height": "", "relation": "", "peMedical": "", "peAllergy": "", "patientBir": "2010-01-01", "familyHis": "", "patientId": "ff808081648d0d0301648d18768e0018", "medicalHis": "", "type": 1, "patientName": "哦哦", "allergyTag": "", "address": "", "familyHisTag": "", "patientPhone": "13051852468", "medicalHisTag": "", "medicalTag": "", "age": "2010-01-01", "patientSex": 1, "marriage": "", "fertility": ""}], "code": "0000"}
    str_two=json.dumps(ss_two)
    print type(str_one)
    print type(str_two)
    print common_util.is_contain(str_one,str_two)