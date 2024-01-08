<template>
	<el-drawer
		v-model="drawer"
		title="I am the title"
		:with-header="false"
		:modal="true"
		:show-close="true"
		:size="'80%'"
		direction="ttb">
		<div class="drawer">
      <start v-if="opt==='start'"></start>
      <setting v-else-if="opt==='setting'"></setting>
      <info v-else-if="opt === 'info'"></info>
		</div>
	</el-drawer>
	<div class="main">
		<div class="bottom-nav">
			<div class="nav-item" @click="drawer = true; opt='start';">
				<svg t="1704165993478" class="icon" viewBox="0 0 1024 1024" version="1.1"
					xmlns="http://www.w3.org/2000/svg" p-id="5923" width="200" height="200">
					<path
						d="M426.276571 574.866286v372.004571L36.571429 893.147429v-318.281143h389.705142z m0-424.594286v376.576H36.571429V203.995429zM987.428571 574.866286V1024l-518.290285-71.424V574.866286H987.428571zM987.428571 73.142857v453.705143H469.138286V144.566857z"
						fill="#1296db" p-id="5924"></path>
				</svg>
			</div>
			<div class="nav-item" @click="drawer = true; opt='setting';">
				<svg t="1704166457026" class="icon" viewBox="0 0 1024 1024" version="1.1"
					xmlns="http://www.w3.org/2000/svg" p-id="7093" width="200" height="200">
					<path
						d="M940 596l-76-57.6c0.8-8 1.6-16.8 1.6-26.4s-0.8-18.4-1.6-26.4l76-57.6c20.8-16 26.4-44 12.8-68L868 216.8c-9.6-16.8-28-27.2-47.2-27.2-6.4 0-12 0.8-18.4 3.2L712 228c-15.2-10.4-31.2-19.2-47.2-26.4l-13.6-92c-4-26.4-26.4-45.6-53.6-45.6H426.4c-27.2 0-49.6 19.2-53.6 44.8L360 201.6c-16 7.2-31.2 16-47.2 26.4l-90.4-35.2c-6.4-2.4-12.8-3.2-19.2-3.2-19.2 0-37.6 9.6-46.4 26.4L71.2 360c-13.6 22.4-8 52 12.8 68l76 57.6c-0.8 9.6-1.6 18.4-1.6 26.4s0 16.8 1.6 26.4L84 596c-20.8 16-26.4 44-12.8 68L156 807.2c9.6 16.8 28 27.2 47.2 27.2 6.4 0 12-0.8 18.4-3.2L312 796c15.2 10.4 31.2 19.2 47.2 26.4l13.6 92C376 940 399.2 960 426.4 960h171.2c27.2 0 49.6-19.2 53.6-44.8l13.6-92.8c16-7.2 31.2-16 47.2-26.4l90.4 35.2c6.4 2.4 12.8 3.2 19.2 3.2 19.2 0 37.6-9.6 46.4-26.4l85.6-144.8C966.4 640 960.8 612 940 596z m-236-84c0 105.6-86.4 192-192 192s-192-86.4-192-192 86.4-192 192-192 192 86.4 192 192z"
						p-id="7094" fill="#bfbfbf"></path>
				</svg>
			</div>
			<div class="nav-item" @click="drawer = true; opt='info';">
				<svg t="1704166513250" class="icon" viewBox="0 0 1041 1024" version="1.1"
					xmlns="http://www.w3.org/2000/svg" p-id="8356" width="200" height="200">
					<path
						d="M524.575 975.495c255.102 0 459.902-206.597 459.902-461.699S779.677 53.895 524.575 53.895 62.877 258.695 62.877 513.796s206.597 461.699 461.698 461.699z m0 46.709c-280.252 0-506.61-228.155-506.61-508.408S244.323 7.186 524.575 7.186s506.611 226.358 506.611 506.61-226.358 508.408-506.61 508.408z m26.948-795.846c-16.169 0-28.744 5.39-41.32 16.168-10.778 10.78-17.964 25.151-17.964 41.32s5.39 28.743 17.965 41.319c10.778 10.779 25.15 16.168 41.319 16.168 16.168 0 28.744-5.39 41.32-16.168 10.778-10.779 16.168-25.151 16.168-41.32 0-16.168-5.39-28.743-16.169-41.319-12.575-10.779-25.15-16.168-41.32-16.168z m-3.593 513.796c-5.39-5.39-7.186-16.168-7.186-30.54 0-5.39 0-14.372 1.796-25.15 1.797-10.78 3.593-21.559 5.39-30.541l21.558-111.383c1.796-10.779 3.593-21.558 3.593-34.133s1.796-21.558 1.796-25.15c0-23.355-5.39-43.117-17.965-57.489-10.779-14.372-26.947-21.557-48.505-21.557-10.779 0-23.354 3.593-37.726 8.982-12.576 5.39-26.948 12.575-41.32 21.558l-5.39 34.133c3.594-1.796 8.983-5.39 14.373-7.186 5.39-1.796 12.575-3.593 17.965-3.593 10.779 0 19.761 3.593 23.354 8.983 3.593 5.39 5.39 16.168 5.39 30.54 0 7.186 0 16.168-1.797 25.15-1.796 8.983-3.593 19.762-5.39 30.541l-19.76 111.383c-1.797 12.575-3.594 21.558-3.594 30.54-1.796 8.983-1.796 17.965-1.796 26.947 0 23.355 5.39 41.32 17.965 57.488 12.575 14.372 28.744 21.558 50.301 21.558 14.372 0 25.151-1.796 35.93-7.186 10.78-5.39 25.151-12.575 41.32-23.354l5.39-34.134-14.373 7.186c-7.186 1.797-12.575 3.593-17.965 3.593-10.779 1.797-19.761-1.796-23.354-7.186z"
						fill="#1296DB" p-id="8357"></path>
				</svg>
			</div>
			<div class="nav-item" @click="login_out">
        <svg t="1704509491387" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="9209" width="200" height="200"><path d="M509.1 1003.3c-239.9 0-435-195.1-435-435 0-109.3 40.7-213.8 114.6-294.2 21.7-23.6 46.1-44.9 72.2-63.1 20.4-14.2 48.5-9.1 62.6 11.3 14.2 20.4 9.1 48.5-11.3 62.6-20.8 14.5-40.1 31.3-57.4 50.1-58.6 63.8-90.8 146.6-90.8 233.3 0 190.2 154.8 345 345 345s345-154.8 345-345c0-88.3-33.3-172.3-93.8-236.5-16.5-17.5-34.8-33.3-54.4-46.9-20.4-14.2-25.4-42.2-11.3-62.6 14.2-20.4 42.2-25.5 62.6-11.3 24.7 17.2 47.8 37.1 68.5 59.1 76.3 81 118.3 186.9 118.3 298.2 0.2 239.9-194.9 435-434.8 435z" fill="#2081F6" p-id="9210"></path><path d="M509.1 13.3c-24.9 0-45 20.1-45 45v390c0 24.9 20.1 45 45 45s45-20.1 45-45v-390c0-24.8-20.1-45-45-45z" fill="#4C4F54" p-id="9211"></path></svg>
			</div>
		</div>
	</div>

