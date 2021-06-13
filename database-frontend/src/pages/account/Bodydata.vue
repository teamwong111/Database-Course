<template>
  <div>
    <!-- 面包屑导航区 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/center' }">个人页</el-breadcrumb-item>
      <el-breadcrumb-item>健康数据</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 卡片视图 -->
    <el-card>
      <!-- 添加 -->
      <el-row :gutter="20">
        <el-col :span="4">
          <el-button type="primary" @click="add_dialog_visible = true">添加健康数据</el-button>
        </el-col>
      </el-row>
      <!-- 记录列表区域 -->
      <el-table :data="bodydata_list" border stripe>
        <!-- stripe: 斑马条纹 border：边框-->
        <el-table-column type="index" label="#"></el-table-column>
        <el-table-column prop="height" label="身高(cm)"></el-table-column>
        <el-table-column prop="weight" label="体重(kg)"></el-table-column>
        <el-table-column prop="bmi" label="BMI"></el-table-column>
        <el-table-column prop="heart_rate" label="心率"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="primary" icon="el-icon-edit" size="mini" @click="show_edit_dialog(scope.row.bodydata_id)"></el-button>
            <el-button type="danger" icon="el-icon-delete" size="mini" @click="remove_bodydata(scope.row.bodydata_id)" ></el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <!-- 添加记录的对话框 -->
    <el-dialog title="添加健康数据" :visible.sync="add_dialog_visible" width="50%" @close="add_dialog_close">
      <el-form :model="add_bodydata_form" ref="add_bodydata_form_ref" :rules="add_bodydata_form_rules" label-width="100px">
        <el-form-item label="身高(cm)" prop="height">
          <el-input v-model="add_bodydata_form.height"></el-input>
        </el-form-item>
        <el-form-item label="体重(kg)" prop="weight">
          <el-input v-model="add_bodydata_form.weight"></el-input>
        </el-form-item>
        <el-form-item label="BMI" prop="bmi">
          <el-input v-model="add_bodydata_form.bmi"></el-input>
        </el-form-item>
        <el-form-item label="心率" prop="heart_rate">
          <el-input v-model="add_bodydata_form.heart_rate"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="add_dialog_visible = false">取消</el-button>
        <el-button type="primary" @click="add_bodydata">确定</el-button>
      </span>
    </el-dialog>

    <!-- 修改记录的对话框 -->
    <el-dialog title="修改记录信息" :visible.sync="edit_dialog_visible" width="50%" @close="edit_dialog_close">
      <el-form :model="edit_bodydata_form" ref="edit_bodydata_form_ref" :rules="edit_bodydata_form_rules" label-width="100px">
        <el-form-item label="身高(cm)" prop="height">
          <el-input v-model="edit_bodydata_form.height"></el-input>
        </el-form-item>
        <el-form-item label="体重(kg)" prop="weight">
          <el-input v-model="edit_bodydata_form.weight"></el-input>
        </el-form-item>
        <el-form-item label="BMI" prop="bmi">
          <el-input v-model="edit_bodydata_form.bmi"></el-input>
        </el-form-item>
        <el-form-item label="心率" prop="heart_rate">
          <el-input v-model="edit_bodydata_form.heart_rate"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="edit_dialog_visible = false">取消</el-button>
        <el-button type="primary" @click="edit_bodydata">确定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data () {
    return {
      bodydata_list: [],
      add_dialog_visible: false,
      add_bodydata_form: {
        account: window.sessionStorage.getItem('account'),
        height: '',
        weight: ''
      },
      add_bodydata_form_rules: {
        height: [
          { required: true, message: '请输入身高', trigger: 'blur' },
          { min: 1, max: 5, message: '身高的长度在1～5个字', trigger: 'blur' }
        ],
        weight: [
          { required: true, message: '请输入体重', trigger: 'blur' },
          { min: 1, max: 5, message: '体重的长度在1～5个字', trigger: 'blur' }
        ],
        bmi: [
          { required: true, message: '请输入BMI', trigger: 'blur' },
          { min: 1, max: 5, message: 'BMI的长度在1～5个字', trigger: 'blur' }
        ],
        heart_rate: [
          { required: true, message: '请输入心率', trigger: 'blur' },
          { min: 1, max: 5, message: '心率的长度在1～5个字', trigger: 'blur' }
        ]
      },
      edit_dialog_visible: false,
      edit_bodydata_form: {},
      edit_bodydata_form_rules: {
        type: [
          { required: true, message: '请输入身高', trigger: 'blur' },
          { min: 1, max: 5, message: '身高的长度在1～5个字', trigger: 'blur' }
        ],
        weight: [
          { required: true, message: '请输入体重', trigger: 'blur' },
          { min: 1, max: 5, message: '体重的长度在1～5个字', trigger: 'blur' }
        ],
        bmi: [
          { required: true, message: '请输入BMI', trigger: 'blur' },
          { min: 1, max: 5, message: 'BMI的长度在1～5个字', trigger: 'blur' }
        ],
        heart_rate: [
          { required: true, message: '请输入心率', trigger: 'blur' },
          { min: 1, max: 5, message: '心率的长度在1～5个字', trigger: 'blur' }
        ]
      }
    }
  },
  created () {
    this.get_bodydata_list()
  },
  methods: {
    async get_bodydata_list () {
      const { data: res } = await this.$http.post('all_bodydata', { account: window.sessionStorage.getItem('account') })
      console.log(res)
      if (res.code !== 200) return this.$message.error(res.msg)
      this.$message.success(res.msg)
      this.bodydata_list = res.data
    },
    add_dialog_close () {
      this.$refs.add_bodydata_form_ref.resetFields()
    },
    add_bodydata () {
      this.$refs.add_bodydata_form_ref.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.post('add_bodydata', this.add_bodydata_form)
        if (res.code !== 200) return this.$message.error(res.msg)
        this.$message.success(res.msg)
        this.add_dialog_visible = false
        this.get_bodydata_list()
      })
    },
    async show_edit_dialog (id) {
      const { data: res } = await this.$http.post('single_bodydata', { bodydata_id: id, account: window.sessionStorage.getItem('account') })
      console.log(res)
      if (res.code !== 200) return this.$message.error(res.msg)
      this.$message.success(res.msg)
      this.edit_bodydata_form = res.data[0]
      this.edit_dialog_visible = true
    },
    edit_dialog_close () {
      this.$refs.edit_bodydata_form_ref.resetFields()
    },
    edit_bodydata () {
      this.$refs.edit_bodydata_form_ref.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.post('modify_bodydata', this.edit_bodydata_form)
        console.log(res)
        if (res.code !== 200) return this.$message.error(res.msg)
        this.$message.success(res.msg)
        this.edit_dialog_visible = false
        this.get_bodydata_list()
      })
    },
    async remove_bodydata (id) {
      const result = await this.$confirm(
        '此操作将永久删除该记录, 是否继续?',
        '提示',
        {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }
      ).catch(err => err)
      if (result !== 'confirm') {
        return this.$message.info('取消删除')
      }
      const { data: res } = await this.$http.post('del_bodydata', { bodydata_id: id })
      console.log(res)
      if (res.code !== 200) return this.$message.error(res.msg)
      this.$message.success(res.msg)
      this.get_bodydata_list()
    }
  }
}
</script>

<style lang="less" scoped>
</style>
