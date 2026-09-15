// Dean Attali / Beautiful Jekyll 2023

let BeautifulJekyllJS = {

  bigImgEl : null,
  numImgs : null,

  init : function() {
    setTimeout(BeautifulJekyllJS.initNavbar, 10);

    // Shorten the navbar after scrolling a little bit down
    $(window).scroll(function() {
        if ($(".navbar").offset().top > 50) {
            $(".navbar").addClass("top-nav-short");
        } else {
            $(".navbar").removeClass("top-nav-short");
        }
    });

    // On mobile, hide the avatar when expanding the navbar menu
    $('#main-navbar').on('show.bs.collapse', function () {
      $(".navbar").addClass("top-nav-expanded");
    });
    $('#main-navbar').on('hidden.bs.collapse', function () {
      $(".navbar").removeClass("top-nav-expanded");
    });

    // show the big header image
    BeautifulJekyllJS.initImgs();

    BeautifulJekyllJS.initSearch();

    BeautifulJekyllJS.initScrollEffects();

    BeautifulJekyllJS.initNavbarStars();

    BeautifulJekyllJS.initSkyTwinkleStars();
  },

  initNavbar : function() {
    // Set the navbar-dark/light class based on its background color
    const rgb = $('.navbar').css("background-color").replace(/[^\d,]/g,'').split(",");
    const brightness = Math.round(( // http://www.w3.org/TR/AERT#color-contrast
      parseInt(rgb[0]) * 299 +
      parseInt(rgb[1]) * 587 +
      parseInt(rgb[2]) * 114
    ) / 1000);
    if (brightness <= 125) {
      $(".navbar").removeClass("navbar-light").addClass("navbar-dark");
    } else {
      $(".navbar").removeClass("navbar-dark").addClass("navbar-light");
    }
  },

  initNavbarStars : function() {
    // Sprinkle layered twinkling stars (white + rare pink/blue accents) over the black navbar sky.
    // Three layers (background / mid / foreground) make the sky feel deep & scattered.
    var nav = document.querySelector('.navbar-custom');
    if (!nav || document.querySelector('.navbar-star')) { return; }

    var count = 320;
    var i, star, layer, accent;
    for (i = 0; i < count; i++) {
      star = document.createElement('span');
      // rare blue accents, occasional pink accent
      if (i % 37 === 11)      { accent = 'navbar-star--blue'; }
      else if (i % 11 === 0)  { accent = 'navbar-star--pink'; }
      else                    { accent = ''; }

      // layer roll: 45% tiny dim background, 35% mid, 20% bright foreground
      var roll = Math.random();
      if (roll < 0.45)      { layer = 'bg'; }
      else if (roll < 0.80) { layer = 'md'; }
      else                  { layer = 'fg'; }

      star.className = 'navbar-star navbar-star--' + layer + (accent ? ' ' + accent : '');

      // different size per layer (all tiny, fg slightly larger & glowing)
      var size;
      if (layer === 'bg') { size = Math.random() * 0.5 + 0.5; }
      else if (layer === 'md') { size = Math.random() * 0.7 + 0.7; }
      else { size = Math.random() * 1.0 + 1.0; }
      star.style.width = size.toFixed(1) + 'px';
      star.style.height = star.style.width;
      star.style.left = (Math.random() * 100).toFixed(2) + '%';
      // cover the FULL navbar height (0-100% of it) so the bottom edge has stars too.
      // Use rem-based top so it scales with the navbar regardless of its pixel height.
      star.style.top = (Math.random() * 100).toFixed(1) + '%';
      star.style.animationDelay = (Math.random() * 6).toFixed(2) + 's';
      star.style.animationDuration = (Math.random() * 3.4 + 1.6).toFixed(2) + 's';
      nav.appendChild(star);
    }
  },

  initSkyTwinkleStars : function() {
    // Overlay individually-twinkling stars on the tiled starfield sky.
    //
    // The sky itself is one tiled background layer, so animating it would pulse
    // every star in lockstep. Instead we add a fraction of the stars (5%, per
    // --sky-twinkle-pct) as separate elements, each with its own random delay
    // and duration, so the sparkle looks scattered.
    //
    // Only runs on pages that opted into the starfield via `body-class: starry`.
    var body = document.body;
    if (!body || !body.classList.contains('starry')) { return; }
    if (document.querySelector('.starry-twinkle-layer')) { return; }

    var styles = getComputedStyle(document.documentElement);
    var density = parseFloat(styles.getPropertyValue('--sky-density'));
    var pct = parseFloat(styles.getPropertyValue('--sky-twinkle-pct'));
    // Accent mix comes from the stylesheet too, so these stay in step with the
    // generated sky instead of drifting from it as hard-coded numbers.
    var bluePct = parseFloat(styles.getPropertyValue('--sky-blue-pct')) || 0;
    var redPct = parseFloat(styles.getPropertyValue('--sky-red-pct')) || 0;
    if (!density || !pct) { return; }

    var layer = document.createElement('div');
    layer.className = 'starry-twinkle-layer';
    layer.setAttribute('aria-hidden', 'true');
    body.appendChild(layer);

    var count = Math.round(window.innerWidth * window.innerHeight * density * pct);
    // Keep the DOM light on very large displays.
    count = Math.min(count, 260);
    if (count < 1) { return; }

    var i, star, roll;
    for (i = 0; i < count; i++) {
      star = document.createElement('span');
      // carry the tiled sky's palette: mostly white, occasional blue/red
      roll = Math.random();
      if (roll < bluePct) {
        star.className = 'starry-twinkle starry-twinkle--blue';
      } else if (roll < bluePct + redPct) {
        star.className = 'starry-twinkle starry-twinkle--red';
      } else {
        star.className = 'starry-twinkle';
      }
      // Sits in the upper-middle of the tiled sky's size range (0.63-4px) so
      // the twinkling stars do not all read as one uniform size on top of it.
      // Deliberately not scaled to the full ceiling: a large star pulsing is
      // distracting, so the biggest sizes are left to the static tiled layer
      // and the twinkle stays a small-to-medium accent.
      var size = Math.random() * 1.5 + 1.0;
      star.style.width = size.toFixed(1) + 'px';
      star.style.height = star.style.width;
      star.style.left = (Math.random() * 100).toFixed(2) + '%';
      star.style.top = (Math.random() * 100).toFixed(2) + '%';
      // stagger the timing so they do not blink together
      star.style.animationDelay = (Math.random() * 5).toFixed(2) + 's';
      star.style.animationDuration = (Math.random() * 2.6 + 1.8).toFixed(2) + 's';
      layer.appendChild(star);
    }
  },

  initImgs : function() {
    // If the page was large images to randomly select from, choose an image
    if ($("#header-big-imgs").length > 0) {
      BeautifulJekyllJS.bigImgEl = $("#header-big-imgs");
      BeautifulJekyllJS.numImgs = BeautifulJekyllJS.bigImgEl.attr("data-num-img");

      // 2fc73a3a967e97599c9763d05e564189
      // set an initial image
      const imgInfo = BeautifulJekyllJS.getImgInfo();
      const src = imgInfo.src;
      const desc = imgInfo.desc;
      BeautifulJekyllJS.setImg(src, desc);

      // For better UX, prefetch the next image so that it will already be loaded when we want to show it
      const getNextImg = function() {
        const imgInfo = BeautifulJekyllJS.getImgInfo();
        const src = imgInfo.src;
        const desc = imgInfo.desc;

        const prefetchImg = new Image();
        prefetchImg.src = src;
        // if I want to do something once the image is ready: `prefetchImg.onload = function(){}`

        setTimeout(function(){
          const img = $("<div></div>").addClass("big-img-transition").css("background-image", 'url(' + src + ')');
          $(".intro-header.big-img").prepend(img);
          setTimeout(function(){ img.css("opacity", "1"); }, 50);

          // after the animation of fading in the new image is done, prefetch the next one
          //img.one("transitioned webkitTransitionEnd oTransitionEnd MSTransitionEnd", function(){
          setTimeout(function() {
            BeautifulJekyllJS.setImg(src, desc);
            img.remove();
            getNextImg();
          }, 1000);
          //});
        }, 6000);
      };

      // If there are multiple images, cycle through them
      if (BeautifulJekyllJS.numImgs > 1) {
        getNextImg();
      }
    }
  },

  getImgInfo : function() {
    const randNum = Math.floor((Math.random() * BeautifulJekyllJS.numImgs) + 1);
    const src = BeautifulJekyllJS.bigImgEl.attr("data-img-src-" + randNum);
    const desc = BeautifulJekyllJS.bigImgEl.attr("data-img-desc-" + randNum);

    return {
      src : src,
      desc : desc
    }
  },

  setImg : function(src, desc) {
    $(".intro-header.big-img").css("background-image", 'url(' + src + ')');
    if (typeof desc !== typeof undefined && desc !== false) {
      $(".img-desc").text(desc).show();
    } else {
      $(".img-desc").hide();
    }
  },

  initSearch : function() {
    if (!document.getElementById("beautifuljekyll-search-overlay")) {
      return;
    }

    $("#nav-search-link").click(function(e) {
      e.preventDefault();
      $("#beautifuljekyll-search-overlay").show();
      $("#nav-search-input").focus().select();
      $("body").addClass("overflow-hidden");
    });
    $("#nav-search-exit").click(function(e) {
      e.preventDefault();
      $("#beautifuljekyll-search-overlay").hide();
      $("body").removeClass("overflow-hidden");
    });
    $(document).on('keyup', function(e) {
      if (e.key == "Escape") {
        $("#beautifuljekyll-search-overlay").hide();
        $("body").removeClass("overflow-hidden");
      }
    });
  },

  initScrollEffects : function() {
    // 1) Scroll progress bar — a shooting star racing across the top of the page
    var bar = document.createElement('div');
    bar.id = 'scroll-progress';
    document.body.appendChild(bar);

    // the comet head: a bright glowing dot at the leading edge of the progress
    var comet = document.createElement('div');
    comet.className = 'scroll-progress-head';
    bar.appendChild(comet);

    function updateProgress() {
      var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      var docHeight = document.documentElement.scrollHeight - window.innerHeight;
      var pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
      bar.style.width = pct + '%';
    }
    window.addEventListener('scroll', updateProgress, { passive: true });
    updateProgress();

    // 2) Fade-in-up on scroll for cards and sections
    var revealEls = document.querySelectorAll('.research-card, .pub-card, .research-grid, .profile-intro, .home-welcome, .home-news, .welcome-card, .posts-list .post-preview, .pub-lightbox, .post-preview, .blog-tags, .main-content .post-entry, .home-news__title, .home-news__list');
    if (revealEls.length === 0) { return; }

    revealEls.forEach(function(el) {
      if (el.classList.contains('scroll-reveal')) { return; }
      el.classList.add('scroll-reveal');
    });

    if (!('IntersectionObserver' in window)) {
      revealEls.forEach(function(el) { el.classList.add('scroll-reveal-visible'); });
      return;
    }

    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('scroll-reveal-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

    revealEls.forEach(function(el) { observer.observe(el); });
  }
};

// 2fc73a3a967e97599c9763d05e564189

document.addEventListener('DOMContentLoaded', BeautifulJekyllJS.init);
