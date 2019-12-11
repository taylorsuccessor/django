<template>
    <div>
<router-link to="/vue/register/" class="btn btn-primary form-control"> Resume List </router-link>
        <div class="testbox" style="width:50%; margin:0px 25%;">
            <form v-on:submit.prevent="submit">

                <p>Candidate  Information</p>
                <div class="item">
                    <label for="name">Full Name<span>*</span></label>
                    <input id="name" type="text" v-model="model.full_name" name="full_name" required/>
                </div>
                <div class="item">
                <label for="date_of_birth">Date of Birth<span>*</span></label>
                <input id="date_of_birth" type="date" v-model="model.date_of_birth"  name="bdate" required/>
                <i class="fas fa-calendar-alt"></i>
                </div>

                <div class="item">
                <label for="experience_years">Experience Years<span>*</span></label>
                <input id="experience_years" type="text"  v-model="model.experience_years"  name="experience_years" required/>
                </div>

                <div class="question">
                <label>Department</label>
                <div class="question-answer">


                    <div>
                        <input type="radio"  value="HR" id="HR" name="department_id"v-model="model.department_id" />
                        <label for="HR" class="radio"><span>HR</span></label>
                    </div>

                    <div>
                        <input type="radio" value="IT" id="IT" name="department_id" v-model="model.department_id" />
                        <label for="IT" class="radio"><span>IT</span></label>
                    </div>

                    <div>
                        <input type="radio" value="FINANCE" id="FINANCE" name="department_id" v-model="model.department_id" />
                        <label for="FINANCE" class="radio"><span>FINANCE</span></label>
                    </div>



                </div>
                </div>


                <div class="item">
                    <label for="experience_years">Resume<span>*</span></label>
                    <input type="file" id="file" ref="file"  />
                </div>






                <div class="btn-block">
                    <div  style="text-align: center; padding:5px;color:blue;">{{progress}}</div>
                    <button v-if="progress == 'uploading not start yet.'" type="submit" href="/">SUBMIT</button>
                   </div>
            </form>
        </div>
    </div>
</template>



<script>

    import service from '@module/register/vue/service/service';

    import ApiBase from '@resource/api/ApiBase'
        export default{
        data(){
            return {
                file:null,
                progress:'uploading not start yet.',

                model:{},
                errors:{}

                        
        }
        },
        created(){

        },
        mounted(){











        
        },
        methods:{
            submit(){

                this.file = this.$refs.file.files[0];
                var uploadFormData = new FormData();
                uploadFormData.append('full_name', this.model.full_name);
                uploadFormData.append('date_of_birth', this.model.date_of_birth);
                uploadFormData.append('experience_years', this.model.experience_years);
                uploadFormData.append('department_id', this.model.department_id);
                uploadFormData.append('resume', this.file);

                new ApiBase().upload('/api/register/', uploadFormData, this.success,this.faild,this.progressCallback);



            },
            postResult(response){

                // this.data=response;

                this.errors={};
                notification(this,translate('createdSuccessfully'));
                this.$router.push({name:'vue.map.index'});
            },
            postError(error){
                this.errors=error.response.data.errors;
            },

            success( data) {
             console.log('success');
                this.progress = 'Resume uploaded successfully'

            },
            faild(fileIndex, error) {

                this.progress = 'Sorry, please try again later.'
                console.log('faild');
            },
            progressCallback(  uploadPercentage) {
                this.progress =uploadPercentage+'% uploading ...';
                console.log(uploadPercentage);
                },



                },

    }


</script>



