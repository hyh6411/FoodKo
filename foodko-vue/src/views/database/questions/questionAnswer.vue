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
import { ref, onMounted, toRefs } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const currentQuestionIndex = ref(0);
const questions = ref([]);
const userAnswers = ref([]);
const startAnswer = ref(true);
const currentQuestion = ref({}); // 当前显示的题目

const goToPreviousQuestion = () => {
    if (currentQuestionIndex.value > 0) {
        currentQuestionIndex.value--;
        currentQuestion.value = questions.value[currentQuestionIndex.value];
    }
};

const goToNextQuestion = () => {
    if (currentQuestionIndex.value < questions.value.length - 1) {
        currentQuestionIndex.value++;
        currentQuestion.value = questions.value[currentQuestionIndex.value];
    }
};

const submitAnswers = () => {
    // 处理用户提交答案的逻辑
    // 比较 userAnswers 和 questions 中的答案，计算得分，展示答题结果等
    // ...
};

const goAnswer = () => {
    const params = {
        id: '',
        number: 5
    };
    getQuestion(params).then(res => {
        console.log('API 响应数据:', res); // 输出API响应的数据，确保数据格式正确

        if (res.status === '1' && res.result && res.result.length > 0) {
            questions.value = res.result;
            currentQuestion.value = questions.value[0]; // 将当前题目设为第一道题

            // 检查 options 字段是否存在且不为 null 或 undefined
            if (currentQuestion.value.options && currentQuestion.value.options !== null && currentQuestion.value.options !== undefined) {
                // 替换掉字符串中的反斜杠，然后解析JSON
                const optionsString = currentQuestion.value.options.replace(/\\/g, '');
                currentQuestion.value.options = JSON.parse(optionsString);

                // 输出日志，确保获取到了正确的题目和选项数据
                console.log('题目数据：', currentQuestion.value);
                console.log('选项数据：', currentQuestion.value.options);
            } else {
                // 当 options 不存在或为 null 或 undefined 时的处理逻辑
                console.error('题目数据中的 options 字段不存在或为 null/undefined。');
                // 在这里添加适当的处理逻辑，例如显示错误信息或者使用默认选项。
            }

            startAnswer.value = false;
        }
    });
};




onMounted(() => {
    userAnswers.value = Array(questions.value.length).fill(null);
});


</script>

<style lang="scss" scoped>
.question {
    width: 100%;
    height: 800px;
    background-color: #e0dada;
    margin: 0 auto;
}

.text {
    font-size: 27px;
    font-weight: 400;
}
</style>