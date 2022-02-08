<template>
  <div class="shadow-lg rounded-lg">
    <img
      src="@/static/images/product.webp"
      alt="product_img"
      class="rounded-t-lg"
    />
    <div class="m-2">
      <p class="title font-light">This is produt title of rwo lines</p>
      <div class="flex gap-1">
          <p class="price font-medium">$10</p>
          <p class="font-light text-red-500 text-sm line-through">$10</p>
      </div>
      <div class="buttons flex flex-col md:flex-row gap-1 justify-between">
        <button
          class="
            bg-gradient-to-r
            from-red-600
            to-red-500
            hover:from-red-500 hover:to-red-600
            rounded-full
            py-2
            px-4
            duration-75
          "
        >
          Add to cart
        </button>
        <button
          class="
            bg-gradient-to-r
            from-blue-600
            to-red-400
            hover:from-green-400 hover:to-yellow-600
            rounded-full
            py-2
            px-4
            duration-75
          "
        >
          View product
        </button>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped >
.title {
  font-size: $title-text;
}
.price{
    font-size: 1.2rem;
    // color: red;
    // font-weight: 400;
}
.buttons {
  color: white;
  font-size: $products-button;
  font-size: 0.8rem;
}
</style>
