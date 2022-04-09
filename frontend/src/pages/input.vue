<template>
    <el-container>
        <el-aside width="49%">
            <el-row >
                <el-col :span="3">
                    <el-div class = "header">Input</el-div>
                </el-col>
                <div class="right-items" style="float: right;">
                    <el-button @click="handleReset" type="danger">Reset</el-button>
                    <el-button @click='handleExecute' type="success">Execute</el-button>
                </div>
            </el-row>
            <el-row>
                <el-tag type="success">SMT-LIB 2 script</el-tag>
            </el-row>
            <el-input
            type="textarea"
            :autosize="{ minRows: 2, maxRows: 30}"
            placeholder="Input..."
            v-model="textarea">
            </el-input>
            <el-row >
                <el-div class = "body">Timeout: </el-div>
                <el-select v-model="value" placeholder="请选择">
                    <el-option
                      v-for="item in options"
                      :key="item.value"
                      :label="item.label"
                      :value="item.value">
                    </el-option>
                </el-select>
            </el-row>
        </el-aside>
        <el-aside width="2%">
        </el-aside>
        <el-aside width="49%">
        </el-aside>
    </el-container>
</template>
<script>
export default {
    data() {
        return {
            textarea: '; Variable declarations\n (declare-fun a () Int)\n (declare-fun b () Int)\n (declare-fun c () Int)\n\n ; Constraints\n (assert (> a 0))\n (assert (> b 0))\n (assert (> c 0))\n (assert (= (+ (* a a) (* b b)) (* c c)))\n\n ; Solve\n (check-sat)\n (get-model)',
            zoutput: '',
            time: '',
            options: [{
                value: '30',
                label: '30s'
                }, {
                value: '60',
                label: '60s'
                }, {
                value: '120',
                label: '120s'
                }, {
                value: '300',
                label: '300s'
                }, {
                value: '600',
                label: '600s'
                }],
                value: '30'
        }
    },
    methods: {
        handleReset() {
            this.textarea = '; Variable declarations\n (declare-fun a () Int)\n (declare-fun b () Int)\n (declare-fun c () Int)\n\n ; Constraints\n (assert (> a 0))\n (assert (> b 0))\n (assert (> c 0))\n (assert (= (+ (* a a) (* b b)) (* c c)))\n\n ; Solve\n (check-sat)\n (get-model)'
        },
        handleExecute() {
            var param = {
                    "z3input": this.textarea,
                    "timeout" : this.value
                }
                    this.$router.push({
                        name: 'z3',
                        params:{
                            text : this.textarea,
                            output : this.zoutput,
                            time : this.time
                        }
                    })
            //this.axios.post("/z3/output/generate", param).then(
            //    res => {
            //        this.zoutput = res.data
            //        this.time = res.statusText
            //        console.log(res)
            //        this.$router.push({
            //            name: 'z3',
            //            params:{
            //                text : this.textarea,
            //                output : this.zoutput,
            //                time : this.time
            //            }
            //        })
            //    }
            //).catch((error) => {
            //    console.error(error);
            //})
        }
    }
}
</script>
