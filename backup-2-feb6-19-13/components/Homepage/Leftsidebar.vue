<template>
    <div class="sidebar fixed top-0 bottom-0 p-2 overflow-y-auto text-center bg-red-300 z-10">
        <!-- <div v-for="i in 100" key:"i">{{i}}</div> -->
        <div @click="OpenLeftNavbar()" class="flex flex-col">
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
            <fa icon="window-close" />
        </div>
        {{this.$store.state.NavController.leftSidebarOpen}}
    </div>
</template>

<script>
export default {
  methods: {
    OpenLeftNavbar () {
      this.$store.commit('NavController/setOpenLeftSidebar', 0)
    }
  }
}
</script>
