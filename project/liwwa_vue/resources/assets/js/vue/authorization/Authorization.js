export default class Authorization{



constructor(){
}
     static checkIfPermissionMatch(onePermissionToCheck,allUserPermission) {


        var roleArray = new Array();
        roleArray = onePermissionToCheck.split('.');

        var rolePattern = roleArray.join('|\\*)\\.(')
        rolePattern = '\\|(' + rolePattern + '|\\*)';


        const pattern = new RegExp(rolePattern, 'ig');

        return allUserPermission.match(pattern) ? true : false;

    }
    static allow(onePermissionToCheck){
        return Authorization.checkIfPermissionMatch(onePermissionToCheck,Authorization.allow_permission);

    }

    static deny(onePermissionToCheck){
        return Authorization.checkIfPermissionMatch(onePermissionToCheck,Authorization.deny_permission);

    }

    static can(permission){

        // return (($this->deny($permission))? false:true);
        return(Authorization.allow(permission))? ((Authorization.deny(permission))? false:true):false;
    }


     static authorization(to, from, next)  {

// if(typeof to.name == 'undefined'){to.name=to.path.replace('/','.');}

        if(Authorization.can(to.name)){
            next();
        }

    }
}




window.authorization=Authorization.authorization;
window.can=Authorization.can;