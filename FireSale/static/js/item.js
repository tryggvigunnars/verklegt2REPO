$(document).ready(function() {
    const filterResults = (basedOn, queryParam, onSuccess = () => {}) => {
        $.ajax({
            url: `/store/?${queryParam}=${basedOn}`,
            type: 'GET',
            success: function(resp) {
                console.log("here")
                var newHtml = resp.data.map(d => {
                    return `<div class="item">
                                <div class="itemPicture"><img src="${d.image}"></div>                           
                                <div class="itemInfo">
                                    <h3 class="productName">Product: ${d.name}</h3>
                                    <h6 class="sellerName">Seller name: ${d.user}</h6>
                                    <h6 class="sellerLocation">Location: ${d.location}</h6>
                                </div>
                                <div class="itemInfo2">
                                    <h1 class="listingPrice">${d.price}$</h1>
                                    <a href="/store/${d.id}">
                                        <input type="button" id="viewItem" value="View item details">
                                    </a>
                                </div>  
                            </div>`

                });
                console.log(newHtml)
                $('#displayed_items').html(newHtml.join(''));
                //onSuccess();
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    };

    $('.btn-search').on('click', function(e){
        e.preventDefault();
        const searchText = $('#choices-text-preset-values').val();
        filterResults(searchText, 'search_filter', () => {
            $('#choices-text-preset-values').val('');
        });
    });

    $('#order-by').on('change', function (e) {
       const value = this.value;
       console.log(value)
       filterResults(value, 'order_by');
    });
});