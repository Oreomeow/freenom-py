// @grant nodejs
console.log('⏳ 初始化安装推送模块中......');
$exec('wget https://raw.githubusercontent.com/whyour/qinglong/master/sample/notify.py notify.py', {
    cwd: './script/Shell',
    timeout: 0,
    cb(data, error) {
        error ? console.error(error) : console.log(data);
    },
});
console.log('⏳ 开始执行 FNplus.py');
$exec('python3 https://raw.githubusercontent.com/Oreomeow/freenom-py/main/FNplus.py', {
    cwd: './script/Shell',
    timeout: 0,
    env: {
        FN_ID: $store.get('FN_ID', 'string'), // Freenom 用户名
        FN_PW: $store.get('FN_PW', 'string'), // Freenom 密码
        BARK: $store.get('BARK', 'string'), // bark IP 或设备码，例：https://api.day.app/xxxxxx
        DD_BOT_SECRET: $store.get('DD_BOT_SECRET', 'string'), // 钉钉机器人的 DD_BOT_SECRET
        DD_BOT_TOKEN: $store.get('DD_BOT_TOKEN', 'string'), // 钉钉机器人的 DD_BOT_TOKEN
        PUSH_KEY: $store.get('PUSH_KEY', 'string'), // server 酱的 PUSH_KEY，兼容旧版与 Turbo 版
        PUSH_PLUS_TOKEN: $store.get('PUSH_PLUS_TOKEN', 'string'), // push+ 微信推送的用户令牌
        QYWX_AM: $store.get('QYWX_AM', 'string'), // 企业微信应用的 QYWX_AM，参考 http://note.youdao.com/s/HMiudGkb，依次填入 corpid, corpsecret, touser(注：多个成员ID使用 | 隔开), agentid, media_id(选填，不填默认文本消息类型)
        TG_BOT_TOKEN: $store.get('TG_BOT_TOKEN', 'string'), // tg 机器人的 TG_BOT_TOKEN
        TG_USER_ID: $store.get('TG_USER_ID', 'string'), // tg 机器人的 TG_USER_ID
        TG_PROXY_IP: $store.get('TG_PROXY_HOST', 'string'), // tg 机器人的 TG_PROXY_IP，例：127.0.0.1，可不填
        TG_PROXY_PORT: $store.get('TG_PROXY_PORT', 'string'), // tg 机器人的 TG_PROXY_PORT，例：1080，可不填
    },
    cb(data, error) {
        error ? console.error(error) : console.log(data);
    },
});
