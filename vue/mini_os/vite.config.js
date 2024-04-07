import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path';

const getEnvVarOrDefault = (key, defaultValue) => {
  const value = process.env[key];
  if (!value) {
    return defaultValue;
  }
  return value;
};

// const baseUrl = "http://localhost:8000"
const baseUrl = getEnvVarOrDefault("baseUrl", "http://localhost:8000")

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: '0.0.0.0',
    https: false,
    proxy: {
      '/api': {
        target: baseUrl, // 接口的域名
        secure: false, // 如果是https接口，需要配置这个参数
        changeOrigin: true, // 如果接口跨域，需要进行这个参数配置
        rewrite: path => path.replace(/^\/api/, '')
      }
    },
  //   // server: {
  //   //   middlewareMode: 'ssr',
  //   //   middlewares: [
  //   //     proxyMiddleware('/api', {
  //   //       target: baseUrl,
  //   //       changeOrigin: true,
  //   //       // 增加超时时间
  //   //       timeout: 60 * 1000, // 设置为60秒，根据实际情况调整
  //   //     }),
  //   //   ],
  //   // },
  },
  resolve: {
    alias: {
      '@': resolve(__dirname, './src'), // 将'@'指向src目录
    },
  },
})
