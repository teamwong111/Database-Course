<template>
  <div class="page-header-index-wide page-header-wrapper-grid-content-main">
    <el-row :gutter="24">
      <el-col :md="24" :lg="7">
        <el-card style="width:100%" :bordered="false">
          <div class="account-center-avatarHolder" v-if="info[0]">
            <div class="avatar">
              <img :src=info[0].portrait>
            </div>
            <el-divider></el-divider>
            <div class="account">{{info[0].account}}</div>
            <el-divider></el-divider>
            <div class="account-center-detail">
              <div class="username">个人信息</div>
              <p>
                <i class="title"></i>用户名：{{info[0].name}}
              </p>
              <p>
                <i class="group"></i>密码：******
              </p>
            </div>
            <el-divider></el-divider>
            <div class="account-center-detail" v-if="info[1]">
              <div class="username">体质数据</div>
              <p>
                <i class="title"></i>身高：{{info[1].height}}cm
              </p>
              <p>
                <i class="group"></i>体重：{{info[1].weight}}kg
              </p>
              <p>
                <i class="group"></i>BMI：{{info[1].bmi}}
              </p>
              <p>
                <i class="group"></i>心率：{{info[1].heart_rate}}
              </p>
            </div>
          </div>
        </el-card>
      </el-col>
      <el-col :md="24" :lg="17">
        <el-card style="width:100%" :bordered="false">
          <stat></stat>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Stat from '../../components/Stat'
export default {
  components: {
    Stat
  },
  data () {
    return {
      info_form: {
        account: window.sessionStorage.getItem('account')
      },
      info: []
    }
  },
  created () {
    this.get_info()
  },
  methods: {
    async get_info () {
      const { data: res } = await this.$http.post('get_info', this.info_form)
      console.log(res)
      if (res.code !== 200) return this.$message.error(res.msg)
      this.$message.success(res.msg)
      this.info = res.data
      console.log(this.info)
    }
  }
}
</script>

<style lang="less" scoped>
.page-header-wrapper-grid-content-main {
  width: 100%;
  height: 100%;
  min-height: 100%;
  transition: 0.3s;

  .account-center-avatarHolder {
    text-align: center;
    margin-bottom: 24px;

    & > .avatar {
      margin: 0 auto;
      width: 104px;
      height: 104px;
      margin-bottom: 20px;
      border-radius: 50%;
      overflow: hidden;
      img {
        height: 100%;
        width: 100%;
      }
    }

    .username {
      color: rgba(0, 0, 0, 0.85);
      font-size: 20px;
      line-height: 28px;
      font-weight: 500;
      margin-bottom: 4px;
    }
  }

  .account-center-detail {
    p {
      text-align: center;
      margin-bottom: 8px;
      position: relative;
    }

    i {
      text-align: center;
      position: absolute;
      height: 14px;
      width: 14px;
      left: 0;
      top: 4px;
    }

    .title {
      background-position: 0 0;
    }
    .group {
      background-position: 0 -22px;
    }
    .address {
      background-position: 0 -44px;
    }
  }

  .account-center-tags {
    .ant-tag {
      margin-bottom: 8px;
    }
  }

  .account-center-team {
    .members {
      a {
        display: block;
        margin: 12px 0;
        line-height: 24px;
        height: 24px;
        .member {
          font-size: 14px;
          color: rgba(0, 0, 0, 0.65);
          line-height: 24px;
          max-width: 100px;
          vertical-align: top;
          margin-left: 12px;
          transition: all 0.3s;
          display: inline-block;
        }
        &:hover {
          span {
            color: #1890ff;
          }
        }
      }
    }
  }

  .tagsTitle,
  .teamTitle {
    font-weight: 500;
    color: rgba(0, 0, 0, 0.85);
    margin-bottom: 12px;
  }
}
</style>
