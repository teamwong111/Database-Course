<template>
  <div>
    <!-- 面包屑导航区 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/center' }">个人页</el-breadcrumb-item>
      <el-breadcrumb-item>运动记录</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 卡片视图 -->
    <el-card>
      <!-- 搜索 添加 -->
      <el-row :gutter="20">
        <el-col :span="6">
          <el-input placeholder="请输入内容" v-model="search_form.content" clearable @clear="get_record_list">
            <el-button slot="append" icon="el-icon-search" @click="get_record_list"></el-button>
          </el-input>
        </el-col>
        <el-col :span="4">
          <el-button type="primary" @click="add_dialog_visible = true">添加运动记录</el-button>
        </el-col>
      </el-row>
      <!-- 记录列表区域 -->
      <el-table :data="record_list" border stripe>
        <el-table-column type="index" label="#"></el-table-column>
        <el-table-column prop="type" label="类型"></el-table-column>
        <el-table-column prop="time_len" label="时长(h)"></el-table-column>
        <el-table-column prop="place" label="地点"></el-table-column>
        <el-table-column prop="len" label="距离(km)"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="primary" icon="el-icon-edit" size="mini" @click="show_add_dialog(scope.row.record_id)"></el-button>
            <el-button type="danger" icon="el-icon-delete" size="mini" @click="remove_record(scope.row.record_id)"></el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
    <!-- 添加记录的对话框 -->
    <el-dialog title="添加运动记录" :visible.sync="add_dialog_visible" width="30%" @close="add_dialog_close">
      <el-form :model="add_record_form" ref="add_record_form_ref" :rules="add_record_form_rules" label-width="100px">
        <el-form-item label="类型" prop="type">
          <el-select v-model="add_record_form.type">
            <el-option label="篮球" value="篮球"></el-option>
            <el-option label="足球" value="足球"></el-option>
            <el-option label="跑步" value="跑步"></el-option>
            <el-option label="羽毛球" value="羽毛球"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="时长(h)" prop="time_len">
          <el-input v-model="add_record_form.time_len"></el-input>
        </el-form-item>
        <el-form-item label="地点" prop="place">
          <el-input v-model="add_record_form.place"></el-input>
        </el-form-item>
        <el-form-item label="距离(km)" prop="len">
          <el-input v-model="add_record_form.len"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="add_dialog_visible = false">取消</el-button>
        <el-button type="primary" @click="add_record">确定</el-button>
      </span>
    </el-dialog>
    <!-- 修改记录的对话框 -->
    <el-dialog title="修改记录信息" :visible.sync="edit_dialog_visible" width="30%" @close="edit_dialog_close">
      <el-form :model="edit_record_form" ref="edit_record_form_ref" :rules="edit_record_form_rules" label-width="100px">
        <el-form-item label="类型" prop="type">
          <el-select v-model="edit_record_form.type">
            <el-option label="篮球" value="篮球"></el-option>
            <el-option label="足球" value="足球"></el-option>
            <el-option label="跑步" value="跑步"></el-option>
            <el-option label="羽毛球" value="羽毛球"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="时长(h)" prop="time_len">
          <el-input v-model="edit_record_form.time_len"></el-input>
        </el-form-item>
        <el-form-item label="地点" prop="place">
          <el-input v-model="edit_record_form.place"></el-input>
        </el-form-item>
        <el-form-item label="距离(km)" prop="len">
          <el-input v-model="edit_record_form.len"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="edit_dialog_visible = false">取消</el-button>
        <el-button type="primary" @click="editrecord">确定</el-button>
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
      record_list: [],
      add_dialog_visible: false,
      add_record_form: {
        account: window.sessionStorage.getItem('account'),
        type: '',
        time_len: '',
        place: '',
        len: ''
      },
      add_record_form_rules: {
        type: [
          { required: true, message: '请输入类型', trigger: 'change' }
        ],
        time_len: [
          { required: true, message: '请输入时长', trigger: 'blur' },
          { min: 1, max: 5, message: '时长的长度在1～5个字', trigger: 'blur' }
        ],
        place: [
          { required: true, message: '请输入地点', trigger: 'blur' },
          { min: 1, max: 5, message: '地点的长度在1～5个字', trigger: 'blur' }
        ],
        len: [
          { required: true, message: '请输入距离', trigger: 'blur' },
          { min: 1, max: 5, message: '距离的长度在1～5个字', trigger: 'blur' }
        ]
      },
      edit_dialog_visible: false,
      edit_record_form: {},
      edit_record_form_rules: {
        type: [
          { required: true, message: '请输入类型', trigger: 'change' }
        ],
        time_len: [
          { required: true, message: '请输入时长', trigger: 'blur' },
          { min: 1, max: 5, message: '时长的长度在1～5个字', trigger: 'blur' }
        ],
        place: [
          { required: true, message: '请输入地点', trigger: 'blur' },
          { min: 1, max: 5, message: '地点的长度在1～5个字', trigger: 'blur' }
        ],
        len: [
          { required: true, message: '请输入距离', trigger: 'blur' },
          { min: 1, max: 5, message: '距离的长度在1～5个字', trigger: 'blur' }
        ]
      }
    }
  },
  created () {
    this.get_record_list()
  },
  methods: {
    async get_record_list () {
      const { data: res } = await this.$http.post('search_record', this.search_form)
      console.log(res)
      if (res.code !== 200) return this.$message.error(res.msg)
      this.$message.success(res.msg)
      this.record_list = res.data
    },
    add_dialog_close () {
      this.$refs.add_record_form_ref.resetFields()
    },
    add_record () {
      this.$refs.add_record_form_ref.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.post('add_record', this.add_record_form)
        console.log(res)
        if (res.code !== 200) return this.$message.error(res.msg)
        this.$message.success(res.msg)
        this.add_dialog_visible = false
        this.get_record_list()
      })
    },
    async show_add_dialog (id) {
      const { data: res } = await this.$http.post('single_record', { record_id: id, account: window.sessionStorage.getItem('account') })
      console.log(res)
      if (res.code !== 200) return this.$message.error(res.msg)
      this.$message.success(res.msg)
      this.edit_record_form = res.data[0]
      this.edit_dialog_visible = true
    },
    edit_dialog_close () {
      this.$refs.edit_record_form_ref.resetFields()
    },
    editrecord () {
      this.$refs.edit_record_form_ref.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.post('modify_record', this.edit_record_form)
        console.log(res)
        if (res.code !== 200) return this.$message.error(res.msg)
        this.$message.success(res.msg)
        this.edit_dialog_visible = false
        this.get_record_list()
      })
    },
    async remove_record (id) {
      const confirmResult = await this.$confirm(
        '此操作将永久删除该记录, 是否继续?',
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
      const { data: res } = await this.$http.post('del_record', { record_id: id })
      console.log(res)
      if (res.code !== 200) return this.$message.error(res.msg)
      this.$message.success(res.msg)
      this.get_record_list()
    }
  }
}
</script>

<style lang="less" scoped>
</style>
