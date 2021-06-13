<template>
  <div>
    <!-- 面包屑导航区 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/center' }">个人页</el-breadcrumb-item>
      <el-breadcrumb-item>运动分享</el-breadcrumb-item>
    </el-breadcrumb>
    <el-row :gutter="20">
      <el-col :span="6">
        <el-input placeholder="请输入内容" v-model="search_form.content" clearable @clear="get_share_list">
          <el-button slot="append" icon="el-icon-search" @click="get_share_list"></el-button>
        </el-input>
      </el-col>
      <el-col :span="4">
        <el-button type="primary" @click="add_dialog_visible = true">添加我的分享</el-button>
      </el-col>
      <el-col v-for="(item) in share_list" :key="item.share_id">
        <el-card shadow="hover">
          <div slot="header" class="clearfix">
            <span>{{item.share.name}}</span>
          </div>
          <div>
            <span>{{item.share.message}}</span>
            <el-divider v-if="item.comment"></el-divider>
            <div v-for="(sub_item) in item.comment" :key="sub_item.comment_id">
              <span class="comment">{{sub_item.name}}: {{sub_item.content}}</span>
            </div>
            <div class="bottom clearfix">
              <el-button size="small" type="warning" icon="el-icon-star-off" @click="add_liking(item.share.share_id)">{{item.share.liking}}</el-button>
              <el-button size="small" type="success" icon="el-icon-chat-dot-square" @click="add_comment(item.share.share_id)"></el-button>
              <el-button size="small" type="primary" icon="el-icon-edit" v-if="item.share.user_id==user_id" @click="show_edit_dialog(item.share.share_id)"></el-button>
              <el-button size="small" type="danger" icon="el-icon-delete" v-if="item.share.user_id==user_id" @click="remove_share(item.share.share_id)"></el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
    <!-- 添加记录的对话框 -->
    <el-dialog title="添加我的分享" :visible.sync="add_dialog_visible" width="50%" @close="add_dialog_close">
      <el-form :model="add_share_form" ref="add_share_form_ref" :rules="add_share_form_rules" label-width="100px">
        <el-form-item label="分享" prop="message">
          <el-input type="textarea" v-model="add_share_form.message"></el-input>
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
        <el-form-item label="分享" prop="message">
          <el-input type="textarea" v-model="edit_share_form.message"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="edit_dialog_visible = false">取消</el-button>
        <el-button type="primary" @click="edit_share">确定</el-button>
      </span>
    </el-dialog>
    <!-- 评论的对话框 -->
    <el-dialog title="发表评论" :visible.sync="comment_dialog_visible" width="50%" @close="comment_dialog_close">
      <el-form :model="comment_form" ref="comment_form_ref" :rules="comment_form_rules" label-width="100px">
        <el-form-item label="评论" prop="message">
          <el-input type="textarea" v-model="comment_form.message"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="comment_dialog_visible = false">取消</el-button>
        <el-button type="primary" @click="get_comment">确定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data () {
    return {
      user_id: window.sessionStorage.getItem('user_id'),
      search_form: {
        content: ''
      },
      share_list: [],
      add_dialog_visible: false,
      add_share_form: {
        account: window.sessionStorage.getItem('account'),
        message: ''
      },
      add_share_form_rules: {
        message: [
          { required: true, message: '请输入分享', trigger: 'blur' },
          { min: 10, max: 50, message: '分享的长度在10~50个字', trigger: 'blur' }
        ]
      },
      edit_dialog_visible: false,
      edit_share_form: {},
      edit_share_form_rules: {
        message: [
          { required: true, message: '请输入分享', trigger: 'blur' },
          { min: 10, max: 50, message: '分享的长度在10~50个字', trigger: 'blur' }
        ]
      },
      comment_dialog_visible: false,
      comment_form: {
        share_id: '',
        account: window.sessionStorage.getItem('account'),
        message: ''
      },
      comment_form_rules: {
        message: [
          { required: true, message: '请输入评论', trigger: 'blur' },
          { min: 1, max: 50, message: '评论的长度在1~50个字', trigger: 'blur' }
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
    async add_comment (id) {
      this.comment_dialog_visible = true
      this.comment_form.share_id = id
    },
    async get_comment () {
      const { data: res } = await this.$http.post('add_comment', this.comment_form)
      console.log(res)
      if (res.code !== 200) return this.$message.error(res.msg)
      this.$message.success(res.msg)
      this.comment_dialog_visible = false
      this.get_share_list()
    },
    comment_dialog_close () {
      this.$refs.comment_form_ref.resetFields()
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
  .comment {
    color: blue;
    font-size: 10px;
  }
</style>
