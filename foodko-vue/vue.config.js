const { defineConfig } = require('@vue/cli-service')
const defaultSettings = require('./src/settings.js')
const name = defaultSettings.title // 网址标题
const port = 8013 // 端口配置
module.exports = defineConfig({
  publicPath: '/',
  outputDir: 'dist',
  assetsDir: 'static',
  lintOnSave: false,
  transpileDependencies: true,
  devServer: {
    // hot: true,
    port: port,
    open: true,
    // disableHostCheck: true,
    // overlay: {
    //   warnings: false,
    //   errors: true
    // },
    proxy: process.env.VUE_APP_BASE_API,
    // before(app) {
    //   /**
    //     * 我使用的是Visual Studio Code 所以这边传的编辑器类型是code
    //     * 编辑器类型在文章下面了，自己找吧。
    //     */
    //   app.use('/__open-in-editor', openInEditor(['code', 'code-inside']))
    // },
    headers: {
      'Access-Control-Allow-Origin': '*',
    },
    // before: require('./mock/mock-server.js')
  },
})
