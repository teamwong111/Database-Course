import Vue from 'vue'
import VueRouter from 'vue-router'

// 路由懒加载
const Home = () => import('../components/Home.vue')
const Stat = () => import('../components/Stat.vue')

const Login = () => import('../pages/user/Login.vue')
const Regist = () => import('../pages/user/Regist.vue')
const Plan = () => import('../pages/plan/Plan.vue')
const Record = () => import('../pages/record/Record.vue')
const Allshare = () => import('../pages/share/Allshare.vue')
const Bodydata = () => import('../pages/account/Bodydata.vue')
const Center = () => import('../pages/account/Center.vue')
const Modifypassword = () => import('../pages/account/Modifypassword.vue')

Vue.use(VueRouter)

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/stat', component: Stat },
  { path: '/login', component: Login },
  { path: '/regist', component: Regist },
  { path: '/home',
    component: Home,
    children: [
      { path: '/plan', component: Plan },
      { path: '/record', component: Record },
      { path: '/allshare', component: Allshare },
      { path: '/bodydata', component: Bodydata },
      { path: '/center', component: Center },
      { path: '/modifypassword', component: Modifypassword }
    ] }

]

const router = new VueRouter({
  routes
})

// 挂载路由导航守卫
router.beforeEach((to, from, next) => {
  if (to.path === '/login') return next()
  if (to.path === '/regist') return next()
  const account = window.sessionStorage.getItem('account')
  if (!account) return next('/login')
  next()
})

export default router
