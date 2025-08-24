import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import HomeView from '@/views/HomeView.vue'
import ChildSafetyView from '@/views/ChildSafetyView.vue'
import FeeCalculatorView from '@/views/FeeCalculatorView.vue'
import NewsletterView from '@/views/NewsletterView.vue'
import ParentHubView from '@/views/ParentHubView.vue'
import BookVisitView from '@/views/BookVisitView.vue'
import AboutView from '@/views/AboutView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {path: '/login', name: 'login', component: LoginView},
    {path: '/', name: 'home', component: HomeView},
    {path: '/parenthub', name: 'parent_hub', component: ParentHubView},
    {path: '/childsafety', name: 'child_safety', component: ChildSafetyView},
    {path: '/bookvisit', name: 'book_visit', component: BookVisitView},
    {path: '/parenthub', name: 'parent_hub', component: ParentHubView},
    {path: '/about', name: 'about', component: AboutView},
    {path: '/feecalculator', name: 'fee_calculator', component: FeeCalculatorView},
    {path: '/newsletter', name: 'newsletter', component: NewsletterView},
  ]
})

export default router