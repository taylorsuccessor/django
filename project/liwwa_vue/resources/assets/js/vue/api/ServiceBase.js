import ApiBase from '@resource/api/ApiBase'

export default class ServiceBase extends ApiBase{
constructor(){
    super();

}

    getOne(id,callback){
        super.get(this.moduleUrl+id,{},response=>callback(response.data));
    }

    getList(data,callback){
        super.get(this.moduleUrl,data,response=>callback(response.data));
    }

    post(data,callback){
        super.post(this.moduleUrl,data,response=>callback(response.data));
    }


    patch(id,data,callback){

    super.patch(this.moduleUrl+id,data,response=>callback(response.data));
    }

    delete(id){
        super.delete(this.moduleUrl+id);
    }

}