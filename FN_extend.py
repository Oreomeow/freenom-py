# -*- coding: utf8 -*-
"""
Author: shuai93
Modifier: Oreo
Date: Wed Aug 11 10:15:41 UTC 2021
cron: 25 7 */10 * *
new Env('Freenom 续期邮件版');
------------
环境变量说明                     示例
FN_ID: Freenom 用户名           1234567890@gmail.com
FN_PW: Freenom 密码             12345678
MAIL_USER: 发件人邮箱用户名      address@vip.qq.com 或 123456@qq.com
MAIL_ADDRESS: 发件人邮箱地址     address@vip.qq.com 或 123456@qq.com
MAIL_PW: 发件人邮箱授权码        xxxxxxxxxxxxxxxx 看下方链接
* MAIL_HOST: 发件人邮箱服务器    smtp.qq.com 不填默认为这个
* MAIL_PORT: 邮箱服务器端口      465 不填默认为这个
MAIL_TO: 收件人邮箱可与发件人相同 address@vip.qq.com 或 123456@qq.com   

填写总参考：https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=369
------------
依赖模块说明
pip install -r requirements.txt / pip3 install -r requirements.txt
"""

from utils.exception import CustomException
from utils.freenom import FreeNom
from utils.mail import EmailPoster
from utils.settings import (
    FN_ID,
    FN_PW,
    MAIL_ADDRESS,
    MAIL_HOST,
    MAIL_PORT,
    MAIL_PW,
    MAIL_TO,
    MAIL_USER,
)


def mask_data(data: str) -> str:
    return "".join(
        ["*" if i > 2 and i < len(data) - 3 else data[i] for i in range(len(data))]
    )


def main():
    envs = [
        FN_ID,
        FN_PW,
        MAIL_USER,
        MAIL_ADDRESS,
        MAIL_PW,
        MAIL_HOST,
        MAIL_PORT,
        MAIL_TO,
    ]
    print("配置信息（脱敏后）：")
    print([mask_data(env) if isinstance(env, str) else env for env in envs])
    if not all(envs):
        raise CustomException("参数缺失")

    body = {
        "subject": "FreeNom 自动续期",
        "to": [MAIL_TO],
    }
    try:
        results = FreeNom().run()
        body["payload"] = {"results": results, "user": FN_ID}
    except CustomException as e:
        body["body"] = e.message

    EmailPoster().send(data=body)


if __name__ == "__main__":
    main()
