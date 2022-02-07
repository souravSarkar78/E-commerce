<template>
    <div class="fixed top-0 h-14 md:h-20 left-0 md:left-60 right-0 text-center bg-green-300 duration-75 flex justify-center z-10">   <!-- //fixed sorale neme jacche body -->
        <div class="inner-container w-full md:w-10/12 m-1 bg-blue-500 flex space-around items-center justify-around">
        <div class="w-2/3">
        <p class="md:hidden" @click="OpenLeftNavbar()"><fa :icon="['fas','align-justify']" /></p>
        <p class="hidden md:block">Searchbar</p>
        </div>
        <div class="w-2/3">
            <NuxtLink to="/">Logo/Home</NuxtLink>
        </div>
        <div class="w-2/3">
        <fa :icon="['fab','github']" />
        </div>
        </div>
    </div>
</template>

<script>
export default {
  methods: {
    OpenLeftNavbar () {
      this.$store.commit('NavController/setOpenLeftSidebar', 1)
      document.body.style.overflow = 'hidden'
    }
  }
}
</script>
