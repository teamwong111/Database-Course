<template>
  <div class="regist_container">
    <div class="regist_box">
      <!-- 头像区 -->
      <div class="avatar_box">
        <img src="../../assets/logo.png" alt="avatar" />
      </div>
      <!-- 登录表单 -->
      <div>
        <el-form ref="regist_form_ref" :model="regist_form" :rules="regist_form_rules" label-width="80px" class="regist_form">
          <el-form-item label="用户名" prop="name">
            <el-input v-model="regist_form.name" prefix-icon="iconfont icon-user"></el-input>
          </el-form-item>
          <el-form-item label="邮箱" prop="account">
            <el-input v-model="regist_form.account" prefix-icon="iconfont icon-user"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password1">
            <el-input v-model="regist_form.password1" type="password" prefix-icon="iconfont icon-3702mima"></el-input>
          </el-form-item>
          <el-form-item label="确认密码" prop="password2">
            <el-input v-model="regist_form.password2" type="password" prefix-icon="iconfont icon-3702mima"></el-input>
          </el-form-item>
          <el-form-item class="btns">
            <el-button type="primary" @click="regist">注册</el-button>
            <el-button type="info" @click="reset_regist_form">重置</el-button>
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
      regist_form: {
        name: 'wjz',
        account: '841713301@qq.com',
        password1: '123456',
        password2: '123456'
      },
      // 表单验证
      regist_form_rules: {
        name: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 2, max: 20, message: '长度在2到20个字符', trigger: 'blur' }
        ],
        account: [
          { required: true, message: '请输入邮箱', trigger: 'blur' },
          { min: 2, max: 20, message: '长度在2到20个字符', trigger: 'blur' }
        ],
        password1: [
          { required: true, message: '请输入用户密码', trigger: 'blur' },
          { min: 6, max: 18, message: '长度在6到18个字符', trigger: 'blur' }
        ],
        password2: [
          { required: true, message: '请输入用户密码', trigger: 'blur' },
          { min: 6, max: 18, message: '长度在6到18个字符', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    reset_regist_form () {
      this.$refs.regist_form_ref.resetFields()
    },
    regist () {
      this.$refs.regist_form_ref.validate(async valid => {
        if (!valid) return false
        const { data: res } = await this.$http.post('regist', this.regist_form)
        console.log(res)
        if (res.code !== 200) return this.$message.error(res.msg)
        this.$message.success(res.msg)
        this.$router.push('/login')
      })
    }
  }
}
</script>

<style lang="less" scoped>
.regist_container {
  background-color: #2b4b6b;
  height: 100%;
}
.regist_box {
  width: 500px;
  height: 460px;
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
.regist_form {
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
