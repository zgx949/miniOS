<template>
  <!-- 新建文件窗口 -->
  <el-dialog v-model="dialogFormVisible" title="新建文件/文件夹">
    <el-radio-group v-model="newFileType">
      <el-radio :label="'folder'">文件夹</el-radio>
      <el-radio :label="'file'">文件</el-radio>
    </el-radio-group>
    文件（夹）名<el-input v-model="createDirName"></el-input>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="create(createDirName, newFileType)">
          新建
        </el-button>
      </span>
    </template>
  </el-dialog>

  <div>
    <el-row :gutter="10">
      <el-col :xs="12" :sm="12" :md="6" :lg="6" :xl="6">
        <el-button color="#C45DD5" class="fop" type="primary" :icon="ArrowLeftBold"><span
            style="color: #ffffff;" @click="back">后退</span>
        </el-button>
      </el-col>
      <el-col :xs="12" :sm="12" :md="6" :lg="6" :xl="6">
        <el-button color="#C45DD5" class="fop" type="primary" :icon="UploadFilled"><span
            style="color: #ffffff;">上传</span>
        </el-button>
      </el-col>
      <el-col :xs="12" :sm="12" :md="6" :lg="6" :xl="6">
        <el-button color="#C45DD5" class="fop" type="primary" :icon="DocumentAdd"><span
            style="color: #ffffff;" @click="dialogFormVisible=true">新建</span></el-button>
      </el-col>
      <el-col :xs="12" :sm="12" :md="6" :lg="6" :xl="6">
        <el-button color="#C45DD5" class="fop" type="primary" :icon="Files"><span
            style="color: #ffffff;">粘贴</span>
        </el-button>
      </el-col>

    </el-row>
  </div>
</template>

<script setup>
import {
  Files,
  ArrowLeftBold,
  UploadFilled,
  DocumentAdd
} from '@element-plus/icons-vue'

import {defineEmits, ref} from 'vue'
import {createFCB} from "@/api/files";
import {ElNotification} from "element-plus";
const emits = defineEmits(['back', 'create'])

const newFileType = ref('folder') // 创建文件还是文件夹

const createDirName = ref('') // 新建文件名

const back = () => {
  emits('back')
}
// 新建弹窗
const dialogFormVisible = ref(false)

// 创建一个FCB
const create = (FileName, FileType) => {
  emits('create', FileName, FileType)
}

</script>

<style scoped>
.fop {
  /*background-color: #4CAF50;*/
  background-color: #C45DD5;
  border: none;
  color: white;
  text-align: center;
  text-decoration: none;
  /*display: inline-block;*/
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  padding: 10px 24px;
  border-radius: 12px;
}

.fop:hover {
  /*background-color: #45a049;*/
  background-color: #8A66FE;
}
</style>