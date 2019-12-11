
<template>

    <div>




        <div class="modal fade choose-translate-term show" id="chose_translate" tabindex="-1" role="dialog" aria-labelledby="chose_translate" :style="{display:((showModel)?'block':'none')}" style="  padding-left: 0px;">
            <div class="modal-dialog modal-dialog-centered" role="document">
                <div class="modal-content">
                    <button  @click="hide()" type="button" class="close" data-dismiss="modal" aria-label="Close" >
                        <span aria-hidden="true"><img  :src=" 'template_images/icons/modal_close.svg' | assetImage" alt=""></span>
                    </button>
                    <div class="main-dialog">
                        <div class="title">
                            <p class="entry-title">{{boxTitle}} </p>
                            <p class="desc">{{'SELECT_FROM_BELOW_LIST' | translate }} </p>
                        </div>
                        <div class="main-table">
                            <div class="action-row">
                                <div class="search-input form-goup">
                                    <input type="text"  v-model="search.searchText"  class="form-control" :placeholder="'search' | translate ">
                                    <button class="searchbtn" @click="getList();" ><img :src=" 'template_images/icons/search-icon.svg' | assetImage" alt=""></button>
                                </div>
                                <div class="btns" v-if="showCreateButton" >
                                    <button  @click="$emit('showCreate');"  class="b-btn-standart" >{{'CREATE_NEW' | translate }}</button>
                                </div>
                            </div>
                            <div class="main-list">



                                <div class="table-head">
                                    <div class="order__col">
                                        <div class="checkbox-input">
                                            <input type="checkbox" class="custom-checkbox" name="check">
                                            <span></span>
                                        </div>
                                        <p class="">#</p>
                                    </div>
                                    <div class="title__col" v-for="(fieldLabel,field) of fieldList">
                                        <p class="">{{fieldLabel}}</p>
                                    </div>

                                </div>
                                <label   v-for="option of list"    v-bind:class="{ selected: selectedIdList.indexOf(option.id)> -1 }" class="list-item">
                                    <div class="   col-2">
                                        <div class="checkbox-input" style="float:left;">
                                            <input type="checkbox" class="custom-checkbox"  :value="option.id" v-model="selectedIdList" @change="setSelectedList($event)">
                                            <span></span>

                                            <img v-if=" selectedIdList.indexOf(option.id) == -1 " :src=" 'template_images/icons/check-empty.svg' |assetImage">
                                            <img v-if="selectedIdList.indexOf(option.id)> -1 " :src=" 'template_images/icons/check-checked.svg' |assetImage">

                                        </div>
                                        <p class="">{{option.id}}</p>
                                    </div>

                                    <div class="  col-10" v-for="(fieldLabel,field) of fieldList">
                                        <p class="">{{option[field]}}</p>
                                    </div>

                                </label>
                            </div>
                            <div>

                                <pagination  :total="total" @changePage="changePage"  :pagination_size="per_page" ></pagination>

                            </div>
                            <div class="btm-action-row">
                                <div class="btns">
                                    <button @click="hide()"  class="b-btn-standart">{{'CHOOSE' | translate }}</button>
                                </div>
                            </div>




                        </div>
                    </div>
                </div>
            </div>
        </div>














    </div>


</template>




<script>

    import ApiBase from '@resource/api/ApiBase'
    export default{

        props:['showModel','apiUrl','boxTitle','oneOption','showCreateButton','parentSearch'],
        data(){
            return {
                search:{searchText:'',initIdList:[],page:1,per_page:0},
                apiData:[],
                list:[],
                total:0,
                per_page:0,
                selectedIdList:[],
                selectedIdNameList:[],
                api:new ApiBase(),
                fieldList:{"name":"my name"}
            }
        },

        created(){
            // this.selectedIdList=this.parentSelectedIdList.map(function (x) {
            //     return parseInt(x, 10);
            // });
            this.search=this.parentSearch;
           this.selectedIdList= this.search.initIdList;
        },
        mounted(){
            this.getList();
        },
        methods:{
            hide(){

                this.$emit('hide');
            },
            getList(){
                this.api.get(this.apiUrl,this.search,response=>this.setList(response.data));

            },
            setList(response){
                this.search.initIdList=[];

                this.list=this.selectedIdNameList.concat(response.results) ;
                this.list=this.removeDuplicates(this.list);
                this.setSelectedList();
                this.total=response.count;
                this.per_page=response.per_page;
            },
            setSelectedList($event=null){

                var parintSelectedIdList=this.selectedIdList;
                if(this.oneOption ){
                    var oneValue=($event == null)? this.selectedIdList[0]:parseInt($event.target.value);
                    this.selectedIdList=[oneValue];
                    parintSelectedIdList=oneValue;

                }

                this.selectedIdNameList=this.list.filter(option=>this.selectedIdList.indexOf(option.id) > -1);

                this.$emit('setSelectedList', {selectedIdList:parintSelectedIdList,selectedIdNameList:this.selectedIdNameList});
            },
            changePage(page){
                this.search.page=page;
                this.getList();

            },
            removeDuplicates(myArr) {
                return myArr.filter((obj, pos, arr) => {
                    return arr.map(mapObj => mapObj['id']).indexOf(obj['id']) === pos;
                });
            }


        },
        computed:{



        }
    }


</script>
<style lang="scss">

    .popupAllContainer{
        border-bottom:1px solid #eee;
        overflow: auto;

        position:fixed;
        top:0px;
        bottom:0px;
        left:0px;
        right:0px;
        width:100%;
        height:100%;
        z-index:9999;
        h2{
            text-align:center;
            border-bottom:3px solid #eee;
            margin:0px;
            .closeSpan{
                float:right;
                display: inline-block;
                padding:0px 5px;
                cursor:pointer;
            }
        }
        .searchInput{
            width:78%;
        }
        .searchButton{
            width:20%;
            /*border:none;*/
        }

        .shadowBackgroundDiv{
            background:rgba(0,0,0,0.4);
            position:fixed;
            top:0px;
            bottom:0px;
            left:0px;
            right:0px;
            width:100%;
        }
        .popupContentDiv{
            background:#fff;
            z-index: 99999999;
            position:relative;
            display:block;
            margin:auto;
            margin-top:100px;
            width:50%;
            .oneOptionContainer{
                display:block;padding:0px 5px;border-bottom:1px solid #eee;
                font-size:11px;
                margin:0px;
                input[type=checkbox]{display:none;}
                &.selected{
                    background-color: #edffe9;
                    .statusBox{
                        background:green;
                        color:#ffffff;
                    }
                }
                .statusBox{display:inline-block;padding:5px;color:#ffffff; text-align:center;width:100px;}
            }


            @media screen and (max-width: 600px) {
                width: 100%;

                margin-top:0px;
            }
        }

    }

</style>