
<template>


    <div class="row bg-title" style="background:url(/assets/admin/plugins/images/heading-title-bg.jpg) no-repeat center center /cover;">
        <div class="col-lg-12">
            <h4 class="page-title"  v-text="moduleName"></h4>
        </div>
        <div class="col-sm-6 col-md-6 col-xs-12">
            <ol class="breadcrumb pull-left">
                <li><a href="#"  v-text="first">   </a></li>
                <li class="active"  v-text="second"></li>
            </ol>
        </div>
        <div class="col-sm-6 col-md-6 col-xs-12">
            <form role="search" class="app-search hidden-xs pull-right">
                <input type="text" placeholder=" Searche ..." class="form-control">
                <a href="javascript:void(0)"><i class="fa fa-search"></i></a>
            </form>
        </div>
    </div>


</template>




<script>
    export default{

    props:['moduleName','first','second'],
            data(){
        return {

            }
            },

    created(){
    },
    methods:{




    },
    computed:{


    }
    }


</script>