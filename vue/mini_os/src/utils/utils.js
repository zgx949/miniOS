import SparkMD5 from 'spark-md5'
import {upload} from "@/api/files";

// 生成文件MD5
export function getFileMd5(file) {
    return new Promise((resolve, reject) => {
        const fileReader = new FileReader()
        const spark = new SparkMD5.ArrayBuffer()
        fileReader.onload = e => {
        spark.append(e.target.result)
        const md5 = spark.end()
        resolve(md5)
        }
        fileReader.onerror = () => {
        reject(new Error('文件读取出错'))
        }
        fileReader.readAsArrayBuffer(file)
    })
}

// 计算文件分块数量
export function getChunkCount(file) {
    const size = file.size
    const chunkCount = Math.ceil(size / 1024 / 1024)
    return chunkCount
}


export async function buildChunkForm(fcbId, file, chunkNumber, chunkTotal, fileName) {
    const form = new FormData();
    // 这里的data是文件
    form.append("FCBId", fcbId);
    form.append("file", file);
    form.append("chunkNumber", chunkNumber);
    form.append("chunkTotal", chunkTotal);
    form.append("fileName", fileName)
    // TODO:加入md5校验码
    const md5 = await getFileMd5(file)
    form.append("md5", md5)
    return form
}

// 字节单位转为可读单位
export function bytesToSize(bytes, precision = 2) {
    let sizes = ['B', 'KB', 'MB', 'GB', 'TB'];
    if (bytes == 0) return '0 B';
    let i = parseInt(Math.floor(Math.log(bytes) / Math.log(1024)));
    return Math.round((bytes / Math.pow(1024, i)), 2).toFixed(precision) + ' ' + sizes[i];
}

export function getRootUrl() {
    return window.location.protocol + '//' + window.location.host;
}