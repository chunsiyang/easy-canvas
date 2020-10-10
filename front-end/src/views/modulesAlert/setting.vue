<template>
  <div>
    <el-form ref="form" :model="data" label-width="160px">
      <el-form-item :label="$t('modulesAlert.enable')">
        <el-switch v-model="modulesAlertSetting.enable" />
      </el-form-item>
      <el-form-item :label="$t('modulesAlert.notificationMethod')">
        <el-radio-group v-model="modulesAlertSetting.notificationMethod">
          <el-radio label="canvas" />
          <el-radio label="email" />
        </el-radio-group>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">{{ $t('button.save') }}</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
import { getSetting, saveSetting } from '@/api/modulesAlert'

export default {
  name: 'Setting',
  data() {
    return {
      modulesAlertSetting: {
        notificationMethod: 'canvas'
      }
    }
  },
  computed: {},
  mounted() {
    new Promise((resolve, reject) => {
      getSetting().then(response => {
        this.modulesAlertSetting = response.data
        this.originalData = response.data
        if (this.modulesAlertSetting.notificationMethod === undefined) {
          this.modulesAlertSetting.notificationMethod = 'canvas'
        }
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },
  methods: {
    onSubmit() {
      new Promise((resolve, reject) => {
        saveSetting(this.modulesAlertSetting).then(response => {
          this.$message(this.$t('button.save') + '!')
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    }
  }
}
</script>

<style scoped>

</style>
