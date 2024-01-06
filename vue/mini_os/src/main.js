import { createApp } from 'vue'
import App from './App.vue'
// main.ts
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import router from "@/router";

const app = createApp(App)

app.use(ElementPlus)
// 注册路由
app.use(router)
app.mount('#app')

