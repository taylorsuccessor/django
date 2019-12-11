



















import Echo from "laravel-echo";

/**
 * First we will load all of this project's JavaScript dependencies which
 * includes Vue and other libraries. It is a great starting point when
 * building robust, powerful web applications using Vue and Laravel.
 */
require('./bootstrap');

window.Vue = require('vue');


/**
 * Next, we will create a fresh Vue application instance and attach it to
 * the page. Then, you may begin adding components to this application
 * or customize the JavaScript scaffolding to fit your unique needs.
 */

//Vue.component('example', require('./components/Example.vue'));

import VueRouter from 'vue-router';
Vue.use(VueRouter);


import register_routes  from '@module/register/vue/route';
let router=  new VueRouter({ routes:register_routes
      });






import Notifications from 'vue-notification'


Vue.use(Notifications);

Vue.component('pagination', require('@resource/layout/partial/pagination'));
Vue.component('popupSelect', require('@resource/layout/partial/modal'));
Vue.component('header-banner', require('@resource/layout/partial/headerBanner'));
Vue.component('app-header', require('@resource/layout/partial/header'));
Vue.component('upload-file', require('@resource/components/uploadFile'));

import { Datetime } from 'vue-datetime';
import 'vue-datetime/dist/vue-datetime.css'
Vue.component('datetime', Datetime);
//<datetime v-model="model.name" type="time" format="yyyy-MM-dd"  input-class="form-control"></datetime>




Vue.filter('translate', function (value) {

    return value ;//translate(value);
});


Vue.filter('transLookups', function (id,lookupsKey) {

    return transLookups(id,lookupsKey);
});



Vue.filter('canPipe', function (value) {

    return can(value);
});


window.Moment = require('moment');
Vue.filter('formatDate', function (value,format) {
    var momentValue=Moment(value);

    return momentValue.format(format);
});

Vue.filter('assetImage', function (value) {

    return process.env.MIX_ASSETS_URL + value;
});



Vue.prototype.$channel=function(channel,event,callback){

    if(process.env.MIX_CHANNEL_DRIVER =='pusher'){
        window.Echo.private(channel).listen(event,callback);

    }else if(process.env.MIX_CHANNEL_DRIVER =='node_channel'){
        event=event.replace(/^\./g,"");
        console.log(event);
        window.nodeChannel.channel('private-'+channel,event,callback);

    }
}


var app = null;
import ServerDataInit from '@resource/setting/ServerDataInit';
function initApp(){


    new ServerDataInit({});
    // updateMeta(Authorization.csrf_token);




    app = new Vue({
        el: '#mainAppContainer',
        router:router,
    });

}


import ApiBase from '@resource/api/ApiBase'
import Authorization from "./authorization/Authorization";



initApp();
