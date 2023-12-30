package main

// 创建文件
func create(filename string) bool {
	// 新增一个FCB项
	return true
}

// 打开文件
func open(filename string) int {
	// 读取一个FCB项，和索引节点到内存
	return -1
}

// 定位指针
func seek(offset int) bool {
	// 修改文件指针
	return true
}

// 读取文件
func read(fd int) byte {
	// 根据文件指针读取一个块
	return 0
}

// 写入文件
func write(fd int, content string) bool {
	// 写入一个块
	return true
}

// 关闭文件
func close(fd int) bool {
	// 关闭一个文件
	return true
}

// 删除文件
func delete(fd int) bool {
	// 删除文件
	return true
}
