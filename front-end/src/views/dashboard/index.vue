<template>
  <div class="dashboard-container">
    <h1>Welcome to EASY-CANVAS</h1>
    <hr>
    <h4>What is EASY-CANVAS</h4>
    <p>
      EASY-CANVAS is a Canvas assistant app built for students who are using Canvas as their learning management system with the main goal of making your life easier by adding additional functions to Canvas.
    </p>
    <h4>How it works</h4>
    <p>EASY-CANVAS provide functions which are not original supported by Canvas. To achieve this EASY-CANVAS has to use your Canvas access token to communicate to your Canvas API server which means your access token must be store in the database of EASY-CANVAS to get it to work. What we could grantee is that your Canvas access token will be used and only used by EASY-CANVAS with no malicious intent. EASY-CANVAS is also an open-source project on Github and we are welcome for participation and supervision from the community.</p>
    <p> Our Github page is <a target="_blank" href="https://github.com/chunsiyang/easy-canvas" style="color: #4a9ff9"><u>https://github.com/chunsiyang/easy-canvas</u></a></p>
    <b style="color: red"> If this app helps you please star us on Github, your star will be the best encouragement for us</b>
    <h4>How to use EASY-CANVAS</h4>
    <p>First you need to generate your Canvas access token</p>
    <p>Please go to your Canvas Account -> Setting</p>
    <p>Click the + New Access Token button</p>
    <div style="align-content: center; width: 100%">
      <img src="../../../../img/token1.png" width="90%"/>
      <br>
      <p>Fill the purpose with a EAST-CANVAS and choose an expiration date. Please note that the shorter the expiration date, the higher the security, but once the access token expires, the access token needs to be refreshed.</p>
      <br>
      <img src="../../../../img/token2.png" width="60%"/>
      <br>
      <p>Click the Generate token button</p>
      <br>
      <img src="../../../../img/token3.png" width="60%"/>
      <br>
      <p>Now you have successful generate your Canvas access token, please fill it in the profile page on EASY-CANVAS, you also need to fill the Canvas address with your school Canvas address.</p>
      <br>
      <img src="../../../../img/profile.png" width="90%  "/>
      <br>
      <p>Now please enjoy the easy life with EASY-CANVAS.</p>
      <br>
    </div>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Dashboard',
  computed: {
    ...mapGetters([
      'name',
      'roles'
    ])
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
