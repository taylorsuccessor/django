<template>
    <div >
  this my {{ip}}internal component {{message}}
<p>
{{myFunction('variableToEdit')}}
    </p>
<ul>
    <li v-for="row in rows" v-text="row.name"></li>
    </ul>
    </div>
</template>
<script>
export default{
    data(){
        return {
            message:"my componenet message",
            ip:'',
            rows:[],
        }
    },
    created(){
        console.log('created');
        axios.post('http://localhost:8000/json',{email:'taylorsuccessor@gmail.com',password:'123456'}).then((response)=>{
            this.ip=response.data.ip;
            this.rows=response.data.rows;
        });
    },
    mounted(){
        console.log('mounted');
    },
    methods:{
        myFunction(myValue){return "the following variable ("+myValue+") come from method";}
    },

}


</script>