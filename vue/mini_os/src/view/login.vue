
<template>
<!--  <div class="login-container">-->
<!--    <el-form ref="loginForm" :model="form" :rules="rules" label-width="100px" @submit.prevent="handleSubmit">-->
<!--      <el-form-item label="用户名" prop="username">-->
<!--        <el-input v-model="form.username" placeholder="请输入用户名"></el-input>-->
<!--      </el-form-item>-->
<!--      <el-form-item label="密码" prop="password">-->
<!--        <el-input type="password" v-model="form.password" placeholder="请输入密码"></el-input>-->
<!--      </el-form-item>-->
<!--      <el-form-item>-->
<!--        <el-button type="primary" @click="handleSubmit">登录</el-button>-->
<!--      </el-form-item>-->
<!--    </el-form>-->
<!--  </div>-->



  <div class="dowebok limiter">
    <div class="container-login100">
      <div class="wrap-login100 p-t-190 p-b-30">
        <form class="login100-form validate-form">
          <div class="login100-form-avatar">
            <img src="https://www.dowebok.com/demo/898/images/avatar-01.jpg" alt="AVATAR">
          </div>

          <span class="login100-form-title p-t-20 p-b-45">MiniOS</span>

          <div class="wrap-input100 validate-input m-b-10" data-validate="请输入用户名">
            <input class="input100" type="text" name="username" placeholder="用户名" autocomplete="off" v-model="form.username">
            <span class="focus-input100"></span>
            <span class="symbol-input100">
                <i class="fa fa-user"></i>
            </span>
          </div>

          <div class="wrap-input100 validate-input m-b-10" data-validate="请输入密码">
            <input class="input100" type="password" name="pass" placeholder="密码" v-model="form.password">
            <span class="focus-input100"></span>
            <span class="symbol-input100">
                        <i class="fa fa-lock"></i>
              </span>
          </div>

          <div class="container-login100-form-btn p-t-10">
            <button class="login100-form-btn"  @click="handleSubmit">登 录</button>
          </div>

          <div class="text-center w-full p-t-25 p-b-230">
            <a href="/forget.html" class="txt1">忘记密码？</a>
          </div>

          <div class="text-center w-full">
            <a class="txt1" href="/register.html">
              立即注册
              <i class="fa fa-long-arrow-right"></i>
            </a>
          </div>
        </form>
      </div>
    </div>
  </div>

</template>

<script setup>
import { useRouter } from 'vue-router';
import { ref, reactive, onMounted } from 'vue';
import {ElForm, ElFormItem, ElInput, ElButton, ElNotification} from 'element-plus';

const router = useRouter();

const rules = {
  username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
  password: [{ required: true, message: '请输入密码', trigger: 'blur' }],
};

const form = reactive({
  username: 'guest',
  password: 'guest',
});

// 登录函数
const handleSubmit = () => {
  localStorage.setItem('token', form.username + '||' + form.password)
  ElNotification({
    title: '系统提示',
    message: `登录成功`,
    type: 'success',
  })
  router.push({ name: 'Desk' })
}

onMounted(() => {
  const token = localStorage.getItem('token')
  // 判断是否已登录
  const isLoggedIn = token !== null && token !== ''
  // 如果存在用户登录状态
  if (isLoggedIn) {
    ElNotification({
      title: '系统提示',
      message: `账号已登录`,
      type: 'success',
    })
    router.push({ name: 'Desk' })
  } else {
    ElNotification({
      title: '系统提示',
      message: `请先登录账号`,
      type: 'error',
    })
  }
})
</script>

<style scoped>


* {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
}

body, html {
  height: 100%;
  font-family: Montserrat-Regular, sans-serif;
}

/*---------------------------------------------*/
a {
  font-family: Montserrat-Regular;
  font-size: 14px;
  line-height: 1.7;
  color: #666666;
  margin: 0px;
  transition: all 0.4s;
  -webkit-transition: all 0.4s;
  -o-transition: all 0.4s;
  -moz-transition: all 0.4s;
}

a:focus {
  outline: none !important;
}

a:hover {
  text-decoration: none;
  color: #fff;
}

/*---------------------------------------------*/
h1,h2,h3,h4,h5,h6 {
  margin: 0px;
}

p {
  font-family: Montserrat-Regular;
  font-size: 14px;
  line-height: 1.7;
  color: #666666;
  margin: 0px;
}

ul, li {
  margin: 0px;
  list-style-type: none;
}


/*---------------------------------------------*/
input {
  outline: none;
  border: none;
}

