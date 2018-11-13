# 概述
使用flask-restful框架构建API，并使用了flask-login作为登陆认证

# 用到的依赖
- [x] flask
- [x] flask-login 
- [x] flask-sqlalchemy
- [x] flask-migrate 
- [x] pymysql

# 项目结构
```
使用蓝图进行分割项目，结合了flask-restful+flask-login 编写restful-api
```
# 代码
[如何在蓝图中使用restful框架](app/auth/__init__.py)
[如何在flask中进行集成](app/__init__.py)

# 下一步
- [ ] 错误处理
- [ ] 返回格式的统一
- [ ] 其他方式认证
- [ ] 多重认证
- [ ] 安全
