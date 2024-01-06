<template>
	<div class="files">
    <el-dialog v-model="dialogFormVisible" title="新建文件/文件夹">
      文件（夹）名<el-input v-model="createDirName"></el-input>
      <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="create(createDirName, 'folder')">
          新建
        </el-button>
      </span>
      </template>
    </el-dialog>
		<div>
			<el-text style="color: #000000; font-size: large;">当前目录: </el-text>

			<el-cascader :options="options" :props="props1" clearable />

			<el-button
          color="#C45DD5"
          class="fop"
          type="primary"
          :icon="ArrowLeftBold"
          @click="back"
      >
			后退
      </el-button>


		</div>
		<div>
			<el-row :gutter="10">
				<el-col :xs="12" :sm="12" :md="6" :lg="6" :xl="6">
					<el-button color="#C45DD5" class="fop" type="primary" :icon="UploadFilled"><span
							style="color: #ffffff;">上传文件</span>
					</el-button>
				</el-col>
				<el-col :xs="12" :sm="12" :md="6" :lg="6" :xl="6">
					<el-button color="#C45DD5" class="fop" type="primary" :icon="FolderAdd"><span
							style="color: #ffffff;" @click="dialogFormVisible=true">新建文件夹</span></el-button>
				</el-col>
				<el-col :xs="12" :sm="12" :md="6" :lg="6" :xl="6">
					<el-button color="#C45DD5" class="fop" type="primary" :icon="DocumentAdd"><span
							style="color: #ffffff;" @click="dialogFormVisible=true">新建文件</span></el-button>
				</el-col>
				<el-col :xs="12" :sm="12" :md="6" :lg="6" :xl="6">
					<el-button color="#C45DD5" class="fop" type="primary" :icon="Files"><span
							style="color: #ffffff;">粘贴文件</span>
					</el-button>
				</el-col>
			</el-row>
		</div>
		<!-- 文件表格数据 -->
		<el-table
        :data="filterTableData"
        style="width: 100%; color: #000000;"
        height="300"
        :header-cell-style="{ color: '#000000' }"
        v-loading="loading"
    >
			<el-table-column label="文件名" prop="fileName" width="100">
				<template #default="scope">
					<el-button v-if="scope.row.fileType==='folder'" link style="color: #000000;" @click="open(scope.row)">{{ scope.row.fileName }}</el-button>
          <el-button v-else link style="color: #000000;" @click="open(scope.row)">{{ scope.row.fileName }}</el-button>
        </template>
			</el-table-column>

      <el-table-column label="修改日期" prop="modificationTime" width="120" />
      <el-table-column label="类型" prop="fileType" width="80">
        <template #default="scope">
          <el-tag type="success" v-if="scope.row.fileType === 'folder'">文件夹</el-tag>
          <el-tag v-else>文件</el-tag>
        </template>
      </el-table-column>
			<el-table-column label="大小" prop="fileSize"  width="100"/>
			<el-table-column align="right">
				<template #header>
					<el-input v-model="search" placeholder="搜索文件(夹)" />
				</template>
				<template #default="scope">
					<el-button size="small" type="success" @click="handleDelete(scope.$index, scope.row)">分享</el-button>
					<el-button size="small" type="primary" @click="handleDelete(scope.$index, scope.row)">下载</el-button>
					<el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
				</template>
			</el-table-column>
		</el-table>
	</div>


</template>

