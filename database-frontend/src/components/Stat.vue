<template>
  <div>
    <el-row>
      <el-col :span="16">
         <div id="main" style="width: 900px; height:570px;"></div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import echarts from 'echarts'

export default {
  data () {
    return {
      data_stat: []
    }
  },
  created () {
    this.get_data_stat()
  },
  methods: {
    async get_data_stat () {
      const { data: res } = await this.$http.post('data_stat', { account: window.sessionStorage.getItem('account') })
      console.log(res)
      if (res.code !== 200) return this.$message.error(res.msg)
      this.$message.success(res.msg)
      this.data_stat = res.data
      var myChart = echarts.init(document.getElementById('main'))
      var option = {
        legend: {},
        tooltip: {},
        dataset: {
          source: this.data_stat
        },
        xAxis: { type: 'category' },
        yAxis: {},
        series: [
          { type: 'bar', smooth: true },
          { type: 'bar', smooth: true },
          { type: 'bar', smooth: true },
          { type: 'bar', smooth: true }
        ]
      }
      myChart.setOption(option)
    }
  }
}
</script>

<style>
div{
  margin: 0;
  padding: 0;
}
</style>
