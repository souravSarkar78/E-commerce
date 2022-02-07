<template>
    <div class="sidebar fixed top-0 h-screen p-2 overflow-y-auto text-center bg-red-300 z-20">
        <!-- <div v-for="i in 100" key:"i">{{i}}</div> -->
        <div @click="OpenLeftNavbar()" class="">
          <p class="text-2xl relative -right-20 md:hidden">
            <fa icon="window-close" />
          </p>
            <div class="bg-red-500">
              <NuxtLink to="AllProducts">Products</NuxtLink>
            </div>
        </div>
        {{this.$store.state.NavController.leftSidebarOpen}}
    </div>
</template>

<script>
export default {
  methods: {
    OpenLeftNavbar () {
      this.$store.commit('NavController/setOpenLeftSidebar', 0)
      document.body.style.overflow = 'scroll'
    }
  }
}
</script>