<script setup>
	import {
		Search,
		FolderAdd,
		Files,
		ArrowLeftBold,
		UploadFilled,
		DocumentAdd
	} from '@element-plus/icons-vue'
  import {
    computed,
    ref,
    onMounted, watch
  } from 'vue'
	import { ElNotification } from 'element-plus'
  import {createFCB, list} from "@/api/files";
  const dialogFormVisible = ref(false)
  const createDirName = ref('') // 新建文件名
	// 目录单选
	const props1 = {
		checkStrictly: true,
	}

	const options = [
      {
        value: 'guide',
        label: 'Guide',
        children: [{
            value: 'disciplines',
            label: 'Disciplines',
            children: [{
                value: 'consistency',
                label: 'Consistency',
              },
              {
                value: 'feedback',
                label: 'Feedback',
              },
              {
                value: 'efficiency',
                label: 'Efficiency',
              },
              {
                value: 'controllability',
                label: 'Controllability',
              },
            ],
          },
          {
            value: 'navigation',
            label: 'Navigation',
            children: [{
                value: 'side nav',
                label: 'Side Navigation',
              },
              {
                value: 'top nav',
                label: 'Top Navigation',
              },
            ],
          },
        ],
      },
      {
        value: 'component',
        label: 'Component',
        children: [{
            value: 'basic',
            label: 'Basic',
            children: [{
                value: 'layout',
                label: 'Layout',
              },
              {
                value: 'color',
                label: 'Color',
              },
              {
                value: 'typography',
                label: 'Typography',
              },
              {
                value: 'icon',
                label: 'Icon',
              },
              {
                value: 'button',
                label: 'Button',
              },
            ],
          },
          {
            value: 'form',
            label: 'Form',
            children: [{
                value: 'radio',
                label: 'Radio',
              },
              {
                value: 'checkbox',
                label: 'Checkbox',
              },
              {
                value: 'input',
                label: 'Input',
              },
              {
                value: 'input-number',
                label: 'InputNumber',
              },
              {
                value: 'select',
                label: 'Select',
              },
              {
                value: 'cascader',
                label: 'Cascader',
              },
              {
                value: 'switch',
                label: 'Switch',
              },
              {
                value: 'slider',
                label: 'Slider',
              },
              {
                value: 'time-picker',
                label: 'TimePicker',
              },
              {
                value: 'date-picker',
                label: 'DatePicker',
              },
              {
                value: 'datetime-picker',
                label: 'DateTimePicker',
              },
              {
                value: 'upload',
                label: 'Upload',
              },
              {
                value: 'rate',
                label: 'Rate',
              },
              {
                value: 'form',
                label: 'Form',
              },
            ],
          },
          {
            value: 'data',
            label: 'Data',
            children: [{
                value: 'table',
                label: 'Table',
              },
              {
                value: 'tag',
                label: 'Tag',
              },
              {
                value: 'progress',
                label: 'Progress',
              },
              {
                value: 'tree',
                label: 'Tree',
              },
              {
                value: 'pagination',
                label: 'Pagination',
              },
              {
                value: 'badge',
                label: 'Badge',
              },
            ],
          },
          {
            value: 'notice',
            label: 'Notice',
            children: [{
                value: 'alert',
                label: 'Alert',
              },
              {
                value: 'loading',
                label: 'Loading',
              },
              {
                value: 'message',
                label: 'Message',
              },
              {
                value: 'message-box',
                label: 'MessageBox',
              },
              {
                value: 'notification',
                label: 'Notification',
              },
            ],
          },
          {
            value: 'navigation',
            label: 'Navigation',
            children: [{
                value: 'menu',
                label: 'Menu',
              },
              {
                value: 'tabs',
                label: 'Tabs',
              },
              {
                value: 'breadcrumb',
                label: 'Breadcrumb',
              },
              {
                value: 'dropdown',
                label: 'Dropdown',
              },
              {
                value: 'steps',
                label: 'Steps',
              },
            ],
          },
          {
            value: 'others',
            label: 'Others',
            children: [{
                value: 'dialog',
                label: 'Dialog',
              },
              {
                value: 'tooltip',
                label: 'Tooltip',
              },
              {
                value: 'popover',
                label: 'Popover',
              },
              {
                value: 'card',
                label: 'Card',
              },
              {
                value: 'carousel',
                label: 'Carousel',
              },
              {
                value: 'collapse',
                label: 'Collapse',
              },
            ],
          },
        ],
      },
      {
        value: 'resource',
        label: 'Resource',
        children: [{
            value: 'axure',
            label: 'Axure Components',
          },
          {
            value: 'sketch',
            label: 'Sketch Templates',
          },
          {
            value: 'docs',
            label: 'Design Documentation',
          },
        ],
      },
    ]

