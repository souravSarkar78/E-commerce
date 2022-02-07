<template>
    <div class="fixed top-0 h-14 md:h-20 w-full text-center bg-green-300 duration-75 flex justify-center">
        <div class="inner-container w-full md:w-2/3 m-1 bg-blue-500 flex space-around items-center justify-around">
        <div class="w-2/3">
        <p @click="OpenLeftNavbar()"><fa :icon="['fas','align-justify']" /></p>
        </div>
        <div class="w-2/3">
            <NuxtLink to="/">Logo</NuxtLink>
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
    }
  }
}
</script>
