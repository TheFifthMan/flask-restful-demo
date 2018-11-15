# 概述
使用flask写API，并且使用token做为认证

# restful API
唯一的资源路径
自描述消息
统一的消息交换形式
统一的内容类型

# 逻辑
1. 生成token以及token的过期时间
2. 存入数据库
3. 设置token回收的方法
4. 生成token的链接
5. delete token的链接
6. 在[authorization](app/authorization.py)里面设置认证的方式。实现逻辑就是使用basic auth 去访问生成token的链接，然后取得token 去访问其他私密资源。

# 总结
这里只是简单的使用token，一个token，全部的资源都可以使用，显然不合理，但是在这里我们没有做任何限制。这里就有一个漏洞，如果我也有权限登陆，我可以拿我的token去访问你的资源，就造成了越权攻击. 合理的方式是我们还需要检验这个token是否有权限检查相关的资源。







