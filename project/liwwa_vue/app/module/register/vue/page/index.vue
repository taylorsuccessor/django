
<template>

<div>








<router-link to="/vue/register/create/" class="btn btn-primary form-control"> Register new Candidate  </router-link>

    <div class="limiter">
        <div class="container-table100">
            <div class="wrap-table100">
                <div class="table">

                    <div class="row header">
                        <div class="cell">
                            Full Name
                        </div>
                        <div class="cell">
                            Date of Birth
                        </div>
                        <div class="cell">
                            Experience Years
                        </div>
                        <div class="cell">
                            Department
                        </div>
                        <div class="cell">
                            Resume
                        </div>
                    </div>

                    <div class="row"  v-for="oResult in data.results ">
                        <div class="cell" data-title="Full Name">
                            {{oResult.full_name}}
                        </div>
                        <div class="cell" data-title="Age">
                            {{oResult.date_of_birth}}
                        </div>
                        <div class="cell" data-title="Job Title">
                            {{oResult.experience_years}}
                        </div>
                        <div class="cell" data-title="Location">
                            {{oResult.department_id}}
                        </div>
                        <div class="cell" data-title="Location">

                            <a v-on:click ="downladFile(oResult.id)" >Download Resume</a>

                        </div>
                    </div>


                </div>
            </div>
        </div>
    </div>













</div>


</template>


<script>
    import service from '@module/register/vue/service/service';


    import ApiBase from '@resource/api/ApiBase'
    export default{
        data(){
            return {
                data:{'count': 0, 'results': [] ,per_page:15},
                search:{page:1 }
            }
        },
        created(){
            this.getData();
        },
        mounted(){
           },


        methods:{


            setDataResult(response){
                console.log(response)
                this.data=response;
                this.total=response.count  ;
            },
            getData(){


                new service().getList(this.search,this.setDataResult);



            },
            downladFile(id){
                new ApiBase().download('api/download_resume/',id,this.successDownladFile);

            },
            successDownladFile(response){
                window.open(response.url, "_blank");
            }

        },

    }


</script>











<style type="text/css">


    /*//////////////////////////////////////////////////////////////////
    [ FONT ]*/


    @font-face {
        font-family: Poppins-Regular;
        /*src: url('../fonts/poppins/Poppins-Regular.ttf');*/
    }

    @font-face {
        font-family: Poppins-Bold;
        /*src: url('../fonts/poppins/Poppins-Bold.ttf');*/
    }

    /*//////////////////////////////////////////////////////////////////
    [ RESTYLE TAG ]*/
    * {
        margin: 0px;
        padding: 0px;
        box-sizing: border-box;
    }

    body, html {
        height: 100%;
        font-family: sans-serif;
    }

    /* ------------------------------------ */
    a {
        margin: 0px;
        transition: all 0.4s;
        -webkit-transition: all 0.4s;
        -o-transition: all 0.4s;
        -moz-transition: all 0.4s;
    }

    a:focus {
        outline: none !important;
    }

    a:hover {
        text-decoration: none;
    }

    /* ------------------------------------ */
    h1,h2,h3,h4,h5,h6 {margin: 0px;}

    p {margin: 0px;}

    ul, li {
        margin: 0px;
        list-style-type: none;
    }


    /* ------------------------------------ */
    input {
        display: block;
        outline: none;
        border: none !important;
    }

    textarea {
        display: block;
        outline: none;
    }

    textarea:focus, input:focus {
        border-color: transparent !important;
    }

    /* ------------------------------------ */
    button {
        outline: none !important;
        border: none;
        background: transparent;
    }

    button:hover {
        cursor: pointer;
    }

    iframe {
        border: none !important;
    }


    /*//////////////////////////////////////////////////////////////////
    [ Table ]*/

    .limiter {
        width: 100%;
        margin: 0 auto;
    }

    .container-table100 {
        width: 100%;
        min-height: 100vh;
        background: #c4d3f6;

        display: -webkit-box;
        display: -webkit-flex;
        display: -moz-box;
        display: -ms-flexbox;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
        padding: 33px 30px;
    }

    .wrap-table100 {
        width: 960px;
        border-radius: 10px;
        overflow: hidden;
    }

    .table {
        width: 100%;
        display: table;
        margin: 0;
    }

    @media screen and (max-width: 768px) {
        .table {
            display: block;
        }
    }

    .row {
        display: table-row;
        background: #fff;
    }

    .row.header {
        color: #ffffff;
        background: #6c7ae0;
    }

    @media screen and (max-width: 768px) {
        .row {
            display: block;
        }

        .row.header {
            padding: 0;
            height: 0px;
        }

        .row.header .cell {
            display: none;
        }

        .row .cell:before {
            font-family: Poppins-Bold;
            font-size: 12px;
            color: #808080;
            line-height: 1.2;
            text-transform: uppercase;
            font-weight: unset !important;

            margin-bottom: 13px;
            content: attr(data-title);
            min-width: 98px;
            display: block;
        }
    }

    .cell {
        display: table-cell;
    }

    @media screen and (max-width: 768px) {
        .cell {
            display: block;
        }
    }

    .row .cell {
        font-family: Poppins-Regular;
        font-size: 15px;
        color: #666666;
        line-height: 1.2;
        font-weight: unset !important;

        padding-top: 20px;
        padding-bottom: 20px;
        border-bottom: 1px solid #f2f2f2;
    }

    .row.header .cell {
        font-family: Poppins-Regular;
        font-size: 18px;
        color: #fff;
        line-height: 1.2;
        font-weight: unset !important;

        padding-top: 19px;
        padding-bottom: 19px;
    }

    .row .cell:nth-child(1) {
        width: 360px;
        padding-left: 40px;
    }

    .row .cell:nth-child(2) {
        width: 160px;
    }

    .row .cell:nth-child(3) {
        width: 250px;
    }

    .row .cell:nth-child(4) {
        width: 190px;
    }


    .table, .row {
        width: 100% !important;
    }

    .row:hover {
        background-color: #ececff;
        cursor: pointer;
    }

    @media (max-width: 768px) {
        .row {
            border-bottom: 1px solid #f2f2f2;
            padding-bottom: 18px;
            padding-top: 30px;
            padding-right: 15px;
            margin: 0;
        }

        .row .cell {
            border: none;
            padding-left: 30px;
            padding-top: 16px;
            padding-bottom: 16px;
        }
        .row .cell:nth-child(1) {
            padding-left: 30px;
        }

        .row .cell {
            font-family: Poppins-Regular;
            font-size: 18px;
            color: #555555;
            line-height: 1.2;
            font-weight: unset !important;
        }

        .table, .row, .cell {
            width: 100% !important;
        }
    }
</style>

