<template>
  <div class="login_container">
    <div class="login_box">
      <!-- 头像区 -->
      <div class="avatar_box">
        <img src="../../assets/logo.png" alt="avatar" />
      </div>
      <!-- 登录表单 -->
      <div>
        <el-form ref="login_form_ref" :model="login_form" :rules="login_form_rules" label-width="60px" class="login_form">
          <el-form-item label="账号" prop="account">
            <el-input v-model="login_form.account" prefix-icon="iconfont icon-user"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input v-model="login_form.password" type="password" prefix-icon="iconfont icon-3702mima"></el-input>
          </el-form-item>
          <el-form-item class="btns">
            <el-button type="primary" @click="login">登录</el-button>
            <el-button type="primary" @click="to_regist">注册</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      login_form: {
        account: '841713301@qq.com',
        password: '123456'
      },
      // 表单验证
      login_form_rules: {
        account: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 2, max: 20, message: '长度在2到20个字符', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入用户密码', trigger: 'blur' },
          { min: 6, max: 18, message: '长度在6到18个字符', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    to_regist () {
      this.$router.push('/regist')
    },
    login () {
      this.$refs.login_form_ref.validate(async valid => {
        if (!valid) return false
        const { data: res } = await this.$http.post('login', this.login_form)
        console.log(res)
        if (res.code !== 200) return this.$message.error(res.msg)
        this.$message.success(res.msg)
        window.sessionStorage.setItem('account', res.data[0].account)
        window.sessionStorage.setItem('user_id', res.data[0].user_id)
        this.$router.push('/center')
      })
    }
  }
}
</script>

<style lang="less" scoped>
.login_container {
  background-color: #2b4b6b;
  height: 100%;
}
.login_box {
  width: 450px;
  height: 360px;
  background-color: #fff;
  border-radius: 3px;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  .avatar_box {
    width: 130px;
    height: 130px;
    border: 1px solid #eee;
    border-radius: 50%;
    padding: 10px;
    box-shadow: 0 0 10px #ddd;
    position: absolute;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #fff;
    img {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background-color: #eee;
    }
  }
}
.login_form {
  position: absolute;
  bottom: 60px;
  width: 100%;
  padding: 0 20px;
  box-sizing: border-box;
}
.btns {
  display: flex;
  justify-content: center;
}
.info {
  font-size: 13px;
  margin: 10px 15px;
}
</style>
