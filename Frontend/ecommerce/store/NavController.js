export const state = () => ({
  leftSidebarOpen: 0
})

export const mutations = {
  setOpenLeftSidebar (state, payload) {
    state.leftSidebarOpen = !state.leftSidebarOpen
  }
}

export const action = { }

// export const getters = {
//   getLeftSidebarStatus: state => state.leftSidebarOpen
// }
