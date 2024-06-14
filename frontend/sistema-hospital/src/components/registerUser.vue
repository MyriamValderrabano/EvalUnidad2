<template>
    <div class="min-h-screen bg-lime-200 flex flex-col justify-center py-5 sm:px-6 lg:px-8 px-6">
        
        <div class="flex  rounded-lg shadow-lg overflow-hidden mx-100 ">
            <div class="w-full p-8 lg:w-1/2">
                <Person></Person>
            </div>
            <div class="w-full p-8 lg:w-1/2">
                <User></User>
                
            </div>  
        </div>
       
                
     
    </div>

</template>
<script>
import Person from './personas.vue'
import User from './usuarios.vue'

export default{
    components:{
        Person,
        User
    }
}
</script>