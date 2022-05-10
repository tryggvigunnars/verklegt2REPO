$(document).ready(function() {
    $('.btn-search').on('click', function(e){
        e.preventDefault();
        var searchText = $('#choices-text-preset-values').val();
        $.ajax({
            url: '/store?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    console.log(d);
                    return `<div class="item">
                                <div className="itemPicture"><img src="${d.image}" style="width: 80px;">
                                <a href="/store/${d.id}">
                                   <h3>${d.item_name}</h3>
                                   <h6>${d.user}</h6>
                                   <h6>${d.location}</h6>
                                   <h1>${d.price}</h1>
                                </a>     
                            </div>`
                });

                /*<div className="item">
                    <div className="itemPicture"><img src="{{ info.itemimage_set.first.img }}" style="width: 80px;">
                    </div>
                    <div className="itemInfo">
                        <h3 className="productName">Product: {{info.item_name}}</h3>
                        <h6 className="sellerName">Seller name: {{info.user}}</h6>
                        <h6 className="sellerLocation">Location: {{info.location}}</h6>
                    </div>
                    <div className="itemInfo2">
                        <h1 className="listingPrice">{{info.price}} kr.</h1>
                        <input type="button" href="/store/{{ info.id }}" id="viewItem" value="View item details">

                    </div>
                </div>*/
                $('#displayed_items').html(newHtml.join(''));
                $('#choices-text-preset-values').val('');
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        })
    });
});