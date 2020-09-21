import request from '@/utils/request'

export function getSetting() {
  return request({
    url: '/modulesalert/setting',
    method: 'get'
  })
}

export function saveSetting(data) {
  return request({
    url: '/modulesalert/setting',
    method: 'post',
    data
  })
}
