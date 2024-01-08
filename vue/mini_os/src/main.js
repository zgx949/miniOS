import { createApp } from 'vue'
import App from './App.vue'
// main.ts
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import router from "@/router";
import registerDirectives from "@/components/window/index";


const app = createApp(App)
// 注冊窗口拖动事件
app.use(registerDirectives)
app.use(ElementPlus)
// 注册路由
app.use(router)
app.mount('#app')

