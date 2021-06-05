<template>
  <div>
    <!-- 面包屑导航区 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/center' }">个人页</el-breadcrumb-item>
      <el-breadcrumb-item>运动计划</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 卡片视图 -->
    <el-card>
      <!-- 搜索 添加 -->
      <el-row :gutter="20">
        <el-col :span="6">
          <el-input placeholder="请输入内容" v-model="search_form.content" clearable @clear="get_plan_list">
            <el-button slot="append" icon="el-icon-search" @click="get_plan_list"></el-button>
          </el-input>
        </el-col>
        <el-col :span="4">
          <el-button type="primary" @click="add_dialog_visible = true">添加运动计划</el-button>
        </el-col>
      </el-row>
      <!-- 计划列表区域 -->
      <el-table :data="plan_list" border stripe>
        <el-table-column type="index" label="#"></el-table-column>
        <el-table-column prop="name" label="计划"></el-table-column>
        <el-table-column prop="frequency" label="运动频率(week)"></el-table-column>
        <el-table-column prop="sports_time" label="运动时长(h/week)"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="primary" icon="el-icon-edit" size="mini" @click="show_edit_dialog(scope.row.plan_id)"></el-button>
            <el-button type="danger" icon="el-icon-delete" size="mini" @click="remove_plan(scope.row.plan_id)"></el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
    <!-- 添加计划的对话框 -->
    <el-dialog title="添加运动计划" :visible.sync="add_dialog_visible" width="30%" @close="add_dialog_close">
      <el-form :model="add_plan_form" ref="add_plan_form_ref" :rules="add_plan_form_rules" label-width="150px">
        <el-form-item label="计划名" prop="name">
          <el-input v-model="add_plan_form.name"></el-input>
        </el-form-item>
        <el-form-item label="运动频率(week)" prop="frequency">
          <el-input v-model="add_plan_form.frequency"></el-input>
        </el-form-item>
        <el-form-item label="运动时长(h/week)" prop="sports_time">
          <el-input v-model="add_plan_form.sports_time"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="add_dialog_visible = false">取消</el-button>
        <el-button type="primary" @click="add_plan">确定</el-button>
      </span>
    </el-dialog>
    <!-- 修改计划的对话框 -->
    <el-dialog title="修改计划信息" :visible.sync="edit_dialog_visible" width="50%" @close="edit_dialog_close">
      <el-form :model="edit_plan_form" ref="edit_plan_form_ref" :rules="edit_plan_form_rules" label-width="150px">
        <el-form-item label="计划名" prop="name">
          <el-input v-model="edit_plan_form.name"></el-input>
        </el-form-item>
        <el-form-item label="运动频率(week)" prop="frequency">
          <el-input v-model="edit_plan_form.frequency"></el-input>
        </el-form-item>
        <el-form-item label="运动时长(h/week)" prop="sports_time">
          <el-input v-model="edit_plan_form.sports_time"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="edit_dialog_visible = false">取消</el-button>
        <el-button type="primary" @click="edit_plan">确定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data () {
    return {
      search_form: {
        account: window.sessionStorage.getItem('account'),
        content: ''
      },
      plan_list: [],
      add_dialog_visible: false,
      add_plan_form: {
        account: window.sessionStorage.getItem('account'),
        name: '',
        frequency: '',
        sports_time: ''
      },
      add_plan_form_rules: {
        name: [
          { required: true, message: '请输入计划名', trigger: 'blur' },
          { min: 1, max: 5, message: '计划名的长度在1～5个字', trigger: 'blur' }
        ],
        frequency: [
          { required: true, message: '请输入运动频率(week)', trigger: 'blur' },
          { min: 1, max: 5, message: '运动频率的长度在1～5个字', trigger: 'blur' }
        ],
        sports_time: [
          { required: true, message: '请输入运动时长(h/week)', trigger: 'blur' },
          { min: 1, max: 5, message: '运动时长的长度在1～5个字', trigger: 'blur' }
        ]
      },
      edit_dialog_visible: false,
      edit_plan_form: {},
      edit_plan_form_rules: {
        name: [
          { required: true, message: '请输入计划名', trigger: 'blur' },
          { min: 1, max: 5, message: '计划名的长度在1～5个字', trigger: 'blur' }
        ],
        frequency: [
          { required: true, message: '请输入运动频率(week)', trigger: 'blur' },
          { min: 1, max: 5, message: '运动频率的长度在1～5个字', trigger: 'blur' }
        ],
        sports_time: [
          { required: true, message: '请输入运动时长(h/week)', trigger: 'blur' },
          { min: 1, max: 5, message: '运动时长的长度在1～5个字', trigger: 'blur' }
        ]
      }
    }
  },
  created () {
    this.get_plan_list()
  },
  methods: {
    async get_plan_list () {
      const { data: res } = await this.$http.post('search_plan', this.search_form)
      console.log(res)
      if (res.code !== 200) return this.$message.error(res.msg)
      this.$message.success(res.msg)
      this.plan_list = res.data
    },
    add_dialog_close () {
      this.$refs.add_plan_form_ref.resetFields()
    },
    add_plan () {
      this.$refs.add_plan_form_ref.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.post('add_plan', this.add_plan_form)
        console.log(res)
        if (res.code !== 200) return this.$message.error(res.msg)
        this.$message.success(res.msg)
        this.add_dialog_visible = false
        this.get_plan_list()
      })
    },
    async show_edit_dialog (id) {
      const { data: res } = await this.$http.post('single_plan', { plan_id: id, account: '841713301@qq.com' })
      console.log(res)
      if (res.code !== 200) return this.$message.error(res.msg)
      this.$message.success(res.msg)
      this.edit_plan_form = res.data[0]
      console.log(res.data)
      this.edit_dialog_visible = true
    },
    edit_dialog_close () {
      this.$refs.edit_plan_form_ref.resetFields()
    },
    edit_plan () {
      this.$refs.edit_plan_form_ref.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.post('modify_plan', this.edit_plan_form)
        console.log(res)
        if (res.code !== 200) return this.$message.error(res.msg)
        this.$message.success(res.msg)
        this.edit_dialog_visible = false
        this.get_plan_list()
      })
    },
    async remove_plan (id) {
      const confirmResult = await this.$confirm(
        '此操作将永久删除该计划, 是否继续?',
        '提示',
        {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }
      ).catch(err => err)
      if (confirmResult !== 'confirm') {
        return this.$message.info('已取消删除')
      }
      const { data: res } = await this.$http.post('del_plan', { plan_id: id })
      console.log(res)
      if (res.code !== 200) return this.$message.error(res.msg)
      this.$message.success(res.msg)
      this.get_plan_list()
    }
  }
}
</script>

<style lang="less" scoped>
</style>
