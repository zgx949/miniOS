import { createStore } from 'vuex';
import axios from 'axios'; // 假设你使用axios进行API请求

// 定义状态
const state = {
    user: null,
    loading: false,
    error: null,
};

// 定义getter
const getters = {
    isLoggedIn: (state) => !!state.user,
};

// 定义mutations
const mutations = {
    SET_USER(state, newUser) {
        state.user = newUser;
    },
    SET_LOADING(state, isLoading) {
        state.loading = isLoading;
    },
    SET_ERROR(state, newError) {
        state.error = newError;
    },
};

// 定义actions
const actions = {
    async login({ commit }, credentials) {
        commit('SET_LOADING', true);
        try {
            const response = await axios.post('/api/login', credentials);
            commit('SET_USER', response.data.user);
        } catch (error) {
            commit('SET_ERROR', error.message);
        } finally {
            commit('SET_LOADING', false);
        }
    },
};

export default createStore({
    state,
    getters,
    mutations,
    actions,
});