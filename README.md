# Database-Course

[中文文档](https://github.com/teamwong111/Database-Course/blob/main/README-cn.md)

It is my term porject repo of Compiling Principles Course(2021 spring) in Tongji University

---

## Contents
- [Introduction](#Introduction)
- [Structure](#Structure)
- [Running](#Running)
- [Defenders](#Defenders)
- [License](#License)

---

## Introduction
This repo contain the term project of Tongji University's Database Course in 2021 spring. The tech stack is as follows:

1. backend：Flask
2. frontend：Vue+Element UI
3. database：SQLite

The features are as follows：

1. user management
2. health data management
3. sports plans management
4. sports records management
5. sports share management
6. comments to shares management

---

## Structure
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

## Running
- OS：Windows10

- Frontend：
    ```bash
    yarn install	//install dependency
    yarn run serve	//run in dev mode
    ```
- Backend:
    ```bash
    pip install requirements.txt	//install packages. If there is any missing, please follow the prompts
    python app.py					//run in debug mode

---

## Defenders
The repo is currently owned by https://github.com/teamwong111 maintain

If I have infringement or you have any questions, please contact me by email wungjz1@gmail.com

---

## License
[MIT](https://github.com/teamwong111/Database-Course/blob/main/LICENSE)

---