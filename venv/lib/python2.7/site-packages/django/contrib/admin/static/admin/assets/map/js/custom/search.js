function searchList(searchInput,listSelector){
    var listItems=$(listSelector);
    var searchText=searchInput.val().toLowerCase();

    listItems.each(function(){
        var listItem=$(this);
        if(listItem.text().toLowerCase().match(new RegExp('.*'+searchText+'.*'))){
            listItem.show();
        }else{
            listItem.hide();
        }
    });

}
