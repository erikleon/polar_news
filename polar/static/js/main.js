(function($, window, document, undefined) {
  var init = function () {
    // carouselInit();
    formHandler();
  },
  query_polar = function() {
    $.ajax({
        url : "query_polar/", // the endpoint
        type : "POST", // http method
        data : { query : $('#query-text').val() }, // data sent with the post request
        // handle a successful response
        success : function(json) {
          for (var i = 0; i < Object.keys(json['results']['articles']).length; i++) {
            html = '<li class="article-list-item"><span class="source-brand"><img src=""></span><span><a target="_blank" href="'+json['results']['articles'][i]['url']+'"><div class="article-title">'+json['results']['articles'][i]['title']+'</div><div class="article-url">'+json['results']['articles'][i]['url']+'</div></a></span></li>';
            if (json['results']['articles'][i]['source_position'] > 0.5) {
              $('.results .right ul').append(html);
            } else {
              $('.results .left ul').append(html);
            }
          }
          $('.results').removeClass('error');
          $('.results').addClass('success');
          $('.loader').removeClass('active');
          $('.loader').addClass('success');
        },
        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('.results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            $('.results').addClass('success');
            $('.results').addClass('error');
            $('.loader').removeClass('active');
        }
    });
  }
  formHandler = function () {
    $('#post-form').on('submit', function(event){
      event.preventDefault();
      console.log("form submitted!")  // sanity check
      console.log($('#query-text').val());
      $('.loader').addClass('active');
      query_polar();
    });
  },
  // This function gets cookie with a given name
  getCookie = function (name) {
      var cookieValue = null;
      if (document.cookie && document.cookie != '') {
          var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
              var cookie = jQuery.trim(cookies[i]);
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) == (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  },
  csrftoken = getCookie('csrftoken'),
  /* The functions below will create a header with csrftoken */
  csrfSafeMethod = function (method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  },
  sameOrigin = function (url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
      (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
      // or any other URL that isn't scheme relative or absolute i.e relative.
      !(/^(\/\/|http:|https:).*/.test(url));
  },

  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
              // Send the token to same-origin, relative URLs only.
              // Send the token only if the method warrants CSRF protection
              // Using the CSRFToken value acquired earlier
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });

  init();
})(jQuery, window, document);
