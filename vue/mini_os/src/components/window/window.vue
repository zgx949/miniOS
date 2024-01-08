<template>
  <transition name="drag-win">
    <div
        class="drag-dialog ban-select-font"
        ref="dragWin"
        v-show="props.modelValue"
        v-resize="props.resizeAble"
    >
      <!-- 拖拽窗体头部 -->
      <div class="drag-bar" :style="props.headStyle" v-drag="props.dragAble">
        <slot name="head" />
        <el-button text :icon="Close"
            class="drag-btn"
            @click="controlDialog"
            v-if="props.closeShow"
            type="danger"
        />

        <el-button text :icon="CopyDocument"
            class="drag-btn"
            @click="fullScreen"
            v-if="props.fullShow"
        />

        <el-button text :icon="Minus"
                   class="drag-btn"
                   @click="hide"
        />
      </div>
      <!-- 拖拽框主要部分 -->
      <div class="drag-main" :style="props.mainStyle">
        <slot />
      </div>
    </div>
  </transition>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import { Minus, CopyDocument, Close } from "@element-plus/icons-vue";

// props传入数据类型约束
interface Props {
  modelValue: boolean; //控制窗体的显示与否
  width?: string; // 默认宽 —— 设置头高 宽高最好传入变量
  height?: string; // 默认高
  headHeight?: string; // 默认控制栏高
  headStyle?: string; // 控制栏样式
  mainStyle?: string; //主要内容区域样式
  resizeAble?: boolean | string; // 是否可以调整尺寸 默认可以调整
  dragAble?: boolean | string; // 是否可以拖拽 默认可拖拽
  closeShow?: boolean; // 关闭控制显示 默认不显示
  fullShow?: boolean; // 全屏控制显示 默认不显示
}
/** 组件调整参数默认值 */
const props = withDefaults(defineProps<Props>(), {
  modelValue: true,
  width: "500px",
  height: "60vh",
  headHeight: "35px",
  headStyle: "",
  mainStyle: "",
  resizeAble: "",
  dragAble: "",
  closeShow: true,
  fullShow: true
});

// 窗体记录数据类型约束
interface recordType {
  width: number;
  height: number;
  top: number;
  left: number;
  fill: boolean;
}
//记录原来的大小
const recordBox: recordType = {
  width: 0,
  height: 0,
  top: 0,
  left: 0,
  fill: false
};

//获取窗口实体
const dragWin: any = ref(null);
// 事件定义
const emits = defineEmits(["update:modelValue", "close", "hide"]);

/** 方法定义 */
// 内部控制窗口开关
const controlDialog = () => {
  emits("update:modelValue", !props.modelValue);
  emits("closeWindow")
}

// 隐藏窗口
const hide = () => {
  emits("hide")
}

// 全屏控件
const fullScreen = () => {
  const tmp = dragWin.value;
  const style = dragWin.value.style;
  // 宽的样式 如果被手动缩小或者放大，则表示非全屏状态，则将状态置为false
  if (!style.width || style.width !== "100vw") {
    recordBox.fill = false;
  }
  // 全屏或是还原
  if (recordBox.fill) {
    style.width = `${recordBox.width}px`;
    style.height = `${recordBox.height}px`;
    style.top = `${recordBox.top}px`;
    style.left = `${recordBox.left}px`;
  } else {
    // 记录一下原来的样式
    recordBox.width = tmp.offsetWidth;
    recordBox.height = tmp.offsetHeight;
    recordBox.top = tmp.offsetTop;
    recordBox.left = tmp.offsetLeft;
    //全屏样式
    style.width = "100vw";
    style.height = "100vh";
    style.top = "0px";
    style.left = "0px";
  }
  recordBox.fill = !recordBox.fill; // 全屏状态变换
};
</script>

<style scoped>
/* 禁止选中文字 */
.ban-select-font {
  -moz-user-select: none; /*火狐*/
  -webkit-user-select: none; /*webkit浏览器*/
  -ms-user-select: none; /*IE10*/
  -khtml-user-select: none; /*早期浏览器*/
  user-select: none;
}

.drag-dialog {
  border-radius: 10px;
  position: fixed;
  width: v-bind("props.width");
  height: v-bind("props.height");
  left: calc(50% - v-bind("props.width") / 2);
  top: calc(50% - v-bind("props.height") / 2);
  box-sizing: border-box;
  padding: 8px;
  overflow: hidden;
  color: #fff;
  min-width: 200px;
  min-height: 200px;
  max-width: 100vw;
  max-height: 100vh;
  background-color: #ffffff;
}

.drag-bar {
  width: 100%;
  cursor: move;
  height: v-bind("props.headHeight");
  border-bottom: 1px solid #fff;
  box-sizing: border-box;
  padding: 1px 2px 9px;
  background-color: #ffffff;
  border-bottom-color: #000000;
}

.drag-btn {
  width: 25px;
  height: 25px;
  float: right;
  cursor: pointer;
  margin-left: 5px;
}


.drag-main {
  width: 100%;
  height: calc(100% - v-bind("props.headHeight"));
  box-sizing: border-box;
  overflow: auto;
  font-size: 13px;
  line-height: 1.6;
}

/* vue渐入渐出样式 */
.drag-win-enter-from,
.drag-win-leave-to {
  opacity: 0;
  transform: scale(0);
}
.drag-win-enter-to,
.drag-win-leave-from {
  opacity: 1;
}
.drag-win-enter-active,
.drag-win-leave-active {
  transition: all 0.5s ease;
}
</style>
