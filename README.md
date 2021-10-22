<div align="center"> 
<h1 align="center">𝘧𝘳𝘦𝘦𝘯𝘰𝘮-𝘱𝘺</h1>

<a href="https://github.com/Oreomeow/freenom-py/stargazers"><img src="https://img.shields.io/github/stars/Oreomeow/freenom-py?color=9cf&logo=Riseup&logoColor=9cf&style=for-the-badge" alt="GitHub stars"></a>
<a href="https://github.com/Oreomeow/freenom-py/network"><img src="https://img.shields.io/github/forks/Oreomeow/freenom-py?color=9cf&style=for-the-badge" alt="GitHub forks"></a>
<a href="https://t.me/joinchat/muGNhnaZglQ0N2Q1"><img src="https://img.shields.io/badge/talk-Telegram-9cf?logo=Telegram&style=for-the-badge" alt="Telegram"></a>
<a href="https://github.com/Oreomeow/freenom-py/issues"><img src="https://img.shields.io/github/issues/Oreomeow/freenom-py?color=yellow&style=for-the-badge" alt="GitHub issues"></a>
<a href="https://github.com/Oreomeow/freenom-py/commits"><img src="https://img.shields.io/github/last-commit/Oreomeow/freenom-py?color=orange&logo=GitHub&style=for-the-badge" alt="GitHub last commit"></a>

</div>
  

## 项目描述 🔑

Freenom 自动续期域名的脚本

## 项目部署 🥳

Python 运行环境
* Windows、Linux、青龙、elecV2P 等

## 使用说明 🕹

<h3 align="center">🌏 通用版</h3>

PC、VPS 等可直接运行，无通知变量

```sh
wget https://raw.githubusercontent.com/Oreomeow/freenom-py/main/FNplus.py
```

```sh
python3 FNplus.py -u USERNAME -p PASSWORD
```

`USERNAME` ：Freenom 用户名  
`PASSWORD` ：Freenom 密码

<h3 align="center">🐉 青龙邮件版 📧</h3>

1. 修改配置文件

```sh
## ql repo命令拉取脚本时需要拉取的文件后缀，直接写文件后缀名即可
RepoFileExtensions="js py ts html"
```

2. 添加定时拉取任务并运行

```
ql repo https://github.com/Oreomeow/freenom-py.git "FN_extend.py" "" "utils|templates"
```

3. 安装依赖

```sh
docker exec -it qinglong bash # 进入容器内
```

```sh
cd /ql/scripts
wget https://raw.githubusercontent.com/Oreomeow/freenom-py/main/requirements.txt -O requirements.txt
pip3 install -r requirements.txt
```

