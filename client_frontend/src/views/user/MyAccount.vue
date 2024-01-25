<template>
    <template v-if="$store.state.isAuthenticated">
        <p>Привет пользователь</p>
    </template>
    <template v-else>
        <LogIn />
    </template>
</template>

<script>
import LogIn from '@/components/LogIn'


export default {
    name: 'MyAccount',
    data() {
        return {
            
        }
    },
    components: {
        LogIn
    }
}

</script>
