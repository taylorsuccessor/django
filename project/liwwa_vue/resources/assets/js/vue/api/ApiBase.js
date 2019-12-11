import Authorization from "@resource/authorization/Authorization";

export default class ApiBase  {

    setAxiosDefault(){
        // axios.defaults.baseURL = 'https://api.ureed.com';
        // axios.defaults.headers.common['Authorization'] = 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwaWN0dXJlIjoiaHR0cHM6Ly9tZWRpYS1zdGFnaW5nLXVyZWVkLnMzLmFtYXpvbmF3cy5jb20vY2FjaGUvYmMvMjYvYmMyNmEzM2M5MTZmYmZkNDE0MmVhMzFmNTE3MDdiNTcucG5nIiwidXNlcm5hbWUiOiJzYXJhIiwiYXRpYmlVc2VyVHlwZSI6WyJGUiJdLCJzdGF0dXMiOiJBQyIsIm9yaWdfaWF0IjoxNTMzNzE3MDg1LCJlbWFpbCI6InNhcmEuYWxmdWxpQGdtYWlsLmNvbV94eHgiLCJ1c2VyX3R5cGUiOiJmciIsImRpc3BsYXlfbmFtZSI6Ik1vaGFtbWFkIiwiZXhwIjoxNjIwMDMwNjg1LCJpc19yZW1lbWJlcl9tZSI6ZmFsc2UsInVzZXJfaWQiOjE2NiwiZnJlZWxhbmNlcl9pZCI6OTUsImJhbGFuY2UiOjU0LjQxfQ.vzeeYfQ8Dkf0hNxyqyudL47pa6s-UTopxnabNTj5lvU';
        axios.defaults.headers.post['Content-Type'] = 'Application/json; charset=utf-8';
        // axios.defaults.headers.common['X-ADMIN'] = '1';
        // axios.defaults.headers.common['X-CSRF-TOKEN'] = Authorization.csrf_token;

    }
    constructor() {

         this.requestConfig={
             baseURL:process.env.MIX_API_URL,
             url:'',
             method:'get',
             params:{},
             crossdomain: true

         }
this.errorCallback=null;
this.setAxiosDefault();





    }


      request(){
         return  axios(this.requestConfig) .catch( (error) =>{
                  console.log(error);
                  alert('Error, pleas try again later!');
                  if(this.errorCallback != null){
                      this.errorCallback(error);
                  }
              });
    }

    get(url,data={},callback=null){
        this.requestConfig['method']='GET';
        this.requestConfig['url']=url;
        this.requestConfig['params']=data;
        this.request().then(response=>callback(response));

    }

    post(url,data={},callback=null){
        this.requestConfig['method']='POST';
        this.requestConfig['url']=url;
        this.requestConfig['params']=data;
        this.request().then(response=>callback(response));

    }



    patch(url,data={},callback=null){

        this.requestConfig['method']='patch';
        this.requestConfig['url']=url;
        this.requestConfig['params']=data;
        this.request().then(response=>callback(response));

    }

    delete(url){
        this.requestConfig['method']='DELETE';
        this.requestConfig['url']=url;
        this.request();

    }
    upload(url,formData,successCallback,faildCallback,progressCallback){

        return  axios.post(process.env.MIX_API_URL + url,formData,{
            headers: {
                'Content-Type': 'multipart/form-data'
            },
            onUploadProgress: function( progressEvent ) {
                var uploadPercentage = parseInt( Math.round( ( progressEvent.loaded * 100 ) / progressEvent.total ) );
                progressCallback(uploadPercentage);
            }.bind(this)
        }).then(function(response){
            successCallback(response.data);
        })
            .catch(function(error){
                faildCallback(error);
            });
    }


    download(url,resume_id,getFileResponce){

        return  axios({
            baseURL:process.env.MIX_API_URL,
            url:url,
            method:'post',
            params:{id:resume_id},
            crossdomain: true,
            headers:{
                'x-admin':1
            }

        }).then(function(response){
            getFileResponce(response.data);
        })
            .catch(function(error){
                console.log(error);
            });
    }
}
