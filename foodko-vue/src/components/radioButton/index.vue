<template>
  <div>
    <div class="operation_flex">
      <div>
        <slot name="search">
          <el-input
            v-model="searchVal"
            :placeholder="(searchTip || lang.searchNumberOrDesc)"
            clearable
            :style="{'width': Number(searchWidth) + 'px'}"
            @keyup.enter.native="search"
            @keyup.native="searchVal = searchVal.replace(/\'/g, '')"
            @clear="search"
          >
            <el-button slot="append" icon="el-icon-search" @click="search"></el-button>
          </el-input>
        </slot>
        <slot name="inputRight"></slot>
        <slot name="default">
          <span v-if="isShowBtn" style="display: inline-block; margin: 0 10px;">
            <slot name="buttonLeft"></slot>
            <template v-for="(item, k) in btnList">
              <template v-if="item.btnPer/**RBAC按钮 */">
                <el-button
                  :key="k"
                  v-btnPer="item.btnPer"
                  :label="item.value"
                  :type="item.styleType"
                  :disabled="btnDisabled[item.value] || false"
                  @click="clickGroup(item.value)"
                >
                  <i class="iconsize iconfont" :class="item.icon"></i>
                  {{ item.tooltipContent }}
                </el-button>
              </template>
              <template v-else-if="item.btnPerArg/**RBAC按钮 arg传参 */">
                <el-button
                  v-btnPer:[item.btnPerArg]
                  :key="k"
                  :label="item.value"
                  :type="item.styleType"
                  :disabled="btnDisabled[item.value] || false"
                  @click="clickGroup(item.value)"
                >
                  <i class="iconsize iconfont" :class="item.icon"></i>
                  {{ item.tooltipContent }}
                </el-button>
              </template>
              <template v-else-if="item.btncon/**条件按钮 */">
                <el-button
                  :key="k"
                  v-btncon="item.btncon"
                  :label="item.value"
                  :type="item.styleType"
                  :disabled="btnDisabled[item.value] || false"
                  @click="clickGroup(item.value)"
                >
                  <i class="iconsize iconfont" :class="item.icon"></i>
                  {{ item.tooltipContent }}
                </el-button>
              </template>
              <template v-else>
                <el-button
                  :key="k"
                  :label="item.value/**普通按钮 */"
                  :type="item.styleType"
                  :disabled="btnDisabled[item.value] || false"
                  @click="clickGroup(item.value)"
                >
                  <i class="iconsize iconfont" :class="item.icon"></i>
                  {{ item.tooltipContent }}
                </el-button>
              </template>
            </template>
          </span>
        </slot>
        <warnInfo v-if="tabTipText">{{ tabTipText }}</warnInfo>
      </div>
      <div>
        <slot name="right"></slot>
      </div>
    </div>
  </div>
</template>

