/*___________________________________helper_functions*/

/*__________________________time*/

function convertSecondsToText(timeDifirint,negative){
    negative=(timeDifirint<0 || negative==true)? true:false;
    timeDifirint=Math.abs(timeDifirint);

    var daysNumber=Math.floor(timeDifirint/86400);
    var reminderSeconds=timeDifirint- (daysNumber*86400);

    var  hoursNumber=Math.floor(reminderSeconds/3600);
    reminderSeconds=reminderSeconds- (hoursNumber*3600);
    var momentsNumber=Math.floor(reminderSeconds/60);
    reminderSeconds=reminderSeconds- (momentsNumber*60);


    var timeString=' ';//(negative == true)? 'After ':'Before ';
    timeString+=(daysNumber > 0)? ''+daysNumber +' day , ':'';
    timeString+=(hoursNumber > 0)? hoursNumber +' hour , ':'';
    timeString+=(momentsNumber > 0)? momentsNumber +' minute , ':'';
    timeString+=(reminderSeconds > 0)? reminderSeconds +' second ':'';
    timeString=(timeString=='before ')? 'Now':timeString;


    return timeString;
}
function getHour(time){

    timeDifirint=Math.abs(time);

    var daysNumber=Math.floor(timeDifirint/86400);
    var reminderSeconds=timeDifirint- (daysNumber*86400);

    var  hoursNumber=Math.floor(reminderSeconds/3600);
    reminderSeconds=reminderSeconds- (hoursNumber*3600);
    var momentsNumber=Math.floor(reminderSeconds/60);
    reminderSeconds=reminderSeconds- (momentsNumber*60);

    var timeString='';

    timeString+=(daysNumber > 0)? ''+daysNumber +':':'';
    timeString+=(hoursNumber > 0)? hoursNumber +':':'00';
    timeString+=(momentsNumber > 0)?  momentsNumber :'00';


    return timeString;
}



function calculateDifferenceTime(valuestart,valuestop) {

    //create date format 86400
    var valuestartArray=valuestart.split(':');
    valuestart=(valuestartArray[0].length<2 ? '0'+valuestartArray[0]:valuestartArray[0])+':'+(valuestartArray[1]<10 ? '0'+valuestartArray[1]:valuestartArray[1])+':00';

    var valuestopArray=valuestop.split(':');
    valuestop=(valuestopArray[0].length<2 ? '0'+valuestopArray[0]:valuestopArray[0])+':'+(valuestopArray[1]<10 ? '0'+valuestopArray[1]:valuestopArray[1])+':00';

    var timeStart = new Date('1970-01-01 ' + valuestart ).getTime()  ;// new Date("01/01/2007 " + valuestart);
    var timeEnd =new Date('1970-01-01 ' + valuestop ).getTime() ;// new Date("01/01/2007 " + valuestop);

    var difference = Math.abs(timeEnd - timeStart)/1000 ;

    var diff_result = new Date(difference);

    var differenceType='onTime';
    if(timeEnd > timeStart && difference /(60) > 10  ){

        differenceType='early';

    }else if(timeEnd < timeStart && difference /(60)  > 10  ){

        differenceType='delay';
    }


    return [
        differenceType,
        convertSecondsToText(difference)
    ];




}
function fixNumber(number){

    return (number < 10)? '0'+number:number;
}
function hourToSecond(hour){

    var hourArray=hour.split(':');

    return (parseInt(hourArray[0])*60*60)+(parseInt(hourArray[1])*60);
}


function secondToHour(second){
//        var date = new Date(null);
//        date.setSeconds(second); // specify value for SECONDS here
//        return date.toISOString().substr(11, 8);


    var  hoursNumber=Math.floor(second/3600);
    var reminderSeconds=second - (hoursNumber*3600);
    var momentsNumber=Math.floor(reminderSeconds/60);
    reminderSeconds=reminderSeconds- (momentsNumber*60);



    return fixNumber(hoursNumber)+':'+fixNumber(momentsNumber);
}
/*__________________End_time*/


/*_______________________________End____helper_functions*/