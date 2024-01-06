<template>
	<div class="files">
<!--		<div>-->
<!--			<h2 style="text-align: center;margin: 10px;">文件系统</h2>-->
<!--		</div>-->
		<div>
			<el-text style="color: #000000; font-size: large;">当前目录: </el-text>

			<el-cascader :options="options" :props="props1" clearable />

			<el-button color="#C45DD5" class="fop" type="primary" :icon="ArrowLeftBold">
				<!-- <span
					style="color: #ffffff;"></span> -->
			</el-button>

		</div>
		<!-- <div style="display: flex;justify-content: flex-end;align-items: center;"> -->
		<div>
			<el-row :gutter="10">
				<el-col :xs="12" :sm="12" :md="6" :lg="6" :xl="6">
					<el-button color="#C45DD5" class="fop" type="primary" :icon="UploadFilled"><span
							style="color: #ffffff;">上传文件</span>
					</el-button>
				</el-col>
				<el-col :xs="12" :sm="12" :md="6" :lg="6" :xl="6">
					<el-button color="#C45DD5" class="fop" type="primary" :icon="FolderAdd"><span
							style="color: #ffffff;">新建文件夹</span></el-button>
				</el-col>
				<el-col :xs="12" :sm="12" :md="6" :lg="6" :xl="6">
					<el-button color="#C45DD5" class="fop" type="primary" :icon="DocumentAdd"><span
							style="color: #ffffff;">新建文件</span></el-button>
				</el-col>
				<el-col :xs="12" :sm="12" :md="6" :lg="6" :xl="6">
					<el-button color="#C45DD5" class="fop" type="primary" :icon="Files"><span
							style="color: #ffffff;">粘贴文件</span>
					</el-button>
				</el-col>
			</el-row>
		</div>
		<!-- 文件表格数据 -->
		<el-table :data="filterTableData" style="width: 100%; color: #000000;" height="300" :header-cell-style="{ color: '#000000' }">
			<el-table-column label="文件名" prop="name" width="100">
				<template #default="scope">
					<el-button link style="color: #000000;" @click="open">{{ scope.row.name }}</el-button>
			    </template>
			</el-table-column>
			
			<el-table-column label="修改日期" prop="date" width="120" />
			<el-table-column label="类型" prop="type" width="70"/>
			<el-table-column label="大小" prop="size"  width="100"/>
			<el-table-column align="right">
				<template #header>
					<el-input v-model="search" size="small" placeholder="搜索文件(夹)" />
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
		ref
	} from 'vue'
	import { ElNotification } from 'element-plus'

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

// 文件目录
const tableData = ref([
  {
    date: '2016-05-03',
    name: 'Tom',
    type: '文件夹',
	size: '-'
  },
  {
    date: '2016-05-02',
    name: 'John',
    type: '文件',
	size: '50KB'
  },
  {
    date: '2016-05-04',
    name: 'Morgan',
    type: '文件',
	size: '50KB'
  },

])

const search = ref('')
const filterTableData = computed(() =>
  tableData.value.filter(
    (data) =>
      !search.value ||
      data.name.toLowerCase().includes(search.value.toLowerCase())
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
const open = (index, row) => {
	ElNotification({
	    title: 'Success',
	    message: 'This is a success message',
	    type: 'success',
  })
	console.log(index, row)
	
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