</template>

<script setup>
	import {
		ref
	} from 'vue'
  import {
    ElDrawer,
    ElMessageBox, ElNotification
  } from 'element-plus'
  import info from './info.vue'
  import start from './start.vue'
  import setting from './setting.vue'
  import { useRouter } from 'vue-router';
const router = useRouter()
const drawer = ref(false)
const opts = ['info', 'start', 'setting']
const opt = ref('')
//  退出登录
const login_out = ()=> {
    // localStorage.setItem('token', null)
  // localStorage.removeItem('token')
  localStorage.clear()
  ElNotification({
    title: '系统消息',
    message: '退出系统成功',
    type: 'warning',
  })
  router.push({'name': 'Login'})

}
</script>

<style>
	.el-drawer {
	  background-image: url("/bg-light.svg");
	  background-size: cover;

	}
	.main {
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.bottom-nav {
		display: flex;
		justify-content: center;
		padding: 10px;
		background-color: aliceblue;
		opacity: 0.9;
		border-radius: 10px;
	}

	.nav-item {
		padding: 5px;
		margin: 5px;
		transition: all 0.3s ease;
		border-radius: 10px;
	}

	.nav-item:hover {
		transform: scale(1.1) translate(-5px, -5px);
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
	}

	@keyframes scaleAndShadow {
		from {
			transform: scale(1) translate(-5px, -5px);
			box-shadow: none;
		}

		to {
			transform: scale(1.1) translate(-5px, -5px);
			box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
		}
	}
</style>
