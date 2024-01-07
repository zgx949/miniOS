package models

import (
	"fmt"
	"time"
)

// FileIndexNode 文件索引结点结构体
type FileIndexNode struct {
	FileName         string                    // 文件名
	FileSize         int64                     // 文件大小，以字节为单位
	CreationTime     int64                     // 创建时间，以UNIX时间戳表示
	ModificationTime int64                     // 修改时间，以UNIX时间戳表示
	Permissions      string                    // 访问权限，例如读、写和执行等
	OwnerID          int                       // 所有者，通常是一个用户ID
	GroupID          int                       // 组，通常是一个组ID
	FileType         string                    // 文件类型，例如普通文件、目录或设备文件等
	FileLocation     int64                     // 文件在磁盘上的位置，通常是一个偏移量
	SecondaryIndex   map[string]*FileIndexNode // 二级索引，根据文件名的前缀进行索引
}

func main() {
	file := &FileIndexNode{
		FileName:         "example.txt",
		FileSize:         1024,
		CreationTime:     time.Now().Unix(),
		ModificationTime: time.Now().Unix(),
		Permissions:      "rw-r--r--",
		OwnerID:          1000,
		GroupID:          1000,
		FileType:         "regular file",
		FileLocation:     0,
		SecondaryIndex:   make(map[string]*FileIndexNode),
	}

	fmt.Println("文件信息：")
	fmt.Printf("文件名：%s\n", file.FileName)
	fmt.Printf("文件大小：%d 字节\n", file.FileSize)
	fmt.Printf("创建时间：%d\n", file.CreationTime)
	fmt.Printf("修改时间：%d\n", file.ModificationTime)
	fmt.Printf("权限：%s\n", file.Permissions)
	fmt.Printf("所有者：%d\n", file.OwnerID)
	fmt.Printf("组：%d\n", file.GroupID)
	fmt.Printf("文件类型：%s\n", file.FileType)
	fmt.Printf("文件位置：%d\n", file.FileLocation)
}
