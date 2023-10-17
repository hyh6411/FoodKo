<template>
    <div class="question">
        <div class="questionPreview " v-if="startAnswer">
            <div class="text" style="text-align: left;">每日一练</div>
            <div class="text" style="margin: 200px 0 100px 0;">总共为{{ 10 }}题</div>
            <p style="color: rgba(128, 128, 128, 1);">全部为选择题，在选项中选择后点击确定</p>
            <div class="text" style="text-align: right; margin: 200px 20px 0 0;">
                <el-checkbox label="今日已完成" name="type" checked="checked" />
                <el-button style="margin-left: 10px;" @click="goAnswer()">开始</el-button>
            </div>
        </div>
        <div class="questionAnswer" v-else>
            <div class="text"><span>第{{ currentQuestionIndex + 1 }}题</span>{{ currentQuestion.content }}</div>
            <div class="text" v-for="(optionText, optionKey) in currentQuestion.options" :key="optionKey">
                <input type="radio" :id="optionKey" :name="'question_' + currentQuestionIndex" :value="optionKey"
                    v-model="userAnswers[currentQuestionIndex]" />
                <label :for="optionKey">{{ optionKey }}. {{ optionText }}</label>
            </div>
            <div class="answer">
                <div class="text">答案：{{ currentQuestion.answer }}</div>
                <div class="text">解释：{{ currentQuestion.explain }}</div>
            </div>
            <el-button @click="goToPreviousQuestion" v-if="currentQuestionIndex > 0">上一题</el-button>
            <el-button @click="goToNextQuestion" v-if="currentQuestionIndex < questions.length - 1">下一题</el-button>
            <el-button @click="submitAnswers" v-if="currentQuestionIndex === questions.length - 1">提交</el-button>
        </div>
    </div>
</template>
<script setup>
import { getQuestion } from './api.js';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
const route = useRoute();
const currentQuestion = ref({}); // 当前显示的题目
const currentQuestionIndex = ref(0);
const questions = ref([]);
const userAnswers = ref([]);
const startAnswer = ref(true);
const params = {
    id: '',
    number: 5
};

const submitAnswers = () => {
    // 处理用户提交答案的逻辑
    // 比较 userAnswers 和 questions 中的答案，计算得分，展示答题结果等
    // ...
};
// 获取题目数据
const goAnswer = () => {
    getQuestion(params).then(res => {
        console.log('API 响应数据:', res); // 输出API响应的数据，确保数据格式正确
        if (res.status === '1' && res.result && res.result.length > 0) {
            questions.value = res.result;
            // 解析每个题目的选项
            questions.value.forEach(question => {
                // 解析option字段中的JSON字符串
                const optionObj = JSON.parse(question.option);
                // 把获取到的选项对象赋给question.options
                question.options = optionObj;
                console.log(question)
            });
            currentQuestion.value = questions.value[0]; // 将当前题目设为第一道题
            // 选项数据
            console.log(currentQuestion.value.options)
            startAnswer.value = false;
        }
    });
};
// 上一题
const goToPreviousQuestion = () => {
    if (currentQuestionIndex.value > 0) {
        currentQuestionIndex.value--;
        currentQuestion.value = questions.value[currentQuestionIndex.value];
    }
};
// 下一题
const goToNextQuestion = () => {
    if (currentQuestionIndex.value < questions.value.length - 1) {
        currentQuestionIndex.value++;
        currentQuestion.value = questions.value[currentQuestionIndex.value];
    }
};
onMounted(() => {
    userAnswers.value = Array(questions.value.length).fill(null);
});
</script>
<style lang="scss" scoped>
.question {
    width: 100%;
    height: 800px;
    margin: 0 auto;
}

.text {
    font-size: 27px;
    font-weight: 400;
}
</style>