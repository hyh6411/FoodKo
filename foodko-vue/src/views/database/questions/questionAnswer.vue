<template>
    <div class="question">
        <div class="questionPreview" v-if="startAnswer">
            <div class="titleTxt">{{ type == 1 ? '每日一练' : '无尽模式' }}</div>
            <div class="questionNum">{{ type == 1 ? '总共为10题' : '无尽模式' }}</div>
            <p class="tipsTxt">全部为选择题，在选项中选择后点击确定</p>
            <div class="btn">
                <el-checkbox label="今日已完成" name="type" checked="checked" disabled />
                <el-button class="start" @click="goAnswer()">开始</el-button>
            </div>
        </div>
        <div class="questionAnswer" v-else>
            <div class="questionIndex"><span>第{{ type == 1 ? currentQuestionIndex + 1 : questionNum + 1
            }}题、</span>{{
    currentQuestion.content }}</div>
            <div class="questionOptions">
                <div v-for="(optionText, optionKey) in currentQuestion.options" :key="optionKey" class="option_item">
                    <input type="radio" v-model="userAnswers[currentQuestionIndex]" :id="optionKey" :value="optionKey" />
                    <label :for="optionKey">{{ optionKey }}. {{ optionText }}</label>
                </div>
            </div>
            <div class="answerDiv" v-if="isAnswer">
                <div class="answer">正确答案：<span class="explain">{{ currentQuestion.answer }}){{ currentQuestion.explain
                }}</span>
                </div>
            </div>
            <div class="btn">
                <el-button @click="goToPreviousQuestion" :disabled="currentQuestionIndex <= 0"
                    v-if="questions.length !== 1">上一题</el-button>
                <el-button @click="submitAnswer" type="primary" v-if="!isAnswer">确定</el-button>
                <el-button @click="goToNextQuestion" v-if="currentQuestionIndex <= questions.length - 1 && isAnswer"
                    type="primary">
                    下一题
                </el-button>
                <el-button @click="submitAnswerAll"
                    v-if="currentQuestionIndex === questions.length - 1 && questions.length > 1" type="primary">
                    提交
                </el-button>
            </div>
        </div>
    </div>
</template>
<script setup>
import { getQuestion } from './api.js';
import { ref, onMounted, watch, computed } from 'vue';
import { useRoute } from 'vue-router';
import { ElMessage } from 'element-plus'


const route = useRoute();
const currentQuestion = ref({}); // 当前显示的题目
const currentQuestionIndex = ref(0);
const questions = ref([]);
const userAnswers = ref([]);
const startAnswer = ref(true);
const isAnswer = ref(false)
const type = route.query.type;
const questionNum = ref(0)
const params = {
    id: '',
    number: 10
};

const goAnswer = () => {
    console.log(type)
    if (type == 2) {
        params.number = 1;
    }
    // console.log(params)
    getQuestion(params).then(res => {
        console.log('API 响应数据:', res);
        if (res.status === '1' && res.result && res.result.length > 0) {
            // 使用 JSON.stringify 和 JSON.parse 进行深拷贝
            questions.value = JSON.parse(JSON.stringify(res.result));
            // 初始化 userAnswers 为包含足够元素数量的数组
            userAnswers.value = Array(questions.value.length).fill(null);
            // 解析每个题目的选项
            questions.value.forEach(question => {
                const optionObj = JSON.parse(question.option);
                question.options = optionObj;

                // 在每个题目对象上添加独立的 userAnswer 属性
                question.userAnswer = null; // 初始时用户的答案为空
                console.log(question);
            });
            currentQuestion.value = questions.value[0];
            startAnswer.value = false;
        }
    });
};

// 提交单个答案
const submitAnswer = () => {
    const selectedAnswer = userAnswers.value[currentQuestionIndex.value];
    if (!selectedAnswer) {
        ElMessage({
            message: '请选择答案',
            type: 'warning'
        })
        return
    }
    // 用户选择了答案，将答案存储到当前题目对象的userAnswer属性中
    questions.value[currentQuestionIndex.value].userAnswer = selectedAnswer;
    console.log(selectedAnswer)
    // 显示答案和解析
    isAnswer.value = true;
};

// computed获取当前题目的选项:
const currentAnswer = computed(() => {
    return userAnswers[currentIndex]
})

// 提交所有答案
const submitAnswerAll = () => {
    ElMessage({
        message: '提交成功',
        type: 'success'
    })
    for (let i = 0; i < questions.value.length; i++) {
        const question = questions.value[i]
        if (question.userAnswer) {
            console.log(`题号${i + 1},答案${question.userAnswer}`)
        }
    }
    // 重置到开始状态
    startAnswer.value = true
    // 重置数据
    currentQuestionIndex.value = 0
    questions.value = []
    userAnswers.value = []
};
// 获取题目数据
// 上一题
const goToPreviousQuestion = () => {
    if (currentQuestionIndex.value > 0) {
        currentQuestionIndex.value--;
        currentQuestion.value = questions.value[currentQuestionIndex.value];
        // 如果当前题目有用户答案，保持显示答案状态
        if (currentQuestion.value.userAnswer !== null) {
            isAnswer.value = true;
        } else {
            isAnswer.value = false;
        }
    }
};

// 下一题
const goToNextQuestion = () => {
    if (type == 2) {
        goAnswer()
        questionNum.value = questionNum.value + 1
        isAnswer.value = false
    }
    if (currentQuestionIndex.value < questions.value.length - 1) {
        currentQuestionIndex.value++;
        currentQuestion.value = questions.value[currentQuestionIndex.value];
        // 如果当前题目有用户答案，保持显示答案状态
        if (currentQuestion.value.userAnswer !== null) {
            isAnswer.value = true;
        } else {
            isAnswer.value = false;
        }
    }
};
onMounted(() => {
    userAnswers.value = Array(questions.value.length).fill(null);
    // console.log(type); // 输出 2
});
</script>
<style lang="scss" scoped>
.questionPreview {
    padding: 20px;
}

.question {
    width: 100%;
    height: 800px;

    .answerDiv {
        margin-top: 80px;
        color: rgb(156, 156, 156);
    }
}

.titleTxt {
    text-align: left;
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 20px;
    border-left: 7px solid var(--el-color-primary);
    padding-left: 10px;
}

.questionNum {
    font-size: 20px;
    font-weight: bold;
    margin: 200px 0 100px 0;
}

.tipsTxt {
    color: rgba(128, 128, 128, 1);
}

.start {
    margin-left: 10px;
}

.text {
    font-size: 27px;
    font-weight: 400;
}

.questionIndex {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 30px;
}

.questionAnswer {
    max-width: 500px;
    padding: 20px;
    margin-top: 80px;
    text-align: left;
}

.questionOptions {
    margin-top: 40px;
    font-size: 18px;
    margin-bottom: 30px;

    .option_item {
        margin-bottom: 8px;
    }
}

.btn {
    position: absolute;
    bottom: 100px;
    right: 20px;
    text-align: right;
}
</style>