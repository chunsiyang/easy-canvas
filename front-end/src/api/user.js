import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/login',
    method: 'post',
    data
  })
}

export function signUp(data) {
  return request({
    url: '/signup',
    method: 'post',
    data
  })
}


export function getInfo() {
  return request({
    url: '/user/info',
    method: 'get'
  })
}

export function testCanvas(data) {
  return request({
    url: '/user/canvas/test',
    method: 'post',
    data
  })
}

export function logout() {
  return request({
    url: '/user/logout',
    method: 'get'
  })
}

export function updateUser(data) {
  return request({
    url: '/user',
    method: 'post',
    data
  })
}

export function delUser(username) {
  return request({
    url: '/user/del/' + username,
    method: 'post'
  })
}

export function getAllUserInfo() {
  return request({
    url: '/setting/user/all',
    method: 'get'
  })
}
