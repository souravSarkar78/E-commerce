<template>
    <div class="fixed md:relative bottom-0 h-14 md:h-12 w-full text-center bg-green-300 duration-75 flex justify-center">
        <div class="inner-container w-full m-1 bg-blue-500 flex space-around items-center justify-around">
        <NuxtLink to="MyOrders">
            <div class="">
                Orders
            </div>
        </NuxtLink>
        <NuxtLink to="AllProducts">Products</NuxtLink>
        <NuxtLink to="MyAccount">My account</NuxtLink>
        </div>
    </div>
</template>
