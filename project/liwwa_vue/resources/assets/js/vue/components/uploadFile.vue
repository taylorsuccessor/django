<template>
  <div>


    <label for="file">
      <div class="drop-zone__blck" style="position:relative;overflow:hidden;">
        <div class="img"><img :src="'template_images/drop-zone.svg' | assetImage" alt=""></div>
        <div class="desk">
          <p>Drag and drop your file hire or
            <span class="p-light-green">browse</span> to begin upload
          </p>
        </div>
        <input style="position: absolute; left:0;top:0px;padding: 200%;" type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>

      </div>
    </label>


    <div class="load__blck" v-for="file of fileList" v-if="typeof file.hide =='undefined'">
      <p class="title">{{file.index}} - <a :href="file.upload_base_url+file.new_name">{{file.original_name}}</a></p>
      <div class="load-line">
        <div class="load-progress">
          <div class="load-line" :style="'width:'+file.progress+'%;'"></div>
        </div>
        <p class="load-progress-perc">{{file.progress}}%</p>
        <svg @click=" deleteRow(file.id,file.index)" width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd"
                d="M11.0342 12.1792L15.6533 16.7983L16.8457 15.6062L12.2266 10.9871L16.8447 6.36816L15.6533 5.17627L11.0342 9.79517L6.41504 5.17603L5.22266 6.36816L9.8418 10.9873L5.22266 15.6064L6.41504 16.7986L11.0342 12.1792Z"
                fill="#64C0B6"></path>
        </svg>
      </div>
      <p class="action" v-if="file.progress < 100 && file.progress > 0">(Uploading...)</p>
    </div>


  </div>
</template>
<script>

  import ApiBase from '@resource/api/ApiBase'

  export default {
    props: ['upload_group_id'],
    data() {
      return {
        file: "",
        index: 0,
        fileList: [],

      }
    },
    created() {

    },
    mounted() {

      if (this.upload_group_id > 0) {
        new ApiBase().get('/general/upload_file/upload_group_file_list', {upload_group_id: this.upload_group_id}, this.setFileList);
      }
    },
    methods: {
      handleFileUpload() {
        this.addSelectedFileToList();
        this.file = this.$refs.file.files[0];
        var changeFile = ''
        if (this.validateFileMem() == false) {
          var error = 'you cant upload this file'
          var changeFile = this.fileList[this.index];
          changeFile['original_name'] = 'Fail';
          changeFile['progress'] = 0;
          this.$emit('faild', error);

          return;
        }
        var api = new ApiBase();
        var uploadFormData = new FormData();
        uploadFormData.append('upload_file', this.file);
        uploadFormData.append('upload_group_id', this.upload_group_id);

        api.upload('/general/upload_file/ajax', uploadFormData, this.index, this.success, this.faild, this.progress);
        this.index += 1;
      },
      addSelectedFileToList() {

        var filePath = this.$refs.file.value;

        var basename = filePath.replace(/\\/g, '/').split('/').pop();
        this.fileList.push({index: this.index, progress: 0, upload_base_url: '#', new_name: '#', original_name: basename, id: 0});

      },

      validateFileMem() {
        var ext = this.file.name.substr(this.file.name.lastIndexOf('.') + 1);

        if (['xlsx', 'xls', 'tmx'].indexOf(ext) > -1) {

          return true;
        } else {

          return false

        }

        // this.faild()
      },
      success(fileIndex, data) {
        this.$emit('success', data);
        var changeFile = data;
        changeFile['index'] = fileIndex;
        changeFile['progress'] = 100;
        this.fileList.splice(fileIndex, 1, changeFile);

      },
      faild(fileIndex, error) {
        var changeFile = this.fileList[fileIndex];
        changeFile['original_name'] = 'Fail';
        changeFile['progress'] = 0;

        this.fileList.splice(fileIndex, 1, changeFile);

        this.$emit('faild', error);
      },
      progress(fileIndex, uploadPercentage) {
        var changeFile = this.fileList[fileIndex];
        changeFile['progress'] = uploadPercentage;
        this.fileList.splice(fileIndex, 1, changeFile);
        this.$emit('progress', {fileIndex: fileIndex, uploadPercentage: uploadPercentage});
      },
      setFileList(response) {
        this.fileList = response.data.results;
        this.index = this.fileList.length;
      },
      deleteRow(id, index) {
        if (!confirm('Are you sure that you want delete ?')) {
          return false;
        }

        if (id == 0 || typeof id == 'undefined') {

          var tempFile = this.fileList[index];
          tempFile['hide'] = true;
          this.fileList.splice(index, 1, tempFile);

          return false;
        }
        new ApiBase().get('general/upload_file/destroy/' + id, {index: index}, this.deleteResult);


      },
      deleteResult(result) {
        if (result.data.status == 'success') {
          var tempFile = this.fileList[result.data.index];
          tempFile['hide'] = true;
          this.fileList.splice(result.data.index, 1, tempFile);
        } else {

        }
      }
    },

  }


</script>
