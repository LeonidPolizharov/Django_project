function fetch_products(category, page) {
   return fetch('/products/${category}/${page}/products/')
        .then(function (response) {
            return response.text();
        }).then(function(data) {
            $('.category-products').html(data);
        });
}
    

function init_page_navigation() {
    $('a.next-page').on('click', function (event) {
        event.preventDefault();
        fetch_products(event.target.dataset.category, event.target.dataset.page)
            .then(init_page_navigation);
    })
    $('a.previous-page').on('click', function (event) {
        event.preventDefault();
        fetch_products(event.target.dataset.category, event.target.dataset.page)
            .then(init_page_navigation);
    });
}


window.onload = function () {
    fetch_products(PAGE_DATA.categoryId, PAGE_DATA.page).then(init_page_navigation);
}