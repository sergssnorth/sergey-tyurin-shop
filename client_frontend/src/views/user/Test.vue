<template>
    <!-- Расположение на всех экранах
    <div class="container-fluid">
        <div class="d-block d-sm-none">Видно только на xs</div>
        <div class="d-none d-sm-block d-md-none">Видно только на sm</div>
        <div class="d-none d-md-block d-lg-none">Видно только на md</div>
        <div class="d-none d-lg-block d-xl-none">Видно только на lg</div>
        <div class="d-none d-xl-block d-xxl-none">Видно только на xl</div>
        <div class="d-none d-sm-block d-xl-none d-xxl-block d-lg-none d-xl-block d-md-none d-lg-block d-sm-none d-md-block">Видно на всех</div>
    </div> -->
    
    <div class="container-fluid">
        <div class="d-block d-sm-none"><!-- Видно на XS --> Видно только на xs</div>
        <div class="d-none d-sm-block d-md-none"> <!-- Видно на SM --> Видно только на sm</div>
        <div class="d-none d-md-block d-lg-none"><!-- Видно на MD --> Видно только на md</div>
        <div class="d-none d-lg-block d-xl-none"><!-- Видно на LG --> Видно только на lg</div>
        <div class="d-none d-xl-block d-xxl-none"><!-- Видно на XL --> Видно только на xl</div>
        <div class="d-none d-sm-block d-xl-none d-xxl-block d-lg-none d-xl-block d-md-none d-lg-block d-sm-none d-md-block"><!-- Видно на XXL -->Видно на всех</div>
    </div>
</template>


<script>
export default {
    name: 'Test',
    data() {
        return {
            
        }
    },
}

</script>