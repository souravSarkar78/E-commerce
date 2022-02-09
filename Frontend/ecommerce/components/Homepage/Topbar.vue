<template>
  <div
    class="
      fixed
      top-0
      h-14
      w-full
      text-center
      duration-75
      flex
      flex-wrap
      justify-center
      z-5
      bg-gray-700
    "
  >
    <!-- //fixed sorale neme jacche body -->
    <div
      class="
        inner-container
        w-full
        m-1
        flex
        space-around
        items-center
        justify-around
      "
    >
      <div class="w-2/3 hidden">
        <p class="" @click="OpenLeftNavbar()">
          <fa :icon="['fas', 'align-justify']" />
        </p>
        <!-- <p class="hidden md:block">Searchbar</p> -->
      </div>
      <div class="w-2/3 hidden md:block">
      <NuxtLink to="/">Logo/Home</NuxtLink>
      </div>
      <div class="w-2/3">
      <SearchBar />
      </div>
      <div class="w-2/3 text-white  hidden md:block">
        <fa :icon="['fab', 'github']" />
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
