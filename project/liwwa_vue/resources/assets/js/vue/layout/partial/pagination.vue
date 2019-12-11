
<template>
    <div v-if="pages.length > 1" style="overflow:auto;">
        <ul class="pagination">
            <li class="" v-on:click="back()"><span> << </span></li>
            <li v-for="page in pages" v-bind:class="{ active: page==currentPage }" v-on:click="setPage(page)">
                <a  v-on:click="setPage(page)" v-text="page"></a></li>
            <li  v-on:click="next()"><a  rel="next"> >>  </a></li>

        </ul>
        <div ></div>

    </div>


    <div class="noResultDiv" v-else-if="pages.length == 0" >no results</div>


</template>




<script>
    export default{

    props:['total','pagination_size'],
            data(){return {currentPage:1}},

    created(){

//this.createPageArray();

    },
    methods:{

        back(){
            if(this.currentPage <=1){return false;}

            this.setPage(this.currentPage-1);
        },
        next(){
            if(this.currentPage >=Math.ceil(this.total/this.pagination_size)){return false;}
            this.setPage(this.currentPage+1);
        },
        setPage(newPage){


            this.currentPage=newPage;

            this.$emit('changePage', this.currentPage);
        }


    },
    computed:{

        pages(){
            var pages=[];
            for(var i=1;i<=Math.ceil(this.total/this.pagination_size);i++){
                pages.push(i);
            }

            return pages;
        }

    }
    }


</script>