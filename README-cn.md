# Database-Course

这是我在同济大学数据库课程（2021春）的大作业

---

## 目录
- [简介](#简介)
- [项目目录结构](#项目目录结构)
- [运行](#运行)
- [维护者](#维护者)
- [License](#License)

---

## 简介
本仓库为包含同济大学2021年春数据库课程的大作业，一个运动健康管理系统，其技术栈如下：
1. 后端：Flask
2. 前端：Vue+Element UI
3. 数据库：SQLite

其功能如下：
1. 用户管理
2. 健康数据管理
3. 运动计划管理
4. 运动记录管理
5. 运动分享
6. 分享评论

---

## 项目目录结构
```bash
.
│
├─database-backend
│  │  app.py
│  │  requirements.txt
│  │
│  ├─account_manage
│  │  │  account_models.py
│  │  │  bodydata.py
│  │  │  user.py
│  │  └─__init__.py
│  │
│  ├─config
│  │  │  config.py
│  │  │  data.sqlite
│  │  └─__init__.py
│  │
│  ├─db_manage
│  │  │  sql.py
│  │  └─__init__.py
│  │
│  ├─share_manage
│  │  │  share.py
│  │  │  share_models.py
│  │  └─__init__.py
│  │
│  ├─sports_manage
│     │  plan.py
│     │  record.py
│     │  sports_models.py
│     └─__init__.py
│  
│
└─database-frontend
    │
    └─src
        │  App.vue
        │  main-dev.js
        │  main-prod.js
        │
        ├─components
        │      Home.vue
        │      Stat.vue
        │
        ├─pages
        │  ├─account
        │  │      Bodydata.vue
        │  │      Center.vue
        │  │      Modifypassword.vue
        │  │
        │  ├─plan
        │  │      Plan.vue
        │  │
        │  ├─record
        │  │      Record.vue
        │  │
        │  ├─share
        │  │      Allshare.vue
        │  │
        │  └─user
        │          Login.vue
        │          Regist.vue
        │
        ├─plugins
        │      element.js
        │
        └─router
                index.js
```

---

## 运行
- 操作系统：Windows10
- 前端：
    ```bash
    yarn install	//安装依赖
    yarn run serve	//以开发模式运行
    ```
- 后端:
    ```bash
    pip install requirements.txt	//安装python包，如有缺失请按照提示安装其他包
    python app.py					//以Debug模式运行
    ```

---

## 维护者
该仓库目前的维护者为https://github.com/teamwong111

如有侵权或其他问题请通过邮件联系wungjz1@gmail.com

---

## License
[MIT](https://github.com/teamwong111/Compiling-Principles-Course/blob/main/LICENSE)

---