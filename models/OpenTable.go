package models

import (
	"time"
)

// SystemOpenFileTable 系统打开文件表结构体
type SystemOpenFileTable struct {
	FileID           string                 // 文件ID：唯一标识每个文件的编号
	FilePath         string                 // 文件路径：文件在系统中的存储路径
	FileName         string                 // 文件名：文件的名称
	CreationTime     time.Time              // 创建时间：文件被创建的时间
	ModificationTime time.Time              // 修改时间：文件最后一次被修改的时间
	FileSize         int64                  // 文件大小：文件的大小
	OtherAttributes  map[string]interface{} // 其他属性：例如文件类型、权限等
}

// UserOpenFileTable 用户打开文件表结构体
type UserOpenFileTable struct {
	UserID          string                 // 用户ID：唯一标识每个用户的编号
	FileID          string                 // 文件ID：与系统打开文件表中的文件ID对应
	OpenTime        time.Time              // 打开时间：用户打开文件的时间
	OperationStatus string                 // 操作状态：表示用户对文件的操作状态，例如只读、读写等
	OtherAttributes map[string]interface{} // 其他属性：例如光标位置、锁定状态等
}
