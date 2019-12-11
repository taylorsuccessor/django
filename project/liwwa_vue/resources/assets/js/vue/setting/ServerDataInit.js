import User from "@resource/user/User";
import Authorization from "@resource/authorization/Authorization";

export default class ServerDataInit{


    constructor(serverData){
        User.user=serverData.user;

        Authorization.allow_permission='|'+serverData.allow_permission;
        Authorization.deny_permission='|'+serverData.deny_permission;
        Authorization.csrf_token= serverData.csrf_token;
        window.locale=serverData.locale;
        console.log(1111,serverData);
        ServerDataInit.setLocale(locale);
    }

    static setLocale(locale){
        var body= document.getElementsByTagName('body')[0];
        if(locale=='ar'){
            body.classList.add('rtlTemplate');
        }else{

            body.classList.remove('rtlTemplate');
        }
    }

}