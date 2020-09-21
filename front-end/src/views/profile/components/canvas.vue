<template>
  <div>
    <el-form>
      <el-form-item label="Canvas address">
        <el-input v-model="user.canvasAddress" />
      </el-form-item>
      <el-form-item label="Access Token">
        <el-input v-model="user.accessToken" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submit">{{ $t('button.save') }}</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import {getLanguage} from "@/lang";
import {generateToken, getInfo, updateUser} from "@/api/user";

export default {
  name: 'canvas',
  data() {
    return {
      user: {
        canvasAddress: '',
        accessToken: ''
      },
      token: ''
    }
  },
  methods: {
    submit() {
      new Promise((resolve, reject) => {
        updateUser({user_info: this.user}).then(response => {
          this.$message({
            message: this.$t('userManagement.saveSuccess'),
            type: 'success',
            duration: 5 * 1000
          })
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },
  },
  mounted() {
    new Promise((resolve, reject) => {
      getInfo().then(response => {
        this.user = response.data
        this.user.password = ''
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  }
}
</script>
