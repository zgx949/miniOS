<!-- RightClickMenu.vue -->
<template>
  <div class="right-click-menu" v-if="showMenu">
    <ul>
      <li v-for="(item, index) in menuItems" :key="index" @click="handleMenuItemClick(item)">
        {{ item.label }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
// 组件参数定义
// const props = defineProps({
//   menuItems: {
//     type: Array,
//     required: true,
//   },
// });
const menuItems = [{label: '测试'}, {label: '测试2'}]

const showMenu = ref(false);

function handleContextMenu(event) {
  event.preventDefault();
  showMenu.value = true;
}

function handleClickOutside(event) {
  const menuElement = document.querySelector('.right-click-menu');
  if (menuElement && !menuElement.contains(event.target)) {
    showMenu.value = false;
  }
}

function handleMenuItemClick(item) {
  if (typeof item.onClick === 'function') {
    item.onClick();
  }
  showMenu.value = false;
}

onMounted(() => {
  document.addEventListener('mousedown', handleClickOutside);
  document.addEventListener('contextmenu', handleContextMenu);
});

onUnmounted(() => {
  document.removeEventListener('mousedown', handleClickOutside);
  document.removeEventListener('contextmenu', handleContextMenu);
});
</script>

<style scoped>
.right-click-menu {
  position: absolute;
  /* 添加你的样式 */
}
</style>