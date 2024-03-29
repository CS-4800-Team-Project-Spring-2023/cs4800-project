/*!
* Start Bootstrap - Scrolling Nav v5.0.5 (https://startbootstrap.com/template/scrolling-nav)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-scrolling-nav/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});

//Function that is clicked on submit during index.html
//Uses url to obtain resource locations and appends them to index.html
function search() {
	$("#result_list").empty();
	var resource = $('#resourceselect').val();
	$.ajax({
	  url: "http://ec2-52-53-124-118.us-west-1.compute.amazonaws.com/getlocations/" + resource,
	  success: function (res) {
		console.log("The result from the server is: " + res);
		for(var i = 0; i < res.length; i++) {
		  $("#result_list").append('<li class="list-group-item">' + res[i] + "</li>")
		}
	  },
	  error: function(error) {
		console.log("Failed to search." + error);
	  }
	});
  }