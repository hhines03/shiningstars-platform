<!-- src/components/NavBar.vue -->
<template>
  <v-app-bar app color="primary" dark>
    <v-toolbar-title class="ma-2" @click="$router.push('/')">Shining Stars</v-toolbar-title>

    <!-- "Our Childcare" Dropdown Menu -->
    <v-menu offset-y>
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" text>Our Childcare</v-btn>
      </template>
      <v-list>
        <v-list-item to="/about"><v-list-item-title>About Us</v-list-item-title></v-list-item>
        <v-list-item to="/childsafety"><v-list-item-title>Child Safety</v-list-item-title></v-list-item>
        <v-list-item to="/newsletter"><v-list-item-title>Newsletter</v-list-item-title></v-list-item>
      </v-list>
    </v-menu>

    <!-- "Parent Area" Dropdown Menu -->
    <v-menu offset-y>
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" text>Parent Area</v-btn>
      </template>
      <v-list>
        <v-list-item to="/feecalculator"><v-list-item-title>Fee Calculator</v-list-item-title></v-list-item>
        <!-- Add other public parent pages here -->
      </v-list>
    </v-menu>

    <v-spacer></v-spacer>

    <v-btn to="/bookvisit">Book a Visit</v-btn>
    <v-btn to="/login" variant="outlined">Parent Login</v-btn>

  </v-app-bar>
</template>

<script setup>
// No script logic needed for this simple component
</script>

<style scoped>
.v-toolbar-title {
  cursor: pointer;
}
</style>