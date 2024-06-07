import { App } from "vue";
// import bus from "@/plugins/bus";
var zIndex = 0
const directives = {
    drag: {
        mounted(el: any, binding: any, vnode: any) {
            // 如果传递了false就不启用指令，反之true undefined null 不传 则启动
            if (!binding.value && (binding.value ?? "") !== "") return;
            // 拖拽实现
            const odiv = el.parentNode;
            zIndex++
            odiv.style.zIndex = zIndex; //当前拖拽的在最前面显示
            // // 配置移动端拖拽
            el.ontouchstart = (e: any) => {
                zIndex++
                odiv.style.zIndex = zIndex; //当前拖拽的在最前面显示
                const disX = e.touches[0].clientX - odiv.offsetLeft;
                const disY = e.touches[0].clientY - odiv.offsetTop;
                const clientWidth = document.documentElement.clientWidth; //页面的宽
                const oWidth = odiv.clientWidth; //窗口的宽
                const maxX = clientWidth - oWidth; // x轴能移动的最大距离
                const clientHeight = document.documentElement.clientHeight; //页面的高
                const oHeight = odiv.clientHeight; //窗口的高度
                const maxY = clientHeight - oHeight; //y轴能移动的最大距离
                document.ontouchmove = (e: any) => {
                    e.preventDefault;
                    let left = e.touches[0].clientX - disX;
                    let top = e.touches[0].clientY - disY;
                    if (left < 0) left = 0;
                    if (left > maxX) left = maxX;
                    if (top < 0) top = 0;
                    if (top > maxY) top = maxY;
                    odiv.style.left = left + "px";
                    odiv.style.top = top + "px";
                    odiv.style.marginLeft = 0;
                    odiv.style.marginTop = 0;
                };
                document.ontouchend = () => {
                    zIndex++
                    odiv.style.zIndex = zIndex; //当前拖拽的在最前面显示
                    document.ontouchmove = null;
                };
            };


            // 配置PC端拖拽
            el.onmousedown = (eve: any) => {
                zIndex++
                odiv.style.zIndex = zIndex; //当前拖拽的在最前面显示
                // bus.emit("showDrag", 0); //按下的时候发送事件 让其余窗体恢复层级
                eve = eve || window.event;
                const mx = eve.pageX; //鼠标点击时的坐标
                const my = eve.pageY; //鼠标点击时的坐标
                const dleft = odiv.offsetLeft; //窗口初始位置
                const dtop = odiv.offsetTop;
                const clientWidth = document.documentElement.clientWidth; //页面的宽
                const oWidth = odiv.clientWidth; //窗口的宽
                const maxX = clientWidth - oWidth; // x轴能移动的最大距离
                const clientHeight = document.documentElement.clientHeight; //页面的高
                const oHeight = odiv.clientHeight; //窗口的高度
                const maxY = clientHeight - oHeight; //y轴能移动的最大距离
                document.onmousemove = (e: any) => {
                    e.preventDefault;
                    const x = e.pageX;
                    const y = e.pageY;
                    let left = x - mx + dleft; //移动后的新位置
                    let top = y - my + dtop; //移动后的新位置
                    if (left < 0) left = 0;
                    if (left > maxX) left = maxX;
                    if (top < 0) top = 0;
                    if (top > maxY) top = maxY;

                    odiv.style.left = left + "px";
                    odiv.style.top = top + "px";
                    odiv.style.marginLeft = 0;
                    odiv.style.marginTop = 0;
                };
                document.onmouseup = () => {
                    document.onmousemove = null;
                };
            };
        }
    },
    resize: {
        // PC端窗口缩放
        mounted(el: any, binding: any, vnode: any) {
            // 如果传递了false就不启用指令，反之true undefined null 不传 则启动
            if (!binding.value && (binding.value ?? "") !== "") return;
            // 给选定的元素绑定name属性 设置name为resize区分只有该元素可以缩放
            el.name = "resize";
            // 八个方位对应
            const mouseDir: any = {
                top: "n-resize", //上
                bottom: "s-resize", //下
                left: "w-resize", //左
                right: "e-resize", //右
                topright: "ne-resize", //右上
                topleft: "nw-resize", //左上
                bottomleft: "sw-resize", //左下
                bottomright: "se-resize" //右下
            };
            // 记录被修改元素的原始位置大小，以及变更方向
            const pos = { width: 0, height: 0, top: 0, left: 0, x: 0, y: 0, dir: "" };
            // 获取鼠标所在方位
            const getDirection = (ev: any): string => {
                let dir = "";
                const xP = ev.offsetX;
                const yP = ev.offsetY;
                const offset = 12; //内边距为多少时触发
                // 计算是那个方位
                if (yP < offset) dir += "top";
                else if (yP > ev.toElement.clientHeight - offset) dir += "bottom";
                if (xP < offset) dir += "left";
                else if (xP > ev.toElement.clientWidth - offset) dir += "right";
                return dir;
            };
            // 计算移动距离
            const computedDistance = (pre: any, cur: any): any => {
                return [cur.x - pre.x, cur.y - pre.y];
            };
            //数据重置
            const resetData = () => {
                pos.width = 0;
                pos.height = 0;
                pos.top = 0;
                pos.left = 0;
                pos.x = 0;
                pos.y = 0;
                pos.dir = "";
                document.onmousemove = null;
            };
            // 变更尺寸方法
            const changeSize = (e: any) => {
                // 两个点之间的差值，计算鼠标位移数值
                const [disX, disY] = computedDistance(
                    { x: pos.x, y: pos.y },
                    { x: e.pageX, y: e.pageY }
                );
                const addWid = pos.width + disX;
                const subWid = pos.width - disX;
                const addHig = pos.height + disY;
                const subHig = pos.height - disY;
                const minX = 200;
                const minY = 200;
                //上下左右的变更方法
                const top = () => {
                    if (subHig <= minY) return; //不能小于最小最高
                    el.style.height = subHig + "px";
                    el.style.top = pos.top + disY + "px";
                }; // 上
                const bottom = () => {
                    el.style.height = addHig + "px";
                }; // 下
                const left = () => {
                    if (subWid <= minX) return; //不能小于最小宽度
                    el.style.width = subWid + "px";
                    el.style.left = pos.left + disX + "px";
                }; // 左
                const right = () => {
                    el.style.width = addWid + "px";
                }; // 右
                // 变更方位及其修改方法映射
                const doFn: any = {
                    top, //上
                    bottom, //下
                    left, //左
                    right, //右
                    topright: () => {
                        top();
                        right();
                    }, //右上
                    topleft: () => {
                        top();
                        left();
                    }, //左上
                    bottomleft: () => {
                        bottom();
                        left();
                    }, //左下
                    bottomright: () => {
                        bottom();
                        right();
                    } //右下
                };
                doFn[pos.dir]();
            };
            //鼠标按下 触发变更事件
            el.onmousedown = (e: any) => {
                if (e.target.name !== "resize") return;
                let d = getDirection(e);
                //当位置为四个边和四个角才开启尺寸修改
                if (mouseDir[d]) {
                    pos.width = el.clientWidth;
                    pos.height = el.clientHeight;
                    pos.top = el.offsetTop;
                    pos.left = el.offsetLeft;
                    pos.x = e.pageX;
                    pos.y = e.pageY;
                    pos.dir = d;
                    document.onmousemove = changeSize;
                }
                document.onmouseup = resetData;
            };

            /** 鼠标样式变更 */
            const changeShowCursor = (e: any) => {
                e.preventDefault();
                el.style.cursor = "default"; //先恢复鼠标默认
                if (e.target.name !== "resize") return;
                // 修改鼠标显示效果
                let d = getDirection(e);
                // 确定是某个方位的动向
                el.style.cursor = mouseDir[d] || "default";
            };
            el.onmousemove = changeShowCursor; //监听根元素上移动的鼠标事件
        }

    }
};

export default (app: App) => {
    //批量注册指令
    // @ts-ignore
    Object.entries(directives).forEach(([key, fn]) => {
        app.directive(key, fn);
    });
};
