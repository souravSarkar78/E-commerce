<template>
    <div class="sidebar fixed top-0 md:top-14 h-screen p-2 overflow-y-auto text-center bg-yellow-600 z-20">
        <!-- <div v-for="i in 100" key:"i">{{i}}</div> -->
        <div @click="OpenLeftNavbar()" class="">
          <p class="text-2xl relative float-right right-4 md:hidden">
            <fa icon="window-close" />
          </p>
            <div class="bg-red-500 relative top-10 my-2">
              <NuxtLink to="/">Logo/Home</NuxtLink>
            </div>
            <div class="bg-red-500 relative top-10 my-2">
              <NuxtLink to="Products">Products</NuxtLink>
            </div>
            <div class="bg-red-500 relative top-10 my-2">
              <NuxtLink to="MyAccount">My Account</NuxtLink>
            </div>
        </div>
        <!-- {{this.$store.state.NavController.leftSidebarOpen}} -->
    </div>
</template>

<script>
export default {
  methods: {
    OpenLeftNavbar () {
      this.$store.commit('NavController/setOpenLeftSidebar', 0)
      document.body.style.overflowY = 'scroll'
    }
  }
}
</script>
