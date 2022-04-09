<template>
    <el-container>
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
            <el-row>
                <el-col :span="3">
                    <el-div class = "header">Output</el-div>
                </el-col>
            </el-row>
            <el-row>
                <el-tag type="success">Z3 output</el-tag>
            </el-row>
            <el-input
            type="textarea"
            readonly
            :autosize="{ minRows: 2, maxRows: 20}"
            v-model="zoutput">
            </el-input>
            <el-row>
                <el-col :span="3">
                    <el-div class = "header">Summary</el-div>
                </el-col>
            </el-row>
            <el-col span="12">
                <div align="right" >
                    <el-row>
                        <el-div class = "body">
                            <el-div v-html="'Command :&nbsp'"></el-div>
                        </el-div>
                    </el-row>
                    <el-row>
                        <el-div class = "body">
                            <el-div v-html="'Running time :&nbsp'"></el-div>
                        </el-div>
                    </el-row>
                    <el-row>
                        <el-div class = "body">
                            <el-div v-html="'Version :&nbsp'"></el-div>
                        </el-div>
                    </el-row>
                </div>
            </el-col>
            <el-col span="12">
                <div align="left" >
                    <el-row>
                        <el-div class = "body">
                            <el-div v-text = "cmd"></el-div>
                        </el-div>
                    </el-row>
                    <el-row>
                        <el-div class = "body">
                            <el-div v-text = "time"></el-div>
                        </el-div>
                    </el-row>
                    <el-row>
                        <el-div class = "body">
                            <el-div v-text = "ver"></el-div>
                        </el-div>
                    </el-row>
                </div>
            </el-col>
        </el-aside>
    </el-container>
        <el-footer>
            <el-row>
                <el-col >
                    <el-div class = "header">Resources</el-div>
                </el-col>
            </el-row>
            <el-row>
                <el-div class = "body">
                    <el-div v-html="'You may be interested in'"></el-div>
                </el-div>
            </el-row>
            <el-container>
                <el-aside width="49.5%">
                <div align="right" >
                    <el-row>
                        <el-div class = "body"> <el-link type="info" v-html="ref1"></el-link> </el-div>
                    </el-row>
                    <el-row>
                        <el-div class = "body"> <el-link type="info" v-html="ref5"></el-link> </el-div>
                    </el-row>
                </div>
                </el-aside>
                <el-aside width="1%">
                </el-aside>
                <el-aside width="49.5%">
                <div align="left" >
                    <el-row>
                        <el-div class = "body"> <el-link type="info" v-html="ref3"></el-link> </el-div>
                    </el-row>
                    <el-row>
                        <el-div class = "body"> <el-link type="info" v-html="ref4"></el-link> </el-div>
                    </el-row>
                </div>
                </el-aside>
            </el-container>
            <el-row>
                <el-div class = "body">
                <el-link type="info" v-html="ref2"></el-link>
                </el-div>
            </el-row>
        </el-footer>
    </el-container>
</template>
<script>
export default {
    data() {
        return {
            textarea: this.$route.params.text,
            zoutput : this.$route.params.output,
            ref1 : "https://www.philipzucker.com/z3-rise4fun/guide.html",
            ref2 : "https://github.com/philzook58/z3_tutorial",
            ref3 : "https://theory.stanford.edu/~nikolaj/programmingz3.html",
            ref4 : "https://ericpony.github.io/z3py-tutorial/guide-examples.htm",
            ref5 : "https://yurichev.com/writings/SAT_SMT_by_example.pdf",
            //time : this.$route.params.time,
            time : '30s',
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
                value: '30',
            cmd : 'z3 -in -t:30',
            ver : 'z3-4.8.5'
        }
    },
    methods: {
        handleReset() {
            this.textarea = '; Variable declarations\n (declare-fun a () Int)\n (declare-fun b () Int)\n (declare-fun c () Int)\n\n ; Constraints\n (assert (> a 0))\n (assert (> b 0))\n (assert (> c 0))\n (assert (= (+ (* a a) (* b b)) (* c c)))\n\n ; Solve\n (check-sat)\n (get-model)'
        },
        handleExecute() {
            this.cmd = 'z3 -in -t:' + this.value
            var param = {
                    "z3input": this.textarea,
                    "timeout" : this.value
                }
            //this.axios.post("/z3/output/generate", param).then(
            //    res => {
            //        this.zoutput = res.data
            //        this.time = res.statusText
            //        console.log(res)
            //    }
            //).catch((error) => {
            //    console.error(error);
            //})
        }
    }
}
</script>
