
<template>








    <div class=" side-mini-panel"   >
        <ul class="mini-nav">
            <div class="togglediv" onclick="$('body').addClass('content-wrapper');$('.selected').addClass(' cnt-none');$('#togglebtn').hide();"><a href="javascript:void(0)" id="togglebtn"><i class="ti-menu"></i></a></div>






            <li  v-for="(menuSection,index) in menuList" onmouseover="$('.side-mini-panel .selected').removeClass('selected');$(this).addClass('selected');$(this).removeClass(' cnt-none');$('body').removeClass('content-wrapper');$('#togglebtn').show();" c v-bind:class="{ selected: index==0 }" >
                <a href="javascript:void(0)"><i :class="'fa  '+menuSection.icon " data-icon="v"></i></a>
                <div class="sidebarmenu">
                    <h3 class="menu-title">{{menuSection.title }}</h3>
                    <div class="searchable-menu">
                        <form role="search" class="menu-search">
                            <input type="text" placeholder="Search..." class="form-control"> <a href=""><i class="fa fa-search"></i></a> </form>
                    </div>
                    <ul class="sidebar-menu">



                        <li v-for="menu in menuSection.submenu">

                            <router-link :to="menu.link"> {{ menu.title | translate }}</router-link>
                        </li>



                        <hr>
                    </ul>
                </div>
            </li>



        </ul>
    </div>











</template>




<script>
    export default{

        props:[],
        data(){
            return {
                menuList:[
                    // {
                    //     'title':'project',
                    //     'icon':'fa-credit-card',
                    //     'link':'link',
                    //     'submenu':[
                    //         {
                    //             'title':'projectIndex',
                    //             'icon':'sssf',
                    //             'link':'/vue/project',
                    //         }
                    //
                    //     ]
                    //
                    //
                    // },
                ]
            }
        },

        created(){
        },
        methods:{

// showMainMenu(selectedLi){
//
// }


        },
        computed:{


        }
    }


</script>