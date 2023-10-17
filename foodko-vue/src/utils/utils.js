// message
import { ElMessageBox } from 'element-plus'
function showMessageBox(type, message, showCancel) {
  const typeMap = {
    'error': '系统错误',
    'success': '成功',
    'warning': '警告',
  }
  return ElMessageBox.alert(message.replace(/\n/g, '<br/>'), typeMap[type], {
    confirmButtonText: '确定',
    showCancelButton: showCancel,
    cancelButtonClass: '取消',
    dangerouslyUseHTMLString: true,
    showClose: false,
    type: type
  })
}

export default {
  showMessageBox
}