<script>
import warnInfo from '@/components/WarnInfo/index.vue'
export default {
  name: 'TabOperation',
  components: { warnInfo },
  props: {
    // 搜索框的提示文本
    searchTip: {
      type: String,
      default: ''
    },
    searchValue: {
      type: String,
      default: ''
    },
    // 搜索框的宽度
    searchWidth: {
      type: String,
      default: '250'
    },
    btnProps: {
      type: Object,
      default: () => {
        return {
          icon: {}, // 图标
          text: {}, // 文字
          styleType: {}, // 样式
          disabled: {}, // 禁用
          show: {}, // 显示
          btnOrder: [] // 排序
        }
      }
    },
    // 权限按钮配置
    btnPers: {
      type: Object,
      default: () => { return {} }
    },
    // 表格选中
    selected: {
      type: Array,
      default: () => []
    },
    // 粘贴内容的key，粘贴按钮有关
    copyKey: {
      type: String,
      default: 'bomTableCopyData'
    },
    isPermission: {
      type: Boolean,
      default: true
    },
    disabled: {
      type: Boolean,
      default: false
    },
    tabTipText: {
      type: String,
      default: ''
    },
    isShowBtn: {
      type: Boolean,
      default: true
    }
  },
  data() {
    return {
      lang: this.$store.getters.lang,
      searchVal: this.searchValue,
      radioGroupVal: '',
      // 最高等级的禁用
      bDisable: {},
      copyData: ''
    }
  },
  computed: {
    btnPropObj({ btnProps }) {
      return {
        icon: btnProps.icon || {}, // 图标
        text: btnProps.text || {}, // 文字
        disabled: btnProps.disabled || {}, // 禁用
        styleType: btnProps.styleType || {}, // 样式
        show: btnProps.show || {}, // 显示
        btnOrder: btnProps.btnOrder || [] // 排序
      }
    },
    originBtnData({ btnPers, btnPropObj }) {
      return {
        show: {
          add: false,
          create: false,
          del: false,
          paste: false,
          enable: false,
          disable: false,
          ...btnPropObj.icon,
          ...btnPropObj.show
        },
        text: {
          add: this.lang.add1,
          create: this.lang.create,
          del: this.lang.delete,
          paste: this.lang.paste,
          enable: this.lang.enable,
          disable: this.lang.disable,
          ...btnPropObj.text
        },
        icon: {
          add: 'iconicon_add',
          create: 'iconicon_add',
          del: 'iconicon_trash',
          paste: 'iconniantie',
          enable: 'iconicon_succeed',
          disable: 'iconjinyong',
          ...btnPropObj.icon
        },
        styleType: btnPropObj.styleType,
        btnPers
      }
    },
    // 按钮列表
    btnList({ originBtnData, btnPropObj }) {
      const order = [...new Set([...btnPropObj.btnOrder, 'add', 'create', 'del', 'paste', 'enable', 'disable', ...Object.keys(btnPropObj.icon)])]
      const list = []
      order.forEach(item => {
        if (originBtnData.show[item]) {
          list.push({
            tooltipContent: originBtnData.text[item],
            value: item,
            btnPer: (originBtnData.btnPers.btnper || {})[item] || '',
            btncon: (originBtnData.btnPers.btncon || {})[item] || '',
            btnPerArg: (originBtnData.btnPers.btnperarg || {})[item] || '',
            icon: originBtnData.icon[item],
            styleType: originBtnData.styleType[item]
          })
        }
      })
      return list
    },
    // 按钮禁用的自动处理
    btnDisabled({ bDisable, selected, copyData, btnPropObj }) {
      return Object.assign({
        del: !selected.length,
        paste: !copyData,
        enable: !selected.length,
        disable: !selected.length,
        ...btnPropObj.disabled
      }, bDisable)
    }
  },
  watch: {
    searchVal(newVal, oldVal) {
      this.$emit('update:searchValue', newVal)
    }
  },
  mounted() {
    this.updateCopyData()
  },
  methods: {
    updateCopyData() {
      try {
        this.copyData = JSON.parse(sessionStorage.getItem(this.copyKey))
      } catch {
        this.copyData = ''
      }
    },
    clickGroup(val) {
      if (!val) return
      switch (val) {
        case 'add':
          // 添加
          this.$emit('handleAdd', this.selected)
          this.radioGroupVal = ''
          break
        case 'del':
          // 删除
          this.$confirm(`${this.lang.operationDelDatas}？`, this.lang.batchDelete, { type: 'warning' }).then(() => {
            this.$emit('handleDel', this.selected)
          })
          this.radioGroupVal = ''
          break
        case 'paste':
          // 粘贴
          this.$emit('handlePaste', this.copyData)
          this.radioGroupVal = ''
          break
        default: {
          const eventName = 'handle' + val
          this.$emit(eventName)
          this.radioGroupVal = ''
        }
      }
    },
    search() {
      this.$emit('update:searchValue', this.searchVal)
      this.$emit('search', this.searchVal)
    }
  }
}
</script>

<style lang="scss" scoped>
::v-deep .operation_flex {
  display: flex;
  justify-content: space-between;
}
::v-deep .el-radio-group {
  label {
    margin: 0;
  }
  .bomAction {
    border: none;
  }
}
::v-deep .iconsize {
  font-size: 12px !important;
}

::v-deep .dialog-wrap {
  .el-dialog {
    border-radius: 4px;
  }

  .el-dialog__footer {
    padding: 16px;
    display: flex;
    justify-content: flex-end;
    border-radius: 4px 4px 0 0;
    .cancel-btn{
      width: 72px;
      height: 36px;
      padding: 12px 24px;
      background: #74788D;
      font-size: 12px;
    }
    .submit-btn{
      width: 108px;
      height: 36px;
      padding: 12px 44px;
      background: #556EE6;
      font-size: 12px;
    }
  }
  .el-dialog__body {
    padding: 16px 16px 18px;
  }
  .content {
    .iconar-alert {
      color: #F1B44C;
      font-size: 20px;
      line-height: 20px;
      vertical-align:middle;
      padding-right: 12px;
    }
    span {
      line-height: 20px;
      font-size: 14px;
    }
  }
}
</style>
