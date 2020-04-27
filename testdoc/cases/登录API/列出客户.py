from lib.webapi import adminapi


class C1:

    name = 'API-0102'
    tags = ['第一次', '二次']

    @staticmethod
    def teststeps():
        adminapi.admin_login('byhy', '88888888', useProxy=False)
        adminapi.customer_list(1, 1, '')


# if __name__ == '__main__':
#     a = C1()
#     a.teststeps()