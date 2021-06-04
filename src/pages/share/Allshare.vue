<template>
  <div>
    <el-row :gutter="20">
      <el-col :span="6">
        <el-input placeholder="请输入内容" v-model="search_form.content" clearable @clear="get_share_list">
          <el-button slot="append" icon="el-icon-search" @click="get_share_list"></el-button>
        </el-input>
      </el-col>
      <el-col :span="4">
        <el-button type="primary" @click="add_dialog_visible = true">添加我的分享</el-button>
      </el-col>
      <el-col v-for="(share) in share_list" :key="share.share_id">
        <el-card shadow="hover">
          <div slot="header" class="clearfix">
            <span>{{share.name}}</span>
          </div>
          <div>
            <span>{{share.message}}</span>
            <div class="bottom clearfix">
              <el-button size="small" type="primary" icon="el-icon-edit" @click="show_edit_dialog(share.share_id)"></el-button>
              <el-button size="small" type="danger" icon="el-icon-delete" @click="remove_share(share.share_id)"></el-button>
              <el-button size="small" type="warning" icon="el-icon-star-off" @click="add_liking(share.share_id)">{{share.liking}}</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
    <!-- 添加记录的对话框 -->
    <el-dialog title="添加运动记录" :visible.sync="add_dialog_visible" width="50%" @close="add_dialog_close">
      <el-form :model="add_share_form" ref="add_share_form_ref" :rules="add_share_form_rules" label-width="100px">
        <el-form-item label="类型" prop="type">
          <el-input v-model="add_share_form.type"></el-input>
        </el-form-item>
        <el-form-item label="时长(h)" prop="time_len">
          <el-input v-model="add_share_form.time_len"></el-input>
        </el-form-item>
        <el-form-item label="地点" prop="place">
          <el-input v-model="add_share_form.place"></el-input>
        </el-form-item>
        <el-form-item label="距离(km)" prop="len">
          <el-input v-model="add_share_form.len"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="add_dialog_visible = false">取消</el-button>
        <el-button type="primary" @click="add_share">确定</el-button>
      </span>
    </el-dialog>
    <!-- 修改记录的对话框 -->
    <el-dialog title="修改记录信息" :visible.sync="edit_dialog_visible" width="50%" @close="edit_dialog_close">
      <el-form :model="edit_share_form" ref="edit_share_form_ref" :rules="edit_share_form_rules" label-width="100px">
        <el-form-item label="类型" prop="type">
          <el-input v-model="edit_share_form.type"></el-input>
        </el-form-item>
        <el-form-item label="时长(h)" prop="time_len">
          <el-input v-model="edit_share_form.time_len"></el-input>
        </el-form-item>
        <el-form-item label="地点" prop="place">
          <el-input v-model="edit_share_form.place"></el-input>
        </el-form-item>
        <el-form-item label="距离(km)" prop="len">
          <el-input v-model="edit_share_form.len"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="edit_dialog_visible = false">取消</el-button>
        <el-button type="primary" @click="edit_share">确定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data () {
    return {
      search_form: {
        content: ''
      },
      share_list: [],
      add_dialog_visible: false,
      add_share_form: {
        account: window.sessionStorage.getItem('account'),
        type: '',
        time_len: ''
      },
      add_share_form_rules: {
        type: [
          { required: true, message: '请输入类型', trigger: 'blur' },
          { min: 1, max: 5, message: '类型的长度在1～5个字', trigger: 'blur' }
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
      edit_share_form: {},
      edit_share_form_rules: {
        type: [
          { required: true, message: '请输入类型', trigger: 'blur' },
          { min: 1, max: 5, message: '类型的长度在1～5个字', trigger: 'blur' }
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
    this.get_share_list()
  },
  methods: {
    async get_share_list () {
      const { data: res } = await this.$http.post('search_share', this.search_form)
      console.log(res)
      if (res.code !== 200) return this.$message.error(res.msg)
      this.$message.success(res.msg)
      this.share_list = res.data
    },
    add_dialog_close () {
      this.$refs.add_share_form_ref.resetFields()
    },
    add_share () {
      this.$refs.add_share_form_ref.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.post('add_share', this.add_share_form)
        console.log(res)
        if (res.code !== 200) return this.$message.error(res.msg)
        this.$message.success(res.msg)
        this.add_dialog_visible = false
        this.get_share_list()
      })
    },
    async add_liking (id) {
      const { data: res } = await this.$http.post('add_liking', { share_id: id, account: window.sessionStorage.getItem('account') })
      console.log(res)
      if (res.code !== 200) return this.$message.error(res.msg)
      this.$message.success(res.msg)
      this.get_share_list()
    },
    async show_edit_dialog (id) {
      const { data: res } = await this.$http.post('single_share', { share_id: id, account: window.sessionStorage.getItem('account') })
      console.log(res)
      if (res.code !== 200) return this.$message.error(res.msg)
      this.$message.success(res.msg)
      this.edit_share_form = res.data[0]
      this.edit_dialog_visible = true
    },
    edit_dialog_close () {
      this.$refs.edit_share_form_ref.resetFields()
    },
    edit_share () {
      this.$refs.edit_share_form_ref.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.post('modify_share', this.edit_share_form)
        console.log(res)
        if (res.code !== 200) return this.$message.error(res.msg)
        this.$message.success(res.msg)
        this.edit_dialog_visible = false
        this.get_share_list()
      })
    },
    async remove_share (id) {
      const confirmResult = await this.$confirm(
        '此操作将永久删除该分享, 是否继续?',
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
      const { data: res } = await this.$http.post('del_share', { share_id: id })
      console.log(res)
      if (res.code !== 200) return this.$message.error(res.msg)
      this.$message.success(res.msg)
      this.get_share_list()
    }
  }
}
</script>

<style>
  .time {
    font-size: 13px;
    color: #999;
  }
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }
  .button {
    padding: 0;
    float: right;
  }
  .image {
    width: 100%;
    display: block;
  }
  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  .clearfix:after {
      clear: both
  }
</style>