4. 添加环境变量 [示例](https://github.com/Oreomeow/freenom-py/issues/1#issuecomment-903344952)

* 可看[脚本注释](https://raw.githubusercontent.com/Oreomeow/freenom-py/main/FN_extend.py)
* 参考[下方表格](https://github.com/Oreomeow/freenom-py#%E9%82%AE%E4%BB%B6%E7%89%88-)

5. 运行一次 `FN_extend.py` 测试

<h3 align="center">🪁 elecV2P 邮件版 📧</h3>

TASK -> 添加单个任务 -> 修改名称、时间、任务 -> JSMANAGE -> store/cookie 常量储存管理填写[环境变量](https://github.com/Oreomeow/freenom-py#%E9%82%AE%E4%BB%B6%E7%89%88-)

名称：Freenom 续期

时间：cron定时 `25 7 */10 * *`

任务：

```
https://raw.githubusercontent.com/Oreomeow/freenom-py/main/FN_extend.js
```

<h3 align="center">🐉 青龙消息版 📱</h3>

1. 面板添加定时任务，定时随意，运行

```
ql raw https://raw.githubusercontent.com/Oreomeow/freenom-py/main/FNplus.py
```

2. 添加[环境变量](https://github.com/Oreomeow/freenom-py#%E6%B6%88%E6%81%AF%E7%89%88-) [示例](https://github.com/Oreomeow/freenom-py/issues/1#issuecomment-903344952)

3. 运行一次 `FNplus.py` 测试

<h3 align="center">🪁 elecV2P 消息版 📱</h3>

TASK -> 添加单个任务 -> 修改名称、时间、任务 -> JSMANAGE -> store/cookie 常量储存管理填写[环境变量](https://github.com/Oreomeow/freenom-py#%E6%B6%88%E6%81%AF%E7%89%88-)

名称：Freenom 续期

时间：cron定时 `25 7 */10 * *`

任务：

```
https://raw.githubusercontent.com/Oreomeow/freenom-py/main/FNplus.js
```

## 环境变量 🍒

### 邮件版 📧

| 变量 / key | 描述 |  示例 / value |
| --- | --- |  --- |
| FN_ID | Freenom 用户名 | 1234567890@gmail.com |
| FN_PW | Freenom 密码 | 12345678 | 
| MAIL_USER | 发件人邮箱用户名 |  address@vip.qq.com 或 123456@qq.com | 
| MAIL_ADDRESS | 发件人邮箱地址 | address@vip.qq.com 或 123456@qq.com |
| MAIL_PW | 发件人邮箱授权码 | xxxxxxxxxxxxxxxx 看下方链接 |
| MAIL_HOST | 发件人邮箱服务器 | smtp.qq.com 不填默认为这个 |
| MAIL_PORT | 邮箱服务器端口 |  465 不填默认为这个 |
| MAIL_TO | 收件人邮箱可与发件人相同 | address@vip.qq.com 或 123456@qq.com |

* 填写总参考

> [如何设置POP3/SMTP的SSL加密方式？](https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=369)

### 消息版 📱

| 变量 / key | 描述 | 参考 / value |
| --- | --- |  --- |
| FN_ID | Freenom 用户名，多账号空格隔开| 1234567890@gmail.com  9876543210@enayu.com |
| FN_PW | Freenom 密码，多账号空格隔开| 12345678 87654321 |
| BARK | bark 设备码 | BARK 推送[使用](https://github.com/Sitoi/dailycheckin/issues/29)，填写 URL 即可，例如： `https://api.day.app/DxHcxxxxxRxxxxxxcm/` |
| PUSH_KEY | Server 酱 | server 酱推送[官方文档](https://sc.ftqq.com/3.version)，填写 `SCKEY` 代码即可
| TG_BOT_TOKEN | tg 机器人 | 申请 [@BotFather](https://t.me/BotFather) 的 Token，如 `10xxx4:AAFcqxxxxgER5uw` |
| TG_USER_ID | tg 机器人 | 给 [@getidsbot](https://t.me/getidsbot) 发送 /start 获取到的纯数字 ID，如 `1434078534` |
| TG_PROXY_IP | * tg 机器人代理 IP 地址 | 代理类型为 http，比如您代理是 `http://127.0.0.1:1080` ，则填写 `127.0.0.1` ，有密码例子: `username:password@127.0.0.1` |
| TG_PROXY_PORT | * tg 机器人代理端口 | 代理端口号，代理类型为 http，比如您代理是 `http://127.0.0.1:1080` ，则填写 `1080` |
| DD_BOT_TOKEN | 钉钉机器人 | 钉钉推送[官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq)，只需 `https://oapi.dingtalk.com/robot/send?access_token=XXX` 等于符号后面的 `XXX` |
| DD_BOT_SECRET | 钉钉机器人 | 钉钉推送[官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq)密钥，机器人安全设置页面，加签一栏下面显示的 `SEC` 开头的字符串, 注: 填写了 `DD_BOT_TOKEN` 和 `DD_BOT_SECRET` ，钉钉机器人安全设置只需勾选加签即可，其他选项不要勾选 |
| QYWX_AM | 企业微信应用 | [参考文档](http://note.youdao.com/s/HMiudGkb)，依次填入 corpid, corpsecret, touser(注：多个成员ID使用 \| 隔开), agentid, media_id(选填，不填默认文本消息类型) |

*\* 表示选填*

* 调用模块

> [notify.py](https://raw.githubusercontent.com/whyour/qinglong/master/sample/notify.py)

## 查看通知 📮

不出意外会收到一封关于域名续期的邮件或者 tg 等通知消息

## 写在最后 🔚

核心代码见 `utils/freenom.py`

此项目核心接口参考 [Freenom-PHP](https://github.com/luolongfei/freenom) 

**感谢不限于以下开发者**

[@𝘴𝘩𝘶𝘢𝘪93](https://github.com/shuai93)

[@𝘭𝘶𝘰𝘭𝘰𝘯𝘨𝘧𝘦𝘪](https://github.com/luolongfei)