const loading = ref(false)


const tableData = ref([
  {
    "_id": "65994c104379f4da38c8e221",
    "creationTime": "0001-01-01T00:00:00Z",
    "fileLocation": 0,
    "fileName": "123.txt",
    "fileSize": 0,
    "fileType": "file",
    "group": 0,
    "inodeNumber": 0,
    "modificationTime": "0001-01-01T00:00:00Z",
    "owner": 0,
    "parentId": "65994c2c4379f4da38c8e222",
    "permissions": ""
  }
]) // 文件目录
const parentId = ref(["root"]) // 文件夹id队列

// 监听文件夹id
watch(parentId, () =>{
  loadData(parentId.value.at(-1))
})

// 加载数据
const loadData = (id) => {
  loading.value = true
  list(id).then(res => {
    let data = res.data.data
    // 加载数据
    if (res.data.code === 0) {
      if (!data) {
        data = []
      }
      data.sort((a, b) => b.fileType.localeCompare(a.fileType))
      tableData.value = data
    }
    loading.value = false
  })
}
// 后退文件夹
const back = () => {
  const id = parentId.value.at(-1)
  if (id === 'root') {
    ElNotification({
      title: '文件系统',
      message: '已经是根目录了',
      type: 'error',
    })
    return
  }
  parentId.value.pop()

  loadData(parentId.value.at(-1))
}

// 创建一个FCB
const create = (FileName, FileType) => {
  let id = parentId.value.at(-1)
  if (id === 'root') {
    id = null
  }
  createFCB({
    FileName: FileName,
    FileType: FileType,
    parentId: id
  }).then(res => {
    if (res.data.code === 0) {
      dialogFormVisible.value = false
      ElNotification({
        title: '文件系统',
        message: res.data.msg,
        type: 'success',
      })
      loadData(parentId.value.at(-1))

    } else {
      ElNotification({
        title: '文件系统',
        message: res.data.msg,
        type: 'error',
      })
    }
  })
}

onMounted(() => {
  loadData(parentId.value[0])
})

const search = ref('')
const filterTableData = computed(() =>
  tableData.value.filter(
    (data) =>
      !search.value ||
      data.fileName.toLowerCase().includes(search.value.toLowerCase())
  )
)
const handleEdit = (index, row) => {
	ElNotification({
	title: 'Success',
	message: 'This is a success message',
	type: 'success',
  })
  console.log(index, row)
}
const handleDelete = (index, row) => {
	ElNotification({
	title: 'Success',
	message: 'This is a success message',
	type: 'success',
  })
  console.log(index, row)
}
// 打开文件或者文件夹
const open = (row) => {
  if (row.fileType === 'folder') {
    // 改变当前路径ID
    parentId.value.push(row._id)
    loadData(parentId.value.at(-1))
    return
  }
	ElNotification({
	    title: '文件系统',
	    message: `打开文件：${row.fileName}`,
	    type: 'success',
  })
	console.log(row.value)
	
}
</script>

<style>
	.upload-demo {
		width: 20%;
		height: 20px;
	}

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

	/* 表格美化 */
	table {
		border-collapse: collapse;
		width: 100%;

	}

	th,
	td {
		/*border: 1px solid #ccc;*/
		padding: 8px;
		text-align: left;
		transition: background-color 0.3s;
	}

	tr:hover {
		background-color: #f2f2f2;
	}

	th {
		background-color: #f2f2f2;
	}

	.files {
		/* width: 50%; */
		background-color: #ffffff;
		padding: 20px;
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
		opacity: 0.8;
		margin-right: 1%;
		height: 450px;
		/* 设置容器高度 */
		overflow-y: scroll;
		/* 设置水平滚动条 */
		overflow-x: hidden;
		/* 隐藏垂直滚动条 */
		margin: 5px;
		border-radius: 10px;
	}

	a {
		padding: 2px;
	}
</style>
