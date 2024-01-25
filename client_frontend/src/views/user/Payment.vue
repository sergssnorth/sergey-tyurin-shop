<template>

</template>

<script>
export default {
    name: 'Payment',
    data() {
        return {
            user_id: 0,
            accountInformation: {
                client_delivery_information: [
                    {
                        region: "",
                        city: "",
                        street: "",
                        building: ""
                    }
                ],
                name: "",
                sname: "",
                email: "",
                phone: ""
            },
            cart: {
                items: []
            },
            card: {},
            errors: []
        }
    },
}

</script>