textarea {
  outline: none;
  border: none;
}

textarea:focus, input:focus {
  border-color: transparent !important;
}

input:focus::-webkit-input-placeholder { color:transparent; }
input:focus:-moz-placeholder { color:transparent; }
input:focus::-moz-placeholder { color:transparent; }
input:focus:-ms-input-placeholder { color:transparent; }

textarea:focus::-webkit-input-placeholder { color:transparent; }
textarea:focus:-moz-placeholder { color:transparent; }
textarea:focus::-moz-placeholder { color:transparent; }
textarea:focus:-ms-input-placeholder { color:transparent; }

input::-webkit-input-placeholder { color: #999999; }
input:-moz-placeholder { color: #999999; }
input::-moz-placeholder { color: #999999; }
input:-ms-input-placeholder { color: #999999; }

textarea::-webkit-input-placeholder { color: #999999; }
textarea:-moz-placeholder { color: #999999; }
textarea::-moz-placeholder { color: #999999; }
textarea:-ms-input-placeholder { color: #999999; }

/*---------------------------------------------*/
button {
  outline: none !important;
  border: none;
  background: transparent;
}

button:hover {
  cursor: pointer;
}

iframe {
  border: none !important;
}


/*//////////////////////////////////////////////////////////////////
[ Utility ]*/
.txt1 {
  font-family: Montserrat-Regular;
  font-size: 16px;
  color: #000000;
  line-height: 1.4;
}

.bo1 {
  border-bottom: 1px solid #999999;
}

.hov1:hover {
  border-color: #d33f8d;
}


/*//////////////////////////////////////////////////////////////////
[ login ]*/

.limiter {
  width: 100%;
  margin: 0 auto;
}

.container-login100 {
  width: 100%;
  min-height: 100vh;
  display: -webkit-box;
  display: -webkit-flex;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  padding: 15px;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;

  position: relative;
  z-index: 1;
}

.container-login100::before {
  content: "";
  display: block;
  position: absolute;
  z-index: -1;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  /*background: #005bea;*/
  /*background: -webkit-linear-gradient(bottom, #005bea, #00c6fb);*/
  /*background: -o-linear-gradient(bottom, #005bea, #00c6fb);*/
  /*background: -moz-linear-gradient(bottom, #005bea, #00c6fb);*/
  /*background: linear-gradient(bottom, #005bea, #00c6fb);*/
  opacity: 0.9;
}

.wrap-login100 {
  width: 390px;
  background: transparent;
}



/*------------------------------------------------------------------
[  ]*/
.login100-form {
  width: 100%;
  display: -webkit-box;
  display: -webkit-flex;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

.login100-form-title {
  font-family: Montserrat-ExtraBold;
  font-size: 24px;
  color: #fff;
  line-height: 1.2;
  text-align: center;

  width: 100%;
  display: block;
}

/*---------------------------------------------*/
.login100-form-avatar {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  overflow: hidden;
  margin: 0 auto;
}
.login100-form-avatar img {
  width: 100%;
}


/*---------------------------------------------*/
.wrap-input100 {
  position: relative;
  width: 100%;
  z-index: 1;
  margin: 10px;
}

.input100 {
  font-family: Montserrat-Bold;
  font-size: 15px;
  line-height: 1.2;
  color: #333333;

  display: block;
  width: 100%;
  background: #fff;
  height: 50px;
  border-radius: 25px;
  padding: 0 30px 0 53px;
}


/*------------------------------------------------------------------
[ Focus ]*/
.focus-input100 {
  display: block;
  position: absolute;
  border-radius: 25px;
  bottom: 0;
  left: 0;
  z-index: -1;
  width: 100%;
  height: 100%;
  box-shadow: 0px 0px 0px 0px;
  color: rgba(0,91,234, 0.6);
}

.input100:focus + .focus-input100 {
  -webkit-animation: anim-shadow 0.5s ease-in-out forwards;
  animation: anim-shadow 0.5s ease-in-out forwards;
}

@-webkit-keyframes anim-shadow {
  to {
    box-shadow: 0px 0px 80px 30px;
    opacity: 0;
  }
}

@keyframes anim-shadow {
  to {
    box-shadow: 0px 0px 80px 30px;
    opacity: 0;
  }
}

.symbol-input100 {
  font-size: 15px;
  color: #999999;

  display: -webkit-box;
  display: -webkit-flex;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;
  align-items: center;
  position: absolute;
  border-radius: 25px;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 100%;
  padding-left: 30px;
  pointer-events: none;

  -webkit-transition: all 0.4s;
  -o-transition: all 0.4s;
  -moz-transition: all 0.4s;
  transition: all 0.4s;
}

.input100:focus + .focus-input100 + .symbol-input100 {
  color: #00c6fb;
  padding-left: 23px;
}


/*------------------------------------------------------------------
[ Button ]*/
.container-login100-form-btn {
  width: 100%;
  display: -webkit-box;
  display: -webkit-flex;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.login100-form-btn {
  font-family: Montserrat-Bold;
  font-size: 15px;
  line-height: 1.5;
  color: #e0e0e0;

  width: 100%;
  height: 50px;
  border-radius: 25px;
  background: #333333;
  display: -webkit-box;
  display: -webkit-flex;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 25px;

  -webkit-transition: all 0.4s;
  -o-transition: all 0.4s;
  -moz-transition: all 0.4s;
  transition: all 0.4s;

  position: relative;
  z-index: 1;
}

.login100-form-btn::before {
  content: "";
  display: block;
  position: absolute;
  z-index: -1;
  width: 100%;
  height: 100%;
  border-radius: 25px;
  top: 0;
  left: 0;
  background: #005bea;
  background: -webkit-linear-gradient(left, #005bea, #00c6fb);
  background: -o-linear-gradient(left, #005bea, #00c6fb);
  background: -moz-linear-gradient(left, #005bea, #00c6fb);
  background: linear-gradient(left, #005bea, #00c6fb);
  -webkit-transition: all 0.4s;
  -o-transition: all 0.4s;
  -moz-transition: all 0.4s;
  transition: all 0.4s;
  opacity: 0;
}

.login100-form-btn:hover {
  background: transparent;
  color: #fff;
}

.login100-form-btn:hover:before {
  opacity: 1;
}

/*------------------------------------------------------------------
[ Button sign in with ]*/
.btn-face,
.btn-google {
  font-family: Raleway-Bold;
  font-size: 16px;
  line-height: 1.2;

  display: -webkit-box;
  display: -webkit-flex;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;
  justify-content: center;
  align-items: center;
  width: calc((100% - 10px) / 2);
  height: 40px;
  border-radius: 3px;
  border: 1px solid #e6e6e6;
  background-color: #fff;

  -webkit-transition: all 0.4s;
  -o-transition: all 0.4s;
  -moz-transition: all 0.4s;
  transition: all 0.4s;
}


.btn-face {
  color: #3b5998;
}

.btn-face i {
  font-size: 20px;
  margin-right: 10px;
  padding-bottom: 1px;
}

.btn-google {
  color: #555555;
}

.btn-google img {
  width: 19px;
  margin-right: 10px;
  padding-bottom: 1px;
}


.btn-face:hover,
.btn-google:hover {
  border-color: #d33f8d;
}



/*------------------------------------------------------------------
[ Alert validate ]*/

.validate-input {
  position: relative;
}

.alert-validate::before {
  content: attr(data-validate);
  position: absolute;
  max-width: 70%;
  background-color: white;
  border: 1px solid #c80000;
  border-radius: 14px;
  padding: 4px 25px 4px 10px;
  top: 50%;
  -webkit-transform: translateY(-50%);
  -moz-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  -o-transform: translateY(-50%);
  transform: translateY(-50%);
  right: 8px;
  pointer-events: none;

  font-family: Montserrat-Bold;
  color: #c80000;
  font-size: 13px;
  line-height: 1.4;
  text-align: left;

  visibility: hidden;
  opacity: 0;

  -webkit-transition: opacity 0.4s;
  -o-transition: opacity 0.4s;
  -moz-transition: opacity 0.4s;
  transition: opacity 0.4s;
}

.alert-validate::after {
  content: "\f06a";
  font-family: FontAwesome;
  display: block;
  position: absolute;
  color: #c80000;
  font-size: 15px;
  top: 50%;
  -webkit-transform: translateY(-50%);
  -moz-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  -o-transform: translateY(-50%);
  transform: translateY(-50%);
  right: 13px;
}

.alert-validate:hover:before {
  visibility: visible;
  opacity: 1;
}

@media (max-width: 992px) {
  .alert-validate::before {
    visibility: visible;
    opacity: 1;
  }
}

/*//////////////////////////////////////////////////////////////////
[ responsive ]*/

@media (max-width: 576px) {
  .wrap-login100 {
    padding-top: 80px;
    padding-left: 15px;
    padding-right: 15px;
  }
}
</style>
