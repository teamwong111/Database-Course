<template>
  <el-container>
    <!-- 头部 -->
    <el-header>
      <div>
        <img src="../assets/logo.png" alt />
        <span>济动的心</span>
      </div>
      <el-button type="info" @click="logout">退出</el-button>
    </el-header>
    <!-- 主体 -->
    <el-container>
      <!-- 侧边栏 -->
      <el-aside :width="is_collapse ? '64px' : '200px'">
        <div class="toggle-button" @click="togle_collapse">|||</div>
        <el-menu unique-opened :collapse="is_collapse" :collapse-transition="false" router :default-active="active_path" background-color="#333744" text-color="#fff" active-text-color="#409FFF">
          <!-- 一级菜单  -->
          <el-submenu :index="item.id+''" v-for="item in menu_list" :key="item.id" >
            <!-- 一级菜单的模板区域 -->
            <template slot="title">
              <i :class="icon_list[item.id]"></i>
              <span>{{item.name}}</span>
            </template>
            <!-- 二级菜单 -->
            <el-menu-item :index="'/' + sub_item.path" v-for="sub_item in item.children" :key="sub_item.id" @click="save_navstate('/' + sub_item.path)">
              <!-- 导航开启路由模式：
                将index值作为导航路由 -->
              <!-- 二级菜单的模板区域 -->
              <template slot="title">
                <i class="el-icon-menu"></i>
                <span>{{ sub_item.name}}</span>
              </template>
            </el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <!-- 内容主体 -->
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      // 左侧菜单数据
      menu_list: [
        {
          id: 101,
          name: '运动管理',
          children: [
            {
              id: 102,
              name: '运动计划',
              path: 'plan'
            },
            {
              id: 103,
              name: '运动记录',
              path: 'record'
            }
          ]
        },
        {
          id: 104,
          name: '运动分享',
          children: [
            {
              id: 106,
              name: '分享空间',
              path: 'allshare'
            }
          ]
        },
        {
          id: 107,
          name: '个人页',
          children: [
            {
              id: 108,
              name: '个人中心',
              path: 'center'
            },
            {
              id: 109,
              name: '信息修改',
              path: 'modifypassword'
            },
            {
              id: 110,
              name: '健康数据',
              path: 'bodydata'
            }
          ]
        }
      ],
      icon_list: {
        '101': 'iconfont icon-shangpin',
        '102': 'iconfont icon-danju',
        '103': 'iconfont icon-tijikongjian',
        '104': 'iconfont icon-baobiao',
        '107': 'iconfont icon-user'
      },
      // 默认不折叠
      is_collapse: false,
      // 被激活导航地址
      active_path: ''
    }
  },
  created () {
    this.active_path = window.sessionStorage.getItem('active_path')
  },
  methods: {
    logout () {
      window.sessionStorage.clear()
      this.$router.push('/login')
    },
    // 菜单的折叠与展开
    togle_collapse () {
      this.is_collapse = !this.is_collapse
    },
    // 保存连接的激活地址
    save_navstate (path) {
      window.sessionStorage.setItem('active_path', path)
    }
  }
}
</script>

<style lang="less" scoped>
.el-container {
  height: 100%;
}
.el-header {
  background-color: #373f41;
  display: flex;
  justify-content: space-between;
  padding-left: 0;
  align-items: center;
  color: #fff;
  font-size: 20px;
  > div {
    display: flex;
    align-items: center;
    img {
      height: 40px;
    }
    span {
      margin-left: 15px;
    }
  }
}
.el-aside {
  background-color: #333744;

  .el-menu {
    border: none;
  }
}
.el-main {
  background-color: #eaedf1;
}
.iconfont{
  margin-right: 10px;
}
.toggle-button {
  background-color: #4A5064;
  font-size: 10px;
  line-height: 24px;
  color: #fff;
  text-align: center;
  letter-spacing: 0.2em;
  // 鼠标放上去变成小手
  cursor: pointer;
}
</style>
