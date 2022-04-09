import Vue from 'vue'
import Router from 'vue-router'
import Z3 from '@/pages/z3'
import Input from '@/pages/input'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/z3',
      name: 'z3',
      component: Z3 
    },
    {
      path: '/',
      name: 'input',
      component: Input 
    }
  ]
})
