package Models

import (
	"time"
)

type FileControlBlock struct {
	ID               uint      `gorm:"primary_key"`
	FileName         string    // 文件名
	FileSize         int64     // 文件大小
	CreationTime     time.Time // 创建时间
	ModificationTime time.Time // 修改时间
	Permissions      string    // 权限
	Owner            int       // 所有者
	Group            int       // 组
	FileType         string    // 文件类型, 是普通文件还是目录文件
	FileLocation     int64     // 文件位置
	InodeNumber      int       // 索引节点号
}

//func main() {
//	// 示例用法
//	fcb := FileControlBlock{
//		FileName:         "example.txt",
//		FileSize:         1024,
//		CreationTime:     time.Now(),
//		ModificationTime: time.Now(),
//		Permissions:      "rwx",
//		Owner:            1000,
//		Group:            1000,
//		FileType:         "regular file",
//		FileLocation:     1024,
//		InodeNumber:      1,
//	}
//
//	fmt.Println(fcb)
//}
