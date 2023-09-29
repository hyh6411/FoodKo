

re_table = {
    '1': {'msg': '访问成功!'},
    '2': {'msg': '传参错误!'},
    '3': {'msg': '数据库错误!'},
    '4': {'msg': '服务器出错!'},
    '5': {'msg': '未知错误!'}
}


class ReBase:

    def __init__(self, status, msg='', obj={}) -> None:
        self.status = status
        self.obj = obj
        if msg:
            self.massage = msg
        else:
            self.massage = re_table[status]['msg']
        pass

    def print(self):
        return {
            'status': self.status,
            'massage': self.massage,
            'result': self.obj
        }
