<template>
  <div class="password_container">
    <div class="password_box">
      <div>
        <el-form ref="password_form_ref" :model="password_form" :rules="password_form_rules" label-width="80px" class="password_form">
          <el-form-item label="旧密码" prop="password1">
            <el-input v-model="password_form.password1" type="password" prefix-icon="iconfont icon-3702mima"></el-input>
          </el-form-item>
          <el-form-item label="新密码" prop="password2">
            <el-input v-model="password_form.password2" type="password" prefix-icon="iconfont icon-3702mima"></el-input>
          </el-form-item>
          <el-form-item label="新密码" prop="password3">
            <el-input v-model="password_form.password3" type="password" prefix-icon="iconfont icon-3702mima"></el-input>
          </el-form-item>
          <el-form-item class="btns">
            <el-button type="primary" @click="modify_password">确定</el-button>
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
      password_form: {
        account: window.sessionStorage.getItem('account'),
        password1: '123456',
        password2: '123457',
        password3: '123457'
      },
      password_form_rules: {
        password1: [
          { required: true, message: '请输入用户密码', trigger: 'blur' },
          { min: 6, max: 18, message: '长度在6到18个字符', trigger: 'blur' }
        ],
        password2: [
          { required: true, message: '请输入用户密码', trigger: 'blur' },
          { min: 6, max: 18, message: '长度在6到18个字符', trigger: 'blur' }
        ],
        password3: [
          { required: true, message: '请输入用户密码', trigger: 'blur' },
          { min: 6, max: 18, message: '长度在6到18个字符', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    modify_password () {
      this.$refs.password_form_ref.validate(async valid => {
        if (!valid) return false
        const { data: res } = await this.$http.post('modify_password', this.password_form)
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
.password_container {
  background-color: #2b4b6b;
  height: 100%;
}
.password_box {
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
.password_form {
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
