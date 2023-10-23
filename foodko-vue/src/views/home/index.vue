<template>
  <div class="home_content">
    <Card :dx="10" :dy="80">
      <span class="jrink_title">Jrink</span>
      <el-progress :text-inside="true" :stroke-width="26" :percentage="processNum" />
      <el-button circle size="large" class="jrink_icon" :icon="MilkTea" @click="addProcessNum()"></el-button>
    </Card>
  </div>
  <Card :dx="100" :dy="300" :dwidth="350" dheight="120" style="padding: 10px; position: relative;">
    <div class="Date">
      <div an class="info-small">{{ currentDate }}</div>
      <div class="info-small">{{ lunarDay }}</div>
    </div>
    <div class="info-large">{{ currentTime }}</div>
  </Card>
  <Card :dx="500" :dy="70" :dwidth="200" dheight="100" @click="goQuestion" class="Card">
    <div class="question">
      <div class="questionContent">{{ questionsContent }}</div>
      <div class="isCompleted"><el-checkbox label="今日已完成" name="type" checked="checked" />
      </div>
    </div>
  </Card>
</template>
<script setup>
import Card from '@/components/card/index.vue'
import { getLunar } from 'chinese-lunar-calendar'
import { ref, onMounted, onUnmounted } from 'vue'
import { MilkTea } from '@element-plus/icons-vue'
import { getQuestion } from '@/views/database/questions/api';
import { useRouter } from 'vue-router';
const router = useRouter()
const currentTime = ref('');
const currentDate = ref(new Date().toLocaleDateString());
const lunarDay = ref('');
const updateClock = () => {
  const now = new Date();
  const lunarDate = getLunar(now.getFullYear(), now.getMonth() + 1, now.getDate());
  // console.log(lunarDate)
  lunarDay.value = lunarDate.dateStr;
  // 获取当前时间并格式化为 HH:mm
  const options = { hour: '2-digit', minute: '2-digit', hour12: false, minimumIntegerDigits: 2 };
  currentTime.value = now.toLocaleTimeString(undefined, options);
};
const intervalId = setInterval(updateClock, 1000);
const params = {
  id: '',
  number: 1
};
const questionsContent = ref({})
getQuestion(params).then(res => {
  console.log('API 响应数据:', res.result);
  if (res.status === '1' && res.result && res.result.length > 0) {
    questionsContent.value = res.result[0].content;
  }
});
const goQuestion = () => {
  router.push({
    path: "/database/questionAnswer",
    query: { type: 1 }
  })
}
onMounted(() => {
  updateClock()
  getQuestion(params)
});
onUnmounted(() => {
  clearInterval(intervalId); // 清除定时器
});
const processNum = ref(10)
function addProcessNum(num = 10) {
  processNum.value = processNum.value + num
}
</script>

<style lang="scss" scoped>
.home_content {
  .jrink_title {
    font-size: 24px;

  }

  .jrink_icon {
    font-size: large;
    position: absolute;
    top: 60px;
    right: -6px;
    border-right-color: gray;
  }
}

.DateDay {
  width: 100%;
  height: 100%;

}

.Date {
  text-align: left;
  width: 100px;
  display: flex;
  flex-direction: column;

}


.info-small {
  font-size: 18px;
  color: rgba(128, 128, 128, 1);
  /* 小字体 */
}

.info-large {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 60px;
  /* 大字体 */
}

.question {
  text-align: left;
  font-size: 20px;
  font-weight: bold;
  cursor: pointer;
  position: relative;
  white-space: pre-line;
}



.isCompleted {
  position: absolute;
  top: 70px;
  left: 100px;
}

.Card {
  padding: 10px;
  position: relative;
}

.Card:active {
  background-color: beige;
}
</style>