<template>
  <div class="">
    <Leftsidebar class="duration-200 w-80 md:w-60 md:left-0 bg-green-500" v-bind:class="{ 'left-0' : this.$store.state.NavController.leftSidebarOpen, '-left-80' : !this.$store.state.NavController.leftSidebarOpen }"/>
    <div class="boder-box bottom-0 bg-green-500 left-0 md:left-60 duration-200 w-full md:w-auto h-fit" v-bind:class="{ 'left-60' : this.$store.state.NavController.leftSidebarOpen }">
      <Topbar class=""/>
      <Nuxt class="mt-14 md:ml-60" />
      <Downbar class="md:hidden"/>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
    }
  }
}
</script>

<style lang="scss" scoped>
.page {
  margin-top: 4rem;
}
</style>
