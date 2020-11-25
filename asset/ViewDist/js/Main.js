$(document).ready(function () {
    owlcarousel();
    $("#HideOverlay").on("click", function () {
        $(".ovarlay").addClass("add-overlay");
        $(".inner-overlay").addClass("add-inner-ovarlay")
    });
    $("#CloseOverlay").on("click", function () {
        $(".ovarlay").removeClass("add-overlay");
        $(".inner-overlay").removeClass("add-inner-ovarlay")
    });
    $('.ovarlay').mousedown(function () {
        $(".ovarlay").removeClass("add-overlay");
        $(".inner-overlay").removeClass("add-inner-ovarlay")
    });

    if ($(".product-page").length) {
        $(document).ready(function () {
            $('[data-toggle="tooltip"]').tooltip()
            $('#myTab a').on('click', function (e) {
                e.preventDefault()
                $(this).tab('show')
            });
        });
    }

    if ($(".register-page").length) {
        $('#login-form-btn').on('click', function () {
            $("#login-form").show();
            $("#register-form").hide();
            $("#register-form-btn").removeClass('register-btn-active');
            $("#login-form-btn").addClass('register-btn-active');
        });
        $('#register-form-btn').on('click', function () {
            $("#login-form").hide();
            $("#register-form").show();
            $("#register-form-btn").addClass('register-btn-active');
            $("#login-form-btn").removeClass('register-btn-active');
        });
    }


    if ($(".card-page").length) {
        var totalPrice = document.getElementById("card-total-price");
        var ConvertPrice = document.getElementById("card-convert-price");
        var Price = document.getElementById("card-price");
        var addCount = document.getElementById("card-add-link")
        var lowCount = document.getElementById("card-low-link");
        var PriceShow = document.getElementById("card-inner-price-show");
        var number = document.getElementById("cardCount")
        addCount.onclick = function () {
            let number = document.getElementById("cardCount");
            let n = parseInt($(number).text());
            let t = n * 200
            number.innerHTML = `${n + 1}`;
            Price.innerHTML = `${t + 200},000`;
            totalPrice.innerText = `${(t + 200) + 9},000`
        }
        lowCount.onclick = function () {
            let number = document.getElementById("cardCount")
            let n = parseInt($(number).text());
            if (n > 1) {
                let t = n * 200;
                number.innerHTML = `${n - 1}`;
                Price.innerHTML = `${t - 200},000`;
                totalPrice.innerText = `${(t - 200) + 9},000`
            }
        }
    }

    if ($(".perfume-page").length) {
        var perfumeRange = document.getElementById("perfume-range");
        var perfumeRangeShow = document.getElementById("perfume-range-show");
        perfumeRange.value = '10000000';
        perfumeRangeShow.innerHTML = perfumeRange.value;
        perfumeRange.addEventListener("input", rangePerfume);

        function rangePerfume() {
            perfumeRangeShow.innerHTML = perfumeRange.value;
        }
    }
})

function owlcarousel() {
    $(".owl-carousel").each(function () {
        var a = $(this);
        a.owlCarousel({
            rtl: a.data("rtl"),
            items: a.data("items"),
            slideBy: a.data("slideby"),
            center: a.data("center"),
            loop: a.data("loop"),
            margin: a.data("margin"),
            dots: a.data("dots"),
            nav: a.data("nav"),
            stagePadding: a.data("padding"),
            autoplay: a.data("autoplay"),
            autoplayTimeout: a.data("autoplay-timeout"),
            navText: ['<span class="las la-angle-double-right f-4 blue-color"></span>', '<span class="las la-angle-double-left f-4 blue-color"></span>'],
            autoplayHoverPause: a.data("pause"),
            lazyLoad: a.data("lazy"),
            responsive: {
                0: {
                    items: a.data("xs-items") ? a.data("xs-items") : 1,
                    stagePadding: a.data("xs-padding"),
                    nav: a.data("xs-nav")
                },
                576: {
                    items: a.data("sm-items"),
                    stagePadding: a.data("sm-padding"),
                    nav: a.data("sm-nav")
                },
                768: {
                    items: a.data("md-items"),
                    stagePadding: a.data("md-padding"),
                    nav: a.data("md-nav")
                },
                1024: {
                    items: a.data("lg-items"),
                    stagePadding: a.data("lg-padding"),
                    nav: a.data("lg-nav")
                },
                1200: {
                    stagePadding: a.data("xl-padding"),
                    nav: a.data("xl-nav")
                }
            }
        })
    })
